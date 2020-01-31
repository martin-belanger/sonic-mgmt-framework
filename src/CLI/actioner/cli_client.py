################################################################################
#                                                                              #
#  Copyright 2019 Broadcom. The term Broadcom refers to Broadcom Inc. and/or   #
#  its subsidiaries.                                                           #
#                                                                              #
#  Licensed under the Apache License, Version 2.0 (the "License");             #
#  you may not use this file except in compliance with the License.            #
#  You may obtain a copy of the License at                                     #
#                                                                              #
#     http://www.apache.org/licenses/LICENSE-2.0                               #
#                                                                              #
#  Unless required by applicable law or agreed to in writing, software         #
#  distributed under the License is distributed on an "AS IS" BASIS,           #
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    #
#  See the License for the specific language governing permissions and         #
#  limitations under the License.                                              #
#                                                                              #
################################################################################

import os
import json
import urllib3
import pwd
from six.moves.urllib.parse import quote
import syslog
import requests

urllib3.disable_warnings()

sess = requests.Session()

class ApiClient(object):
    """
    A client for accessing a RESTful API
    """

    def __init__(self):
        """
        Create a RESTful API client.
        """

        uri_root = 'https://localhost:8443'
        self.api_uri = os.getenv('REST_API_ROOT', uri_root)

        self.checkCertificate = False

        self.version = "0.0.1"

        if sess.cert is None:
            cert = os.getenv('USER_CERT_PATH', None)
            key = os.getenv('USER_KEY_PATH', None)
            if cert and key:
                sess.cert = (cert, key)
            else:
                username = os.getenv('CLI_USER', None)
                if username is not None:
                    certdir = os.path.join(pwd.getpwnam(username)[5], ".cert")
                    cert = os.path.join(certdir, "certificate.pem")
                    key = os.path.join(certdir, "key.pem")
                    sess.cert = (cert, key)

    def set_headers(self):
        from requests.structures import CaseInsensitiveDict
        return CaseInsensitiveDict({
            'User-Agent': "CLI"
        })

    def request(self, method, path, data=None, headers={}, query=None):
        from requests import request, RequestException

        url = '{0}{1}'.format(self.api_uri, path)

        req_headers = self.set_headers()
        req_headers.update(headers)

        client_token = os.getenv('REST_API_TOKEN', None)

        if client_token:
            syslog.syslog(syslog.LOG_DEBUG, "cli_client request using token %s" % client_token)
            req_headers['Authorization'] = "Bearer " + client_token

        body = None
        if data is not None:
            if 'Content-Type' not in req_headers:
                req_headers['Content-Type'] = 'application/yang-data+json'
            body = json.dumps(data)

        try:
            r = sess.request(
                method,
                url,
                headers=req_headers,
                data=body,
                params=query,
                verify=self.checkCertificate)
            return Response(r)
        except RequestException as e:
            syslog.syslog(syslog.LOG_WARNING, "cli_client request exception %s" % str(e))
            #TODO have more specific error message based
            return self._make_error_response('%Error: Could not connect to Management REST Server')

    def post(self, path, data={}):
        return self.request("POST", path, data)

    def get(self, path, depth=None):
        q = self.prepare_query(depth=depth)
        return self.request("GET", path, query=q)

    def head(self, path, depth=None):
        q = self.prepare_query(depth=depth)
        return self.request("HEAD", path, query=q)

    def put(self, path, data={}):
        return self.request("PUT", path, data)

    def patch(self, path, data={}):
        return self.request("PATCH", path, data)

    def delete(self, path):
        return self.request("DELETE", path, None)

    @staticmethod
    def prepare_query(depth=None):
        query = {}
        if depth != None and depth != "unbounded":
            query["depth"] = depth
        return query

    @staticmethod
    def _make_error_response(errMessage, errType='client', errTag='operation-failed'):
        import requests
        r = Response(requests.Response())
        r.content = {'ietf-restconf:errors':{ 'error':[ {
            'error-type':errType, 'error-tag':errTag, 'error-message':errMessage }]}}
        return r

    def cli_not_implemented(self, hint):
        return self._make_error_response('%Error: not implemented {0}'.format(hint))


class Path(object):
    def __init__(self, template, **kwargs):
        self.template = template
        self.params = kwargs
        self.path = template
        for k, v in kwargs.items():
            self.path = self.path.replace('{%s}' % k, quote(v, safe=''))

    def __str__(self):
        return self.path


class Response(object):
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        self.content = response.content

        try:
            if response.content is None or len(response.content) == 0:
                self.content = None
            elif _has_json_content(response):
                self.content = json.loads(response.content)
        except ValueError:
            # TODO Can we set status_code to 5XX in this case???
            # Json parsing can fail only if server returned bad json
            self.content = response.content

    def ok(self):
        return self.status_code >= 200 and self.status_code <= 299

    def errors(self):
        if self.ok():
            return {}

        errors = self.content

        if(not isinstance(errors, dict)):
            errors = {"error": errors}  # convert to dict for consistency
        elif('ietf-restconf:errors' in errors):
            errors = errors['ietf-restconf:errors']

        return errors

    def error_message(self, formatter_func=None):
        if hasattr(self, 'err_message_override'):
            return self.err_message_override

        err = self.errors().get('error')
        if err == None:
            return None
        if isinstance(err, list):
            err = err[0]
        if isinstance(err, dict):
            if formatter_func is not None:
                return formatter_func(self.status_code, err)
            return default_error_message_formatter(self.status_code, err)
        return str(err)

    def set_error_message(self, message):
        self.err_message_override = add_error_prefix(message)

    def __getitem__(self, key):
        return self.content[key]

def _has_json_content(resp):
    ctype = resp.headers.get('Content-Type')
    return (ctype is not None and 'json' in ctype)

def _has_json_content(resp):
    ctype = resp.headers.get('Content-Type')
    return (ctype is not None and 'json' in ctype)

def default_error_message_formatter(status_code, err_entry):
    if 'error-message' in err_entry:
        err_msg = err_entry['error-message']
        return add_error_prefix(err_msg)
    err_tag = err_entry.get('error-tag')
    if err_tag == 'invalid-value':
        return '%Error: validation failed'
    if err_tag == 'operation-not-supported':
        return '%Error: not supported'
    if err_tag == 'access-denied':
        return '%Error: not authorized'
    return '%Error: operation failed'

def add_error_prefix(err_msg):
    if not err_msg.startswith("%Error"):
        return '%Error: ' + err_msg
    return err_msg


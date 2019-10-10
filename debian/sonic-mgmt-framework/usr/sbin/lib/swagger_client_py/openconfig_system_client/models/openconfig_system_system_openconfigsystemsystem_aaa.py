# coding: utf-8

"""
    Sonic Network Management APIs

    Network management Open APIs for Sonic.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_aaa_accounting import OpenconfigSystemSystemOpenconfigsystemsystemAaaAccounting  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_aaa_authentication import OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthentication  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_aaa_authorization import OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthorization  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_aaa_servergroups import OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroups  # noqa: F401,E501


class OpenconfigSystemSystemOpenconfigsystemsystemAaa(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'authentication': 'OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthentication',
        'authorization': 'OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthorization',
        'accounting': 'OpenconfigSystemSystemOpenconfigsystemsystemAaaAccounting',
        'server_groups': 'OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroups'
    }

    attribute_map = {
        'authentication': 'authentication',
        'authorization': 'authorization',
        'accounting': 'accounting',
        'server_groups': 'server-groups'
    }

    def __init__(self, authentication=None, authorization=None, accounting=None, server_groups=None):  # noqa: E501
        """OpenconfigSystemSystemOpenconfigsystemsystemAaa - a model defined in Swagger"""  # noqa: E501

        self._authentication = None
        self._authorization = None
        self._accounting = None
        self._server_groups = None
        self.discriminator = None

        if authentication is not None:
            self.authentication = authentication
        if authorization is not None:
            self.authorization = authorization
        if accounting is not None:
            self.accounting = accounting
        if server_groups is not None:
            self.server_groups = server_groups

    @property
    def authentication(self):
        """Gets the authentication of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501


        :return: The authentication of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthentication
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """Sets the authentication of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.


        :param authentication: The authentication of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthentication
        """

        self._authentication = authentication

    @property
    def authorization(self):
        """Gets the authorization of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501


        :return: The authorization of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthorization
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """Sets the authorization of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.


        :param authorization: The authorization of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthorization
        """

        self._authorization = authorization

    @property
    def accounting(self):
        """Gets the accounting of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501


        :return: The accounting of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemAaaAccounting
        """
        return self._accounting

    @accounting.setter
    def accounting(self, accounting):
        """Sets the accounting of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.


        :param accounting: The accounting of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemAaaAccounting
        """

        self._accounting = accounting

    @property
    def server_groups(self):
        """Gets the server_groups of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501


        :return: The server_groups of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroups
        """
        return self._server_groups

    @server_groups.setter
    def server_groups(self, server_groups):
        """Sets the server_groups of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.


        :param server_groups: The server_groups of this OpenconfigSystemSystemOpenconfigsystemsystemAaa.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroups
        """

        self._server_groups = server_groups

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OpenconfigSystemSystemOpenconfigsystemsystemAaa, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OpenconfigSystemSystemOpenconfigsystemsystemAaa):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

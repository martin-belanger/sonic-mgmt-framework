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

from openconfig_system_client.models.openconfig_system_system_dns_config_search import OpenconfigSystemSystemDnsConfigSearch  # noqa: F401,E501


class PostOpenconfigSystemSystemDnsConfigSearch(object):
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
        'openconfig_systemsearch': 'list[str]'
    }

    attribute_map = {
        'openconfig_systemsearch': 'openconfig-system:search'
    }

    def __init__(self, openconfig_systemsearch=None):  # noqa: E501
        """PostOpenconfigSystemSystemDnsConfigSearch - a model defined in Swagger"""  # noqa: E501

        self._openconfig_systemsearch = None
        self.discriminator = None

        if openconfig_systemsearch is not None:
            self.openconfig_systemsearch = openconfig_systemsearch

    @property
    def openconfig_systemsearch(self):
        """Gets the openconfig_systemsearch of this PostOpenconfigSystemSystemDnsConfigSearch.  # noqa: E501


        :return: The openconfig_systemsearch of this PostOpenconfigSystemSystemDnsConfigSearch.  # noqa: E501
        :rtype: list[str]
        """
        return self._openconfig_systemsearch

    @openconfig_systemsearch.setter
    def openconfig_systemsearch(self, openconfig_systemsearch):
        """Sets the openconfig_systemsearch of this PostOpenconfigSystemSystemDnsConfigSearch.


        :param openconfig_systemsearch: The openconfig_systemsearch of this PostOpenconfigSystemSystemDnsConfigSearch.  # noqa: E501
        :type: list[str]
        """

        self._openconfig_systemsearch = openconfig_systemsearch

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
        if issubclass(PostOpenconfigSystemSystemDnsConfigSearch, dict):
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
        if not isinstance(other, PostOpenconfigSystemSystemDnsConfigSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

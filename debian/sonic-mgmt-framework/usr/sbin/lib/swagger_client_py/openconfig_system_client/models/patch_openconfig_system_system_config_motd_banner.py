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

from openconfig_system_client.models.openconfig_system_system_config_motd_banner import OpenconfigSystemSystemConfigMotdBanner  # noqa: F401,E501


class PatchOpenconfigSystemSystemConfigMotdBanner(object):
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
        'openconfig_systemmotd_banner': 'str'
    }

    attribute_map = {
        'openconfig_systemmotd_banner': 'openconfig-system:motd-banner'
    }

    def __init__(self, openconfig_systemmotd_banner=None):  # noqa: E501
        """PatchOpenconfigSystemSystemConfigMotdBanner - a model defined in Swagger"""  # noqa: E501

        self._openconfig_systemmotd_banner = None
        self.discriminator = None

        if openconfig_systemmotd_banner is not None:
            self.openconfig_systemmotd_banner = openconfig_systemmotd_banner

    @property
    def openconfig_systemmotd_banner(self):
        """Gets the openconfig_systemmotd_banner of this PatchOpenconfigSystemSystemConfigMotdBanner.  # noqa: E501


        :return: The openconfig_systemmotd_banner of this PatchOpenconfigSystemSystemConfigMotdBanner.  # noqa: E501
        :rtype: str
        """
        return self._openconfig_systemmotd_banner

    @openconfig_systemmotd_banner.setter
    def openconfig_systemmotd_banner(self, openconfig_systemmotd_banner):
        """Sets the openconfig_systemmotd_banner of this PatchOpenconfigSystemSystemConfigMotdBanner.


        :param openconfig_systemmotd_banner: The openconfig_systemmotd_banner of this PatchOpenconfigSystemSystemConfigMotdBanner.  # noqa: E501
        :type: str
        """

        self._openconfig_systemmotd_banner = openconfig_systemmotd_banner

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
        if issubclass(PatchOpenconfigSystemSystemConfigMotdBanner, dict):
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
        if not isinstance(other, PatchOpenconfigSystemSystemConfigMotdBanner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

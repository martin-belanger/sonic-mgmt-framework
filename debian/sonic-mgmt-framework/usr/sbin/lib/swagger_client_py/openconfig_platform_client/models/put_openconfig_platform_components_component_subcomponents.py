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

from openconfig_platform_client.models.openconfig_platform_components_component_subcomponents import OpenconfigPlatformComponentsComponentSubcomponents  # noqa: F401,E501
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_subcomponents import OpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponents  # noqa: F401,E501


class PutOpenconfigPlatformComponentsComponentSubcomponents(object):
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
        'openconfig_platformsubcomponents': 'OpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponents'
    }

    attribute_map = {
        'openconfig_platformsubcomponents': 'openconfig-platform:subcomponents'
    }

    def __init__(self, openconfig_platformsubcomponents=None):  # noqa: E501
        """PutOpenconfigPlatformComponentsComponentSubcomponents - a model defined in Swagger"""  # noqa: E501

        self._openconfig_platformsubcomponents = None
        self.discriminator = None

        if openconfig_platformsubcomponents is not None:
            self.openconfig_platformsubcomponents = openconfig_platformsubcomponents

    @property
    def openconfig_platformsubcomponents(self):
        """Gets the openconfig_platformsubcomponents of this PutOpenconfigPlatformComponentsComponentSubcomponents.  # noqa: E501


        :return: The openconfig_platformsubcomponents of this PutOpenconfigPlatformComponentsComponentSubcomponents.  # noqa: E501
        :rtype: OpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponents
        """
        return self._openconfig_platformsubcomponents

    @openconfig_platformsubcomponents.setter
    def openconfig_platformsubcomponents(self, openconfig_platformsubcomponents):
        """Sets the openconfig_platformsubcomponents of this PutOpenconfigPlatformComponentsComponentSubcomponents.


        :param openconfig_platformsubcomponents: The openconfig_platformsubcomponents of this PutOpenconfigPlatformComponentsComponentSubcomponents.  # noqa: E501
        :type: OpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponents
        """

        self._openconfig_platformsubcomponents = openconfig_platformsubcomponents

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
        if issubclass(PutOpenconfigPlatformComponentsComponentSubcomponents, dict):
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
        if not isinstance(other, PutOpenconfigPlatformComponentsComponentSubcomponents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

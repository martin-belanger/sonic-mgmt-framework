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

from openconfig_platform_client.models.openconfig_platform_components_component_subcomponents_subcomponent_config import OpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig  # noqa: F401,E501
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_config import OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig  # noqa: F401,E501


class PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig(object):
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
        'openconfig_platformconfig': 'OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig'
    }

    attribute_map = {
        'openconfig_platformconfig': 'openconfig-platform:config'
    }

    def __init__(self, openconfig_platformconfig=None):  # noqa: E501
        """PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig - a model defined in Swagger"""  # noqa: E501

        self._openconfig_platformconfig = None
        self.discriminator = None

        if openconfig_platformconfig is not None:
            self.openconfig_platformconfig = openconfig_platformconfig

    @property
    def openconfig_platformconfig(self):
        """Gets the openconfig_platformconfig of this PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig.  # noqa: E501


        :return: The openconfig_platformconfig of this PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig.  # noqa: E501
        :rtype: OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig
        """
        return self._openconfig_platformconfig

    @openconfig_platformconfig.setter
    def openconfig_platformconfig(self, openconfig_platformconfig):
        """Sets the openconfig_platformconfig of this PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig.


        :param openconfig_platformconfig: The openconfig_platformconfig of this PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig.  # noqa: E501
        :type: OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig
        """

        self._openconfig_platformconfig = openconfig_platformconfig

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
        if issubclass(PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig, dict):
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
        if not isinstance(other, PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

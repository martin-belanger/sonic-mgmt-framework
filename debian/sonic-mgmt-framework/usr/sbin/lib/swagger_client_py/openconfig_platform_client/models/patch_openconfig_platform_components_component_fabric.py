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

from openconfig_platform_client.models.openconfig_platform_components_component_fabric import OpenconfigPlatformComponentsComponentFabric  # noqa: F401,E501


class PatchOpenconfigPlatformComponentsComponentFabric(object):
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
        'openconfig_platformfabric': 'object'
    }

    attribute_map = {
        'openconfig_platformfabric': 'openconfig-platform:fabric'
    }

    def __init__(self, openconfig_platformfabric=None):  # noqa: E501
        """PatchOpenconfigPlatformComponentsComponentFabric - a model defined in Swagger"""  # noqa: E501

        self._openconfig_platformfabric = None
        self.discriminator = None

        if openconfig_platformfabric is not None:
            self.openconfig_platformfabric = openconfig_platformfabric

    @property
    def openconfig_platformfabric(self):
        """Gets the openconfig_platformfabric of this PatchOpenconfigPlatformComponentsComponentFabric.  # noqa: E501


        :return: The openconfig_platformfabric of this PatchOpenconfigPlatformComponentsComponentFabric.  # noqa: E501
        :rtype: object
        """
        return self._openconfig_platformfabric

    @openconfig_platformfabric.setter
    def openconfig_platformfabric(self, openconfig_platformfabric):
        """Sets the openconfig_platformfabric of this PatchOpenconfigPlatformComponentsComponentFabric.


        :param openconfig_platformfabric: The openconfig_platformfabric of this PatchOpenconfigPlatformComponentsComponentFabric.  # noqa: E501
        :type: object
        """

        self._openconfig_platformfabric = openconfig_platformfabric

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
        if issubclass(PatchOpenconfigPlatformComponentsComponentFabric, dict):
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
        if not isinstance(other, PatchOpenconfigPlatformComponentsComponentFabric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

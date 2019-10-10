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


class GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode(object):
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
        'openconfig_if_ethernetnegotiated_duplex_mode': 'str'
    }

    attribute_map = {
        'openconfig_if_ethernetnegotiated_duplex_mode': 'openconfig-if-ethernet:negotiated-duplex-mode'
    }

    def __init__(self, openconfig_if_ethernetnegotiated_duplex_mode=None):  # noqa: E501
        """GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ethernetnegotiated_duplex_mode = None
        self.discriminator = None

        if openconfig_if_ethernetnegotiated_duplex_mode is not None:
            self.openconfig_if_ethernetnegotiated_duplex_mode = openconfig_if_ethernetnegotiated_duplex_mode

    @property
    def openconfig_if_ethernetnegotiated_duplex_mode(self):
        """Gets the openconfig_if_ethernetnegotiated_duplex_mode of this GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode.  # noqa: E501


        :return: The openconfig_if_ethernetnegotiated_duplex_mode of this GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode.  # noqa: E501
        :rtype: str
        """
        return self._openconfig_if_ethernetnegotiated_duplex_mode

    @openconfig_if_ethernetnegotiated_duplex_mode.setter
    def openconfig_if_ethernetnegotiated_duplex_mode(self, openconfig_if_ethernetnegotiated_duplex_mode):
        """Sets the openconfig_if_ethernetnegotiated_duplex_mode of this GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode.


        :param openconfig_if_ethernetnegotiated_duplex_mode: The openconfig_if_ethernetnegotiated_duplex_mode of this GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["FULL", "HALF"]  # noqa: E501
        if openconfig_if_ethernetnegotiated_duplex_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `openconfig_if_ethernetnegotiated_duplex_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(openconfig_if_ethernetnegotiated_duplex_mode, allowed_values)
            )

        self._openconfig_if_ethernetnegotiated_duplex_mode = openconfig_if_ethernetnegotiated_duplex_mode

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
        if issubclass(GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode, dict):
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
        if not isinstance(other, GetOpenconfigIfEthernetInterfacesInterfaceEthernetStateNegotiatedDuplexMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

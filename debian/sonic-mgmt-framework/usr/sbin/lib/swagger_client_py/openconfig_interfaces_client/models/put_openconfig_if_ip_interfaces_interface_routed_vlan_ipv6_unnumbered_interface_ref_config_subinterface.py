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

from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv6_unnumbered_interface_ref_config_subinterface import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface  # noqa: F401,E501


class PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface(object):
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
        'openconfig_if_ipsubinterface': 'int'
    }

    attribute_map = {
        'openconfig_if_ipsubinterface': 'openconfig-if-ip:subinterface'
    }

    def __init__(self, openconfig_if_ipsubinterface=None):  # noqa: E501
        """PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ipsubinterface = None
        self.discriminator = None

        if openconfig_if_ipsubinterface is not None:
            self.openconfig_if_ipsubinterface = openconfig_if_ipsubinterface

    @property
    def openconfig_if_ipsubinterface(self):
        """Gets the openconfig_if_ipsubinterface of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface.  # noqa: E501


        :return: The openconfig_if_ipsubinterface of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_if_ipsubinterface

    @openconfig_if_ipsubinterface.setter
    def openconfig_if_ipsubinterface(self, openconfig_if_ipsubinterface):
        """Sets the openconfig_if_ipsubinterface of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface.


        :param openconfig_if_ipsubinterface: The openconfig_if_ipsubinterface of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface.  # noqa: E501
        :type: int
        """

        self._openconfig_if_ipsubinterface = openconfig_if_ipsubinterface

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
        if issubclass(PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface, dict):
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
        if not isinstance(other, PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6UnnumberedInterfaceRefConfigSubinterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

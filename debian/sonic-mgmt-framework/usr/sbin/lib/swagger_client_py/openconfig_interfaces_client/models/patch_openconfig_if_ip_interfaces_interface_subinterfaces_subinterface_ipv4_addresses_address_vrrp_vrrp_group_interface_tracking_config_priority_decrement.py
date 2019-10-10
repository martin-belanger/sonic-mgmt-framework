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

from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv4_addresses_address_vrrp_vrrp_group_interface_tracking_config_priority_decrement import OpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement  # noqa: F401,E501


class PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement(object):
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
        'openconfig_if_ippriority_decrement': 'int'
    }

    attribute_map = {
        'openconfig_if_ippriority_decrement': 'openconfig-if-ip:priority-decrement'
    }

    def __init__(self, openconfig_if_ippriority_decrement=None):  # noqa: E501
        """PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ippriority_decrement = None
        self.discriminator = None

        if openconfig_if_ippriority_decrement is not None:
            self.openconfig_if_ippriority_decrement = openconfig_if_ippriority_decrement

    @property
    def openconfig_if_ippriority_decrement(self):
        """Gets the openconfig_if_ippriority_decrement of this PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement.  # noqa: E501


        :return: The openconfig_if_ippriority_decrement of this PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_if_ippriority_decrement

    @openconfig_if_ippriority_decrement.setter
    def openconfig_if_ippriority_decrement(self, openconfig_if_ippriority_decrement):
        """Sets the openconfig_if_ippriority_decrement of this PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement.


        :param openconfig_if_ippriority_decrement: The openconfig_if_ippriority_decrement of this PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement.  # noqa: E501
        :type: int
        """

        self._openconfig_if_ippriority_decrement = openconfig_if_ippriority_decrement

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
        if issubclass(PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement, dict):
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
        if not isinstance(other, PatchOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv4AddressesAddressVrrpVrrpGroupInterfaceTrackingConfigPriorityDecrement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

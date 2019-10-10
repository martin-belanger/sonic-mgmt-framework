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

from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_addresses_address_vrrp_vrrp_group_config_preempt_delay import OpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay  # noqa: F401,E501


class PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay(object):
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
        'openconfig_if_ippreempt_delay': 'int'
    }

    attribute_map = {
        'openconfig_if_ippreempt_delay': 'openconfig-if-ip:preempt-delay'
    }

    def __init__(self, openconfig_if_ippreempt_delay=None):  # noqa: E501
        """PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ippreempt_delay = None
        self.discriminator = None

        if openconfig_if_ippreempt_delay is not None:
            self.openconfig_if_ippreempt_delay = openconfig_if_ippreempt_delay

    @property
    def openconfig_if_ippreempt_delay(self):
        """Gets the openconfig_if_ippreempt_delay of this PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay.  # noqa: E501


        :return: The openconfig_if_ippreempt_delay of this PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_if_ippreempt_delay

    @openconfig_if_ippreempt_delay.setter
    def openconfig_if_ippreempt_delay(self, openconfig_if_ippreempt_delay):
        """Sets the openconfig_if_ippreempt_delay of this PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay.


        :param openconfig_if_ippreempt_delay: The openconfig_if_ippreempt_delay of this PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay.  # noqa: E501
        :type: int
        """

        self._openconfig_if_ippreempt_delay = openconfig_if_ippreempt_delay

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
        if issubclass(PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay, dict):
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
        if not isinstance(other, PutOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6AddressesAddressVrrpVrrpGroupConfigPreemptDelay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

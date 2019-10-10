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

from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_config_dhcp_client import OpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigDhcpClient  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_config_dup_addr_detect_transmits import OpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigDupAddrDetectTransmits  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_config_enabled import OpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_subinterfaces_subinterface_ipv6_config_mtu import OpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigMtu  # noqa: F401,E501


class PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled(object):
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
        'openconfig_if_ipenabled': 'bool',
        'openconfig_if_ipmtu': 'int',
        'openconfig_if_ipdup_addr_detect_transmits': 'int',
        'openconfig_if_ipdhcp_client': 'bool'
    }

    attribute_map = {
        'openconfig_if_ipenabled': 'openconfig-if-ip:enabled',
        'openconfig_if_ipmtu': 'openconfig-if-ip:mtu',
        'openconfig_if_ipdup_addr_detect_transmits': 'openconfig-if-ip:dup-addr-detect-transmits',
        'openconfig_if_ipdhcp_client': 'openconfig-if-ip:dhcp-client'
    }

    def __init__(self, openconfig_if_ipenabled=None, openconfig_if_ipmtu=None, openconfig_if_ipdup_addr_detect_transmits=None, openconfig_if_ipdhcp_client=None):  # noqa: E501
        """PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ipenabled = None
        self._openconfig_if_ipmtu = None
        self._openconfig_if_ipdup_addr_detect_transmits = None
        self._openconfig_if_ipdhcp_client = None
        self.discriminator = None

        if openconfig_if_ipenabled is not None:
            self.openconfig_if_ipenabled = openconfig_if_ipenabled
        if openconfig_if_ipmtu is not None:
            self.openconfig_if_ipmtu = openconfig_if_ipmtu
        if openconfig_if_ipdup_addr_detect_transmits is not None:
            self.openconfig_if_ipdup_addr_detect_transmits = openconfig_if_ipdup_addr_detect_transmits
        if openconfig_if_ipdhcp_client is not None:
            self.openconfig_if_ipdhcp_client = openconfig_if_ipdhcp_client

    @property
    def openconfig_if_ipenabled(self):
        """Gets the openconfig_if_ipenabled of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501


        :return: The openconfig_if_ipenabled of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_if_ipenabled

    @openconfig_if_ipenabled.setter
    def openconfig_if_ipenabled(self, openconfig_if_ipenabled):
        """Sets the openconfig_if_ipenabled of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.


        :param openconfig_if_ipenabled: The openconfig_if_ipenabled of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :type: bool
        """

        self._openconfig_if_ipenabled = openconfig_if_ipenabled

    @property
    def openconfig_if_ipmtu(self):
        """Gets the openconfig_if_ipmtu of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501


        :return: The openconfig_if_ipmtu of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_if_ipmtu

    @openconfig_if_ipmtu.setter
    def openconfig_if_ipmtu(self, openconfig_if_ipmtu):
        """Sets the openconfig_if_ipmtu of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.


        :param openconfig_if_ipmtu: The openconfig_if_ipmtu of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :type: int
        """

        self._openconfig_if_ipmtu = openconfig_if_ipmtu

    @property
    def openconfig_if_ipdup_addr_detect_transmits(self):
        """Gets the openconfig_if_ipdup_addr_detect_transmits of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501


        :return: The openconfig_if_ipdup_addr_detect_transmits of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_if_ipdup_addr_detect_transmits

    @openconfig_if_ipdup_addr_detect_transmits.setter
    def openconfig_if_ipdup_addr_detect_transmits(self, openconfig_if_ipdup_addr_detect_transmits):
        """Sets the openconfig_if_ipdup_addr_detect_transmits of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.


        :param openconfig_if_ipdup_addr_detect_transmits: The openconfig_if_ipdup_addr_detect_transmits of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :type: int
        """

        self._openconfig_if_ipdup_addr_detect_transmits = openconfig_if_ipdup_addr_detect_transmits

    @property
    def openconfig_if_ipdhcp_client(self):
        """Gets the openconfig_if_ipdhcp_client of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501


        :return: The openconfig_if_ipdhcp_client of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_if_ipdhcp_client

    @openconfig_if_ipdhcp_client.setter
    def openconfig_if_ipdhcp_client(self, openconfig_if_ipdhcp_client):
        """Sets the openconfig_if_ipdhcp_client of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.


        :param openconfig_if_ipdhcp_client: The openconfig_if_ipdhcp_client of this PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled.  # noqa: E501
        :type: bool
        """

        self._openconfig_if_ipdhcp_client = openconfig_if_ipdhcp_client

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
        if issubclass(PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled, dict):
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
        if not isinstance(other, PostOpenconfigIfIpInterfacesInterfaceSubinterfacesSubinterfaceIpv6ConfigEnabled):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

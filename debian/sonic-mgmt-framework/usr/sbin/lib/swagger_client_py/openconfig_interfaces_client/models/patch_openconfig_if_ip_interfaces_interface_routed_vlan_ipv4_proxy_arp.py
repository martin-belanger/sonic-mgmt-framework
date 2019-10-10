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

from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv4_proxy_arp import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_proxyarp import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp  # noqa: F401,E501


class PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp(object):
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
        'openconfig_if_ipproxy_arp': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp'
    }

    attribute_map = {
        'openconfig_if_ipproxy_arp': 'openconfig-if-ip:proxy-arp'
    }

    def __init__(self, openconfig_if_ipproxy_arp=None):  # noqa: E501
        """PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ipproxy_arp = None
        self.discriminator = None

        if openconfig_if_ipproxy_arp is not None:
            self.openconfig_if_ipproxy_arp = openconfig_if_ipproxy_arp

    @property
    def openconfig_if_ipproxy_arp(self):
        """Gets the openconfig_if_ipproxy_arp of this PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp.  # noqa: E501


        :return: The openconfig_if_ipproxy_arp of this PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp
        """
        return self._openconfig_if_ipproxy_arp

    @openconfig_if_ipproxy_arp.setter
    def openconfig_if_ipproxy_arp(self, openconfig_if_ipproxy_arp):
        """Sets the openconfig_if_ipproxy_arp of this PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp.


        :param openconfig_if_ipproxy_arp: The openconfig_if_ipproxy_arp of this PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp
        """

        self._openconfig_if_ipproxy_arp = openconfig_if_ipproxy_arp

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
        if issubclass(PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp, dict):
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
        if not isinstance(other, PatchOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

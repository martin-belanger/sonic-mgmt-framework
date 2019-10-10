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

from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv4_addresses import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv4_config import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Config  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv4_neighbors import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Neighbors  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv4_proxy_arp import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4ProxyArp  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv4_unnumbered import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Unnumbered  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_addresses import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Addresses  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_config import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Config  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_neighbors import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Neighbors  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_proxyarp import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_unnumbered import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered  # noqa: F401,E501


class PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses(object):
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
        'openconfig_if_ipaddresses': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Addresses',
        'openconfig_if_ipproxy_arp': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp',
        'openconfig_if_ipneighbors': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Neighbors',
        'openconfig_if_ipunnumbered': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered',
        'openconfig_if_ipconfig': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Config'
    }

    attribute_map = {
        'openconfig_if_ipaddresses': 'openconfig-if-ip:addresses',
        'openconfig_if_ipproxy_arp': 'openconfig-if-ip:proxy-arp',
        'openconfig_if_ipneighbors': 'openconfig-if-ip:neighbors',
        'openconfig_if_ipunnumbered': 'openconfig-if-ip:unnumbered',
        'openconfig_if_ipconfig': 'openconfig-if-ip:config'
    }

    def __init__(self, openconfig_if_ipaddresses=None, openconfig_if_ipproxy_arp=None, openconfig_if_ipneighbors=None, openconfig_if_ipunnumbered=None, openconfig_if_ipconfig=None):  # noqa: E501
        """PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ipaddresses = None
        self._openconfig_if_ipproxy_arp = None
        self._openconfig_if_ipneighbors = None
        self._openconfig_if_ipunnumbered = None
        self._openconfig_if_ipconfig = None
        self.discriminator = None

        if openconfig_if_ipaddresses is not None:
            self.openconfig_if_ipaddresses = openconfig_if_ipaddresses
        if openconfig_if_ipproxy_arp is not None:
            self.openconfig_if_ipproxy_arp = openconfig_if_ipproxy_arp
        if openconfig_if_ipneighbors is not None:
            self.openconfig_if_ipneighbors = openconfig_if_ipneighbors
        if openconfig_if_ipunnumbered is not None:
            self.openconfig_if_ipunnumbered = openconfig_if_ipunnumbered
        if openconfig_if_ipconfig is not None:
            self.openconfig_if_ipconfig = openconfig_if_ipconfig

    @property
    def openconfig_if_ipaddresses(self):
        """Gets the openconfig_if_ipaddresses of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501


        :return: The openconfig_if_ipaddresses of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Addresses
        """
        return self._openconfig_if_ipaddresses

    @openconfig_if_ipaddresses.setter
    def openconfig_if_ipaddresses(self, openconfig_if_ipaddresses):
        """Sets the openconfig_if_ipaddresses of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.


        :param openconfig_if_ipaddresses: The openconfig_if_ipaddresses of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Addresses
        """

        self._openconfig_if_ipaddresses = openconfig_if_ipaddresses

    @property
    def openconfig_if_ipproxy_arp(self):
        """Gets the openconfig_if_ipproxy_arp of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501


        :return: The openconfig_if_ipproxy_arp of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp
        """
        return self._openconfig_if_ipproxy_arp

    @openconfig_if_ipproxy_arp.setter
    def openconfig_if_ipproxy_arp(self, openconfig_if_ipproxy_arp):
        """Sets the openconfig_if_ipproxy_arp of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.


        :param openconfig_if_ipproxy_arp: The openconfig_if_ipproxy_arp of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Proxyarp
        """

        self._openconfig_if_ipproxy_arp = openconfig_if_ipproxy_arp

    @property
    def openconfig_if_ipneighbors(self):
        """Gets the openconfig_if_ipneighbors of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501


        :return: The openconfig_if_ipneighbors of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Neighbors
        """
        return self._openconfig_if_ipneighbors

    @openconfig_if_ipneighbors.setter
    def openconfig_if_ipneighbors(self, openconfig_if_ipneighbors):
        """Sets the openconfig_if_ipneighbors of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.


        :param openconfig_if_ipneighbors: The openconfig_if_ipneighbors of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Neighbors
        """

        self._openconfig_if_ipneighbors = openconfig_if_ipneighbors

    @property
    def openconfig_if_ipunnumbered(self):
        """Gets the openconfig_if_ipunnumbered of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501


        :return: The openconfig_if_ipunnumbered of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered
        """
        return self._openconfig_if_ipunnumbered

    @openconfig_if_ipunnumbered.setter
    def openconfig_if_ipunnumbered(self, openconfig_if_ipunnumbered):
        """Sets the openconfig_if_ipunnumbered of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.


        :param openconfig_if_ipunnumbered: The openconfig_if_ipunnumbered of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered
        """

        self._openconfig_if_ipunnumbered = openconfig_if_ipunnumbered

    @property
    def openconfig_if_ipconfig(self):
        """Gets the openconfig_if_ipconfig of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501


        :return: The openconfig_if_ipconfig of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Config
        """
        return self._openconfig_if_ipconfig

    @openconfig_if_ipconfig.setter
    def openconfig_if_ipconfig(self, openconfig_if_ipconfig):
        """Sets the openconfig_if_ipconfig of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.


        :param openconfig_if_ipconfig: The openconfig_if_ipconfig of this PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Config
        """

        self._openconfig_if_ipconfig = openconfig_if_ipconfig

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
        if issubclass(PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses, dict):
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
        if not isinstance(other, PostOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4Addresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

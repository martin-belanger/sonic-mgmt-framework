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

from openconfig_interfaces_client.models.openconfig_if_ip_interfaces_interface_routed_vlan_ipv6_unnumbered import OpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_unnumbered import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered  # noqa: F401,E501


class PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered(object):
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
        'openconfig_if_ipunnumbered': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered'
    }

    attribute_map = {
        'openconfig_if_ipunnumbered': 'openconfig-if-ip:unnumbered'
    }

    def __init__(self, openconfig_if_ipunnumbered=None):  # noqa: E501
        """PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ipunnumbered = None
        self.discriminator = None

        if openconfig_if_ipunnumbered is not None:
            self.openconfig_if_ipunnumbered = openconfig_if_ipunnumbered

    @property
    def openconfig_if_ipunnumbered(self):
        """Gets the openconfig_if_ipunnumbered of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered.  # noqa: E501


        :return: The openconfig_if_ipunnumbered of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered
        """
        return self._openconfig_if_ipunnumbered

    @openconfig_if_ipunnumbered.setter
    def openconfig_if_ipunnumbered(self, openconfig_if_ipunnumbered):
        """Sets the openconfig_if_ipunnumbered of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered.


        :param openconfig_if_ipunnumbered: The openconfig_if_ipunnumbered of this PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4Unnumbered
        """

        self._openconfig_if_ipunnumbered = openconfig_if_ipunnumbered

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
        if issubclass(PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered, dict):
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
        if not isinstance(other, PutOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv6Unnumbered):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

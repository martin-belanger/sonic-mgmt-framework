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

from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_neighbors_state import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4NeighborsState  # noqa: F401,E501


class GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState(object):
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
        'openconfig_if_ipstate': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4NeighborsState'
    }

    attribute_map = {
        'openconfig_if_ipstate': 'openconfig-if-ip:state'
    }

    def __init__(self, openconfig_if_ipstate=None):  # noqa: E501
        """GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState - a model defined in Swagger"""  # noqa: E501

        self._openconfig_if_ipstate = None
        self.discriminator = None

        if openconfig_if_ipstate is not None:
            self.openconfig_if_ipstate = openconfig_if_ipstate

    @property
    def openconfig_if_ipstate(self):
        """Gets the openconfig_if_ipstate of this GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState.  # noqa: E501


        :return: The openconfig_if_ipstate of this GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4NeighborsState
        """
        return self._openconfig_if_ipstate

    @openconfig_if_ipstate.setter
    def openconfig_if_ipstate(self, openconfig_if_ipstate):
        """Sets the openconfig_if_ipstate of this GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState.


        :param openconfig_if_ipstate: The openconfig_if_ipstate of this GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4NeighborsState
        """

        self._openconfig_if_ipstate = openconfig_if_ipstate

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
        if issubclass(GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState, dict):
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
        if not isinstance(other, GetOpenconfigIfIpInterfacesInterfaceRoutedVlanIpv4NeighborsNeighborState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

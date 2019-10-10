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

from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_openconfigvlanroutedvlan_config import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlanConfig  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4 import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv6 import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6  # noqa: F401,E501


class OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan(object):
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
        'config': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlanConfig',
        'ipv4': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4',
        'ipv6': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6'
    }

    attribute_map = {
        'config': 'config',
        'ipv4': 'ipv4',
        'ipv6': 'ipv6'
    }

    def __init__(self, config=None, ipv4=None, ipv6=None):  # noqa: E501
        """OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan - a model defined in Swagger"""  # noqa: E501

        self._config = None
        self._ipv4 = None
        self._ipv6 = None
        self.discriminator = None

        if config is not None:
            self.config = config
        if ipv4 is not None:
            self.ipv4 = ipv4
        if ipv6 is not None:
            self.ipv6 = ipv6

    @property
    def config(self):
        """Gets the config of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501


        :return: The config of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlanConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.


        :param config: The config of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlanConfig
        """

        self._config = config

    @property
    def ipv4(self):
        """Gets the ipv4 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501


        :return: The ipv4 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4
        """
        return self._ipv4

    @ipv4.setter
    def ipv4(self, ipv4):
        """Sets the ipv4 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.


        :param ipv4: The ipv4 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4
        """

        self._ipv4 = ipv4

    @property
    def ipv6(self):
        """Gets the ipv6 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501


        :return: The ipv6 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6
        """
        return self._ipv6

    @ipv6.setter
    def ipv6(self, ipv6):
        """Sets the ipv6 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.


        :param ipv6: The ipv6 of this OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6
        """

        self._ipv6 = ipv6

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
        if issubclass(OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan, dict):
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
        if not isinstance(other, OpenconfigVlanInterfacesInterfaceRoutedVlanOpenconfigvlanroutedvlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

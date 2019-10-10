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

from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4_state_counters import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4StateCounters  # noqa: F401,E501


class GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State(object):
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
        'enabled': 'bool',
        'mtu': 'int',
        'dhcp_client': 'bool',
        'counters': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4StateCounters'
    }

    attribute_map = {
        'enabled': 'enabled',
        'mtu': 'mtu',
        'dhcp_client': 'dhcp-client',
        'counters': 'counters'
    }

    def __init__(self, enabled=None, mtu=None, dhcp_client=None, counters=None):  # noqa: E501
        """GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._mtu = None
        self._dhcp_client = None
        self._counters = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if mtu is not None:
            self.mtu = mtu
        if dhcp_client is not None:
            self.dhcp_client = dhcp_client
        if counters is not None:
            self.counters = counters

    @property
    def enabled(self):
        """Gets the enabled of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501


        :return: The enabled of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.


        :param enabled: The enabled of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def mtu(self):
        """Gets the mtu of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501


        :return: The mtu of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.


        :param mtu: The mtu of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def dhcp_client(self):
        """Gets the dhcp_client of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501


        :return: The dhcp_client of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp_client

    @dhcp_client.setter
    def dhcp_client(self, dhcp_client):
        """Sets the dhcp_client of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.


        :param dhcp_client: The dhcp_client of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :type: bool
        """

        self._dhcp_client = dhcp_client

    @property
    def counters(self):
        """Gets the counters of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501


        :return: The counters of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4StateCounters
        """
        return self._counters

    @counters.setter
    def counters(self, counters):
        """Sets the counters of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.


        :param counters: The counters of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4StateCounters
        """

        self._counters = counters

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
        if issubclass(GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State, dict):
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
        if not isinstance(other, GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

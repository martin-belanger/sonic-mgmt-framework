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

from openconfig_interfaces_client.models.openconfig_vlan_interfaces_interface_aggregation_switched_vlan_config_access_vlan import OpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigAccessVlan  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_vlan_interfaces_interface_aggregation_switched_vlan_config_interface_mode import OpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_vlan_interfaces_interface_aggregation_switched_vlan_config_native_vlan import OpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigNativeVlan  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_vlan_interfaces_interface_aggregation_switched_vlan_config_trunk_vlans import OpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigTrunkVlans  # noqa: F401,E501


class PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode(object):
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
        'openconfig_vlaninterface_mode': 'str',
        'openconfig_vlannative_vlan': 'int',
        'openconfig_vlanaccess_vlan': 'int',
        'openconfig_vlantrunk_vlans': 'list[str]'
    }

    attribute_map = {
        'openconfig_vlaninterface_mode': 'openconfig-vlan:interface-mode',
        'openconfig_vlannative_vlan': 'openconfig-vlan:native-vlan',
        'openconfig_vlanaccess_vlan': 'openconfig-vlan:access-vlan',
        'openconfig_vlantrunk_vlans': 'openconfig-vlan:trunk-vlans'
    }

    def __init__(self, openconfig_vlaninterface_mode=None, openconfig_vlannative_vlan=None, openconfig_vlanaccess_vlan=None, openconfig_vlantrunk_vlans=None):  # noqa: E501
        """PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode - a model defined in Swagger"""  # noqa: E501

        self._openconfig_vlaninterface_mode = None
        self._openconfig_vlannative_vlan = None
        self._openconfig_vlanaccess_vlan = None
        self._openconfig_vlantrunk_vlans = None
        self.discriminator = None

        if openconfig_vlaninterface_mode is not None:
            self.openconfig_vlaninterface_mode = openconfig_vlaninterface_mode
        if openconfig_vlannative_vlan is not None:
            self.openconfig_vlannative_vlan = openconfig_vlannative_vlan
        if openconfig_vlanaccess_vlan is not None:
            self.openconfig_vlanaccess_vlan = openconfig_vlanaccess_vlan
        if openconfig_vlantrunk_vlans is not None:
            self.openconfig_vlantrunk_vlans = openconfig_vlantrunk_vlans

    @property
    def openconfig_vlaninterface_mode(self):
        """Gets the openconfig_vlaninterface_mode of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501


        :return: The openconfig_vlaninterface_mode of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :rtype: str
        """
        return self._openconfig_vlaninterface_mode

    @openconfig_vlaninterface_mode.setter
    def openconfig_vlaninterface_mode(self, openconfig_vlaninterface_mode):
        """Sets the openconfig_vlaninterface_mode of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.


        :param openconfig_vlaninterface_mode: The openconfig_vlaninterface_mode of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCESS", "TRUNK"]  # noqa: E501
        if openconfig_vlaninterface_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `openconfig_vlaninterface_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(openconfig_vlaninterface_mode, allowed_values)
            )

        self._openconfig_vlaninterface_mode = openconfig_vlaninterface_mode

    @property
    def openconfig_vlannative_vlan(self):
        """Gets the openconfig_vlannative_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501


        :return: The openconfig_vlannative_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_vlannative_vlan

    @openconfig_vlannative_vlan.setter
    def openconfig_vlannative_vlan(self, openconfig_vlannative_vlan):
        """Sets the openconfig_vlannative_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.


        :param openconfig_vlannative_vlan: The openconfig_vlannative_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :type: int
        """

        self._openconfig_vlannative_vlan = openconfig_vlannative_vlan

    @property
    def openconfig_vlanaccess_vlan(self):
        """Gets the openconfig_vlanaccess_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501


        :return: The openconfig_vlanaccess_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_vlanaccess_vlan

    @openconfig_vlanaccess_vlan.setter
    def openconfig_vlanaccess_vlan(self, openconfig_vlanaccess_vlan):
        """Sets the openconfig_vlanaccess_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.


        :param openconfig_vlanaccess_vlan: The openconfig_vlanaccess_vlan of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :type: int
        """

        self._openconfig_vlanaccess_vlan = openconfig_vlanaccess_vlan

    @property
    def openconfig_vlantrunk_vlans(self):
        """Gets the openconfig_vlantrunk_vlans of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501


        :return: The openconfig_vlantrunk_vlans of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :rtype: list[str]
        """
        return self._openconfig_vlantrunk_vlans

    @openconfig_vlantrunk_vlans.setter
    def openconfig_vlantrunk_vlans(self, openconfig_vlantrunk_vlans):
        """Sets the openconfig_vlantrunk_vlans of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.


        :param openconfig_vlantrunk_vlans: The openconfig_vlantrunk_vlans of this PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode.  # noqa: E501
        :type: list[str]
        """

        self._openconfig_vlantrunk_vlans = openconfig_vlantrunk_vlans

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
        if issubclass(PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode, dict):
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
        if not isinstance(other, PostOpenconfigVlanInterfacesInterfaceAggregationSwitchedVlanConfigInterfaceMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_holdtime import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesHoldtime  # noqa: F401,E501
from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_openconfigifaggregateaggregation import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifaggregateaggregation  # noqa: F401,E501
from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_openconfigifethernetethernet import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifethernetethernet  # noqa: F401,E501
from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_openconfigvlanroutedvlan import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlan  # noqa: F401,E501
from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_state import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesState  # noqa: F401,E501
from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces import GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfaces  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_config import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig  # noqa: F401,E501


class GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface(object):
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
        'name': 'str',
        'config': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig',
        'state': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesState',
        'hold_time': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesHoldtime',
        'subinterfaces': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfaces',
        'openconfig_if_ethernetethernet': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifethernetethernet',
        'openconfig_if_aggregateaggregation': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifaggregateaggregation',
        'openconfig_vlanrouted_vlan': 'GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlan'
    }

    attribute_map = {
        'name': 'name',
        'config': 'config',
        'state': 'state',
        'hold_time': 'hold-time',
        'subinterfaces': 'subinterfaces',
        'openconfig_if_ethernetethernet': 'openconfig-if-ethernet:ethernet',
        'openconfig_if_aggregateaggregation': 'openconfig-if-aggregate:aggregation',
        'openconfig_vlanrouted_vlan': 'openconfig-vlan:routed-vlan'
    }

    def __init__(self, name=None, config=None, state=None, hold_time=None, subinterfaces=None, openconfig_if_ethernetethernet=None, openconfig_if_aggregateaggregation=None, openconfig_vlanrouted_vlan=None):  # noqa: E501
        """GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._config = None
        self._state = None
        self._hold_time = None
        self._subinterfaces = None
        self._openconfig_if_ethernetethernet = None
        self._openconfig_if_aggregateaggregation = None
        self._openconfig_vlanrouted_vlan = None
        self.discriminator = None

        self.name = name
        if config is not None:
            self.config = config
        if state is not None:
            self.state = state
        if hold_time is not None:
            self.hold_time = hold_time
        if subinterfaces is not None:
            self.subinterfaces = subinterfaces
        if openconfig_if_ethernetethernet is not None:
            self.openconfig_if_ethernetethernet = openconfig_if_ethernetethernet
        if openconfig_if_aggregateaggregation is not None:
            self.openconfig_if_aggregateaggregation = openconfig_if_aggregateaggregation
        if openconfig_vlanrouted_vlan is not None:
            self.openconfig_vlanrouted_vlan = openconfig_vlanrouted_vlan

    @property
    def name(self):
        """Gets the name of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The name of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param name: The name of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def config(self):
        """Gets the config of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The config of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param config: The config of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig
        """

        self._config = config

    @property
    def state(self):
        """Gets the state of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The state of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param state: The state of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesState
        """

        self._state = state

    @property
    def hold_time(self):
        """Gets the hold_time of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The hold_time of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesHoldtime
        """
        return self._hold_time

    @hold_time.setter
    def hold_time(self, hold_time):
        """Sets the hold_time of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param hold_time: The hold_time of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesHoldtime
        """

        self._hold_time = hold_time

    @property
    def subinterfaces(self):
        """Gets the subinterfaces of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The subinterfaces of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfaces
        """
        return self._subinterfaces

    @subinterfaces.setter
    def subinterfaces(self, subinterfaces):
        """Sets the subinterfaces of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param subinterfaces: The subinterfaces of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfaces
        """

        self._subinterfaces = subinterfaces

    @property
    def openconfig_if_ethernetethernet(self):
        """Gets the openconfig_if_ethernetethernet of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The openconfig_if_ethernetethernet of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifethernetethernet
        """
        return self._openconfig_if_ethernetethernet

    @openconfig_if_ethernetethernet.setter
    def openconfig_if_ethernetethernet(self, openconfig_if_ethernetethernet):
        """Sets the openconfig_if_ethernetethernet of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param openconfig_if_ethernetethernet: The openconfig_if_ethernetethernet of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifethernetethernet
        """

        self._openconfig_if_ethernetethernet = openconfig_if_ethernetethernet

    @property
    def openconfig_if_aggregateaggregation(self):
        """Gets the openconfig_if_aggregateaggregation of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The openconfig_if_aggregateaggregation of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifaggregateaggregation
        """
        return self._openconfig_if_aggregateaggregation

    @openconfig_if_aggregateaggregation.setter
    def openconfig_if_aggregateaggregation(self, openconfig_if_aggregateaggregation):
        """Sets the openconfig_if_aggregateaggregation of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param openconfig_if_aggregateaggregation: The openconfig_if_aggregateaggregation of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigifaggregateaggregation
        """

        self._openconfig_if_aggregateaggregation = openconfig_if_aggregateaggregation

    @property
    def openconfig_vlanrouted_vlan(self):
        """Gets the openconfig_vlanrouted_vlan of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501


        :return: The openconfig_vlanrouted_vlan of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :rtype: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlan
        """
        return self._openconfig_vlanrouted_vlan

    @openconfig_vlanrouted_vlan.setter
    def openconfig_vlanrouted_vlan(self, openconfig_vlanrouted_vlan):
        """Sets the openconfig_vlanrouted_vlan of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.


        :param openconfig_vlanrouted_vlan: The openconfig_vlanrouted_vlan of this GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface.  # noqa: E501
        :type: GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesOpenconfigvlanroutedvlan
        """

        self._openconfig_vlanrouted_vlan = openconfig_vlanrouted_vlan

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
        if issubclass(GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface, dict):
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
        if not isinstance(other, GetOpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

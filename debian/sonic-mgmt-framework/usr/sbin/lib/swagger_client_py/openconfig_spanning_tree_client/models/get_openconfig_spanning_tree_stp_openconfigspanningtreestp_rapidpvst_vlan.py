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

from openconfig_spanning_tree_client.models.get_openconfig_spanning_tree_stp_openconfigspanningtreestp_rapidpvst_state import GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstState  # noqa: F401,E501
from openconfig_spanning_tree_client.models.get_openconfig_spanning_tree_stp_openconfigspanningtreestp_rstp_interfaces import GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_openconfigspanningtreestp_rapidpvst_config import OpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstConfig  # noqa: F401,E501


class GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan(object):
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
        'vlan_id': 'int',
        'config': 'OpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstConfig',
        'state': 'GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstState',
        'interfaces': 'GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces'
    }

    attribute_map = {
        'vlan_id': 'vlan-id',
        'config': 'config',
        'state': 'state',
        'interfaces': 'interfaces'
    }

    def __init__(self, vlan_id=None, config=None, state=None, interfaces=None):  # noqa: E501
        """GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan - a model defined in Swagger"""  # noqa: E501

        self._vlan_id = None
        self._config = None
        self._state = None
        self._interfaces = None
        self.discriminator = None

        self.vlan_id = vlan_id
        if config is not None:
            self.config = config
        if state is not None:
            self.state = state
        if interfaces is not None:
            self.interfaces = interfaces

    @property
    def vlan_id(self):
        """Gets the vlan_id of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501


        :return: The vlan_id of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.


        :param vlan_id: The vlan_id of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :type: int
        """
        if vlan_id is None:
            raise ValueError("Invalid value for `vlan_id`, must not be `None`")  # noqa: E501

        self._vlan_id = vlan_id

    @property
    def config(self):
        """Gets the config of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501


        :return: The config of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :rtype: OpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.


        :param config: The config of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :type: OpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstConfig
        """

        self._config = config

    @property
    def state(self):
        """Gets the state of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501


        :return: The state of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :rtype: GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.


        :param state: The state of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :type: GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstState
        """

        self._state = state

    @property
    def interfaces(self):
        """Gets the interfaces of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501


        :return: The interfaces of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :rtype: GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.


        :param interfaces: The interfaces of this GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan.  # noqa: E501
        :type: GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces
        """

        self._interfaces = interfaces

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
        if issubclass(GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan, dict):
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
        if not isinstance(other, GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpRapidpvstVlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

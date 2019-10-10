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

from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_config import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesConfig  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv4 import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigifipipv6 import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_subinterfaces_openconfigvlanvlan import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigvlanvlan  # noqa: F401,E501


class OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface(object):
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
        'index': 'int',
        'config': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesConfig',
        'openconfig_vlanvlan': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigvlanvlan',
        'openconfig_if_ipipv4': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4',
        'openconfig_if_ipipv6': 'OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6'
    }

    attribute_map = {
        'index': 'index',
        'config': 'config',
        'openconfig_vlanvlan': 'openconfig-vlan:vlan',
        'openconfig_if_ipipv4': 'openconfig-if-ip:ipv4',
        'openconfig_if_ipipv6': 'openconfig-if-ip:ipv6'
    }

    def __init__(self, index=None, config=None, openconfig_vlanvlan=None, openconfig_if_ipipv4=None, openconfig_if_ipipv6=None):  # noqa: E501
        """OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface - a model defined in Swagger"""  # noqa: E501

        self._index = None
        self._config = None
        self._openconfig_vlanvlan = None
        self._openconfig_if_ipipv4 = None
        self._openconfig_if_ipipv6 = None
        self.discriminator = None

        self.index = index
        if config is not None:
            self.config = config
        if openconfig_vlanvlan is not None:
            self.openconfig_vlanvlan = openconfig_vlanvlan
        if openconfig_if_ipipv4 is not None:
            self.openconfig_if_ipipv4 = openconfig_if_ipipv4
        if openconfig_if_ipipv6 is not None:
            self.openconfig_if_ipipv6 = openconfig_if_ipipv6

    @property
    def index(self):
        """Gets the index of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501


        :return: The index of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.


        :param index: The index of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def config(self):
        """Gets the config of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501


        :return: The config of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.


        :param config: The config of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesConfig
        """

        self._config = config

    @property
    def openconfig_vlanvlan(self):
        """Gets the openconfig_vlanvlan of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501


        :return: The openconfig_vlanvlan of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigvlanvlan
        """
        return self._openconfig_vlanvlan

    @openconfig_vlanvlan.setter
    def openconfig_vlanvlan(self, openconfig_vlanvlan):
        """Sets the openconfig_vlanvlan of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.


        :param openconfig_vlanvlan: The openconfig_vlanvlan of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigvlanvlan
        """

        self._openconfig_vlanvlan = openconfig_vlanvlan

    @property
    def openconfig_if_ipipv4(self):
        """Gets the openconfig_if_ipipv4 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501


        :return: The openconfig_if_ipipv4 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4
        """
        return self._openconfig_if_ipipv4

    @openconfig_if_ipipv4.setter
    def openconfig_if_ipipv4(self, openconfig_if_ipipv4):
        """Sets the openconfig_if_ipipv4 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.


        :param openconfig_if_ipipv4: The openconfig_if_ipipv4 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv4
        """

        self._openconfig_if_ipipv4 = openconfig_if_ipipv4

    @property
    def openconfig_if_ipipv6(self):
        """Gets the openconfig_if_ipipv6 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501


        :return: The openconfig_if_ipipv6 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :rtype: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6
        """
        return self._openconfig_if_ipipv6

    @openconfig_if_ipipv6.setter
    def openconfig_if_ipipv6(self, openconfig_if_ipipv6):
        """Sets the openconfig_if_ipipv6 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.


        :param openconfig_if_ipipv6: The openconfig_if_ipipv6 of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface.  # noqa: E501
        :type: OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesOpenconfigifipipv6
        """

        self._openconfig_if_ipipv6 = openconfig_if_ipipv6

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
        if issubclass(OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface, dict):
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
        if not isinstance(other, OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesSubinterfacesSubinterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

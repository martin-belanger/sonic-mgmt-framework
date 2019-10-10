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


class OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig(object):
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
        'type': 'str',
        'mtu': 'int',
        'loopback_mode': 'bool',
        'description': 'str',
        'enabled': 'bool',
        'openconfig_vlantpid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'mtu': 'mtu',
        'loopback_mode': 'loopback-mode',
        'description': 'description',
        'enabled': 'enabled',
        'openconfig_vlantpid': 'openconfig-vlan:tpid'
    }

    def __init__(self, name=None, type=None, mtu=None, loopback_mode=None, description=None, enabled=None, openconfig_vlantpid=None):  # noqa: E501
        """OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._mtu = None
        self._loopback_mode = None
        self._description = None
        self._enabled = None
        self._openconfig_vlantpid = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if mtu is not None:
            self.mtu = mtu
        if loopback_mode is not None:
            self.loopback_mode = loopback_mode
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if openconfig_vlantpid is not None:
            self.openconfig_vlantpid = openconfig_vlantpid

    @property
    def name(self):
        """Gets the name of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501


        :return: The name of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.


        :param name: The name of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501


        :return: The type of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.


        :param type: The type of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def mtu(self):
        """Gets the mtu of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501


        :return: The mtu of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :rtype: int
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.


        :param mtu: The mtu of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :type: int
        """

        self._mtu = mtu

    @property
    def loopback_mode(self):
        """Gets the loopback_mode of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501


        :return: The loopback_mode of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :rtype: bool
        """
        return self._loopback_mode

    @loopback_mode.setter
    def loopback_mode(self, loopback_mode):
        """Sets the loopback_mode of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.


        :param loopback_mode: The loopback_mode of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :type: bool
        """

        self._loopback_mode = loopback_mode

    @property
    def description(self):
        """Gets the description of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501


        :return: The description of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.


        :param description: The description of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501


        :return: The enabled of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.


        :param enabled: The enabled of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def openconfig_vlantpid(self):
        """Gets the openconfig_vlantpid of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501


        :return: The openconfig_vlantpid of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :rtype: str
        """
        return self._openconfig_vlantpid

    @openconfig_vlantpid.setter
    def openconfig_vlantpid(self, openconfig_vlantpid):
        """Sets the openconfig_vlantpid of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.


        :param openconfig_vlantpid: The openconfig_vlantpid of this OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig.  # noqa: E501
        :type: str
        """

        self._openconfig_vlantpid = openconfig_vlantpid

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
        if issubclass(OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig, dict):
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
        if not isinstance(other, OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

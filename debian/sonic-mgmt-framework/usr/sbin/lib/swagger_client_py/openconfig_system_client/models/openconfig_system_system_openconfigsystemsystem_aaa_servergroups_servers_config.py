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


class OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig(object):
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
        'address': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'timeout': 'timeout'
    }

    def __init__(self, name=None, address=None, timeout=None):  # noqa: E501
        """OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._address = None
        self._timeout = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if timeout is not None:
            self.timeout = timeout

    @property
    def name(self):
        """Gets the name of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501


        :return: The name of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.


        :param name: The name of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501


        :return: The address of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.


        :param address: The address of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def timeout(self):
        """Gets the timeout of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501


        :return: The timeout of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.


        :param timeout: The timeout of this OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if issubclass(OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig, dict):
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
        if not isinstance(other, OpenconfigSystemSystemOpenconfigsystemsystemAaaServergroupsServersConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

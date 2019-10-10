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

from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_aaa_authentication_users_config import OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersConfig  # noqa: F401,E501


class GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser(object):
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
        'username': 'str',
        'config': 'OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersConfig',
        'state': 'OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersConfig'
    }

    attribute_map = {
        'username': 'username',
        'config': 'config',
        'state': 'state'
    }

    def __init__(self, username=None, config=None, state=None):  # noqa: E501
        """GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._config = None
        self._state = None
        self.discriminator = None

        self.username = username
        if config is not None:
            self.config = config
        if state is not None:
            self.state = state

    @property
    def username(self):
        """Gets the username of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501


        :return: The username of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.


        :param username: The username of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def config(self):
        """Gets the config of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501


        :return: The config of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.


        :param config: The config of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersConfig
        """

        self._config = config

    @property
    def state(self):
        """Gets the state of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501


        :return: The state of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersConfig
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.


        :param state: The state of this GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersConfig
        """

        self._state = state

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
        if issubclass(GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser, dict):
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
        if not isinstance(other, GetOpenconfigSystemSystemOpenconfigsystemsystemAaaAuthenticationUsersUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

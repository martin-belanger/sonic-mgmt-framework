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

from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_config import OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig  # noqa: F401,E501


class GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent(object):
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
        'config': 'OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig',
        'state': 'OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig'
    }

    attribute_map = {
        'name': 'name',
        'config': 'config',
        'state': 'state'
    }

    def __init__(self, name=None, config=None, state=None):  # noqa: E501
        """GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._config = None
        self._state = None
        self.discriminator = None

        self.name = name
        if config is not None:
            self.config = config
        if state is not None:
            self.state = state

    @property
    def name(self):
        """Gets the name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501


        :return: The name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.


        :param name: The name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def config(self):
        """Gets the config of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501


        :return: The config of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501
        :rtype: OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.


        :param config: The config of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501
        :type: OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig
        """

        self._config = config

    @property
    def state(self):
        """Gets the state of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501


        :return: The state of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501
        :rtype: OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.


        :param state: The state of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent.  # noqa: E501
        :type: OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig
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
        if issubclass(GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent, dict):
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
        if not isinstance(other, GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

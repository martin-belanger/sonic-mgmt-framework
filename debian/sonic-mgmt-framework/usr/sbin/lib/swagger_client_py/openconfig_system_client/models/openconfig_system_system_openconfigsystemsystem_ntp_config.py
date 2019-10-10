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


class OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig(object):
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
        'ntp_source_address': 'str',
        'enable_ntp_auth': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'ntp_source_address': 'ntp-source-address',
        'enable_ntp_auth': 'enable-ntp-auth'
    }

    def __init__(self, enabled=None, ntp_source_address=None, enable_ntp_auth=None):  # noqa: E501
        """OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig - a model defined in Swagger"""  # noqa: E501

        self._enabled = None
        self._ntp_source_address = None
        self._enable_ntp_auth = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if ntp_source_address is not None:
            self.ntp_source_address = ntp_source_address
        if enable_ntp_auth is not None:
            self.enable_ntp_auth = enable_ntp_auth

    @property
    def enabled(self):
        """Gets the enabled of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501


        :return: The enabled of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.


        :param enabled: The enabled of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def ntp_source_address(self):
        """Gets the ntp_source_address of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501


        :return: The ntp_source_address of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501
        :rtype: str
        """
        return self._ntp_source_address

    @ntp_source_address.setter
    def ntp_source_address(self, ntp_source_address):
        """Sets the ntp_source_address of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.


        :param ntp_source_address: The ntp_source_address of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501
        :type: str
        """

        self._ntp_source_address = ntp_source_address

    @property
    def enable_ntp_auth(self):
        """Gets the enable_ntp_auth of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501


        :return: The enable_ntp_auth of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ntp_auth

    @enable_ntp_auth.setter
    def enable_ntp_auth(self, enable_ntp_auth):
        """Sets the enable_ntp_auth of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.


        :param enable_ntp_auth: The enable_ntp_auth of this OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig.  # noqa: E501
        :type: bool
        """

        self._enable_ntp_auth = enable_ntp_auth

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
        if issubclass(OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig, dict):
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
        if not isinstance(other, OpenconfigSystemSystemOpenconfigsystemsystemNtpConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

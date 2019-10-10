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

from openconfig_system_client.models.openconfig_system_system_ntp_servers_server_config_iburst import OpenconfigSystemSystemNtpServersServerConfigIburst  # noqa: F401,E501


class PatchOpenconfigSystemSystemNtpServersServerConfigIburst(object):
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
        'openconfig_systemiburst': 'bool'
    }

    attribute_map = {
        'openconfig_systemiburst': 'openconfig-system:iburst'
    }

    def __init__(self, openconfig_systemiburst=None):  # noqa: E501
        """PatchOpenconfigSystemSystemNtpServersServerConfigIburst - a model defined in Swagger"""  # noqa: E501

        self._openconfig_systemiburst = None
        self.discriminator = None

        if openconfig_systemiburst is not None:
            self.openconfig_systemiburst = openconfig_systemiburst

    @property
    def openconfig_systemiburst(self):
        """Gets the openconfig_systemiburst of this PatchOpenconfigSystemSystemNtpServersServerConfigIburst.  # noqa: E501


        :return: The openconfig_systemiburst of this PatchOpenconfigSystemSystemNtpServersServerConfigIburst.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_systemiburst

    @openconfig_systemiburst.setter
    def openconfig_systemiburst(self, openconfig_systemiburst):
        """Sets the openconfig_systemiburst of this PatchOpenconfigSystemSystemNtpServersServerConfigIburst.


        :param openconfig_systemiburst: The openconfig_systemiburst of this PatchOpenconfigSystemSystemNtpServersServerConfigIburst.  # noqa: E501
        :type: bool
        """

        self._openconfig_systemiburst = openconfig_systemiburst

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
        if issubclass(PatchOpenconfigSystemSystemNtpServersServerConfigIburst, dict):
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
        if not isinstance(other, PatchOpenconfigSystemSystemNtpServersServerConfigIburst):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

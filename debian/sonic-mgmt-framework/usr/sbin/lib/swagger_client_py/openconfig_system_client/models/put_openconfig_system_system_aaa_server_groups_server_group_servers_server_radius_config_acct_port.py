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

from openconfig_system_client.models.openconfig_system_system_aaa_server_groups_server_group_servers_server_radius_config_acct_port import OpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort  # noqa: F401,E501


class PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort(object):
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
        'openconfig_systemacct_port': 'int'
    }

    attribute_map = {
        'openconfig_systemacct_port': 'openconfig-system:acct-port'
    }

    def __init__(self, openconfig_systemacct_port=None):  # noqa: E501
        """PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort - a model defined in Swagger"""  # noqa: E501

        self._openconfig_systemacct_port = None
        self.discriminator = None

        if openconfig_systemacct_port is not None:
            self.openconfig_systemacct_port = openconfig_systemacct_port

    @property
    def openconfig_systemacct_port(self):
        """Gets the openconfig_systemacct_port of this PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort.  # noqa: E501


        :return: The openconfig_systemacct_port of this PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_systemacct_port

    @openconfig_systemacct_port.setter
    def openconfig_systemacct_port(self, openconfig_systemacct_port):
        """Sets the openconfig_systemacct_port of this PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort.


        :param openconfig_systemacct_port: The openconfig_systemacct_port of this PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort.  # noqa: E501
        :type: int
        """

        self._openconfig_systemacct_port = openconfig_systemacct_port

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
        if issubclass(PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort, dict):
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
        if not isinstance(other, PutOpenconfigSystemSystemAaaServerGroupsServerGroupServersServerRadiusConfigAcctPort):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

from openconfig_lldp_client.models.get_openconfig_lldp_lldp_openconfiglldplldp import GetOpenconfigLldpLldpOpenconfiglldplldp  # noqa: F401,E501


class GetOpenconfigLldpLldp(object):
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
        'openconfig_lldplldp': 'GetOpenconfigLldpLldpOpenconfiglldplldp'
    }

    attribute_map = {
        'openconfig_lldplldp': 'openconfig-lldp:lldp'
    }

    def __init__(self, openconfig_lldplldp=None):  # noqa: E501
        """GetOpenconfigLldpLldp - a model defined in Swagger"""  # noqa: E501

        self._openconfig_lldplldp = None
        self.discriminator = None

        if openconfig_lldplldp is not None:
            self.openconfig_lldplldp = openconfig_lldplldp

    @property
    def openconfig_lldplldp(self):
        """Gets the openconfig_lldplldp of this GetOpenconfigLldpLldp.  # noqa: E501


        :return: The openconfig_lldplldp of this GetOpenconfigLldpLldp.  # noqa: E501
        :rtype: GetOpenconfigLldpLldpOpenconfiglldplldp
        """
        return self._openconfig_lldplldp

    @openconfig_lldplldp.setter
    def openconfig_lldplldp(self, openconfig_lldplldp):
        """Sets the openconfig_lldplldp of this GetOpenconfigLldpLldp.


        :param openconfig_lldplldp: The openconfig_lldplldp of this GetOpenconfigLldpLldp.  # noqa: E501
        :type: GetOpenconfigLldpLldpOpenconfiglldplldp
        """

        self._openconfig_lldplldp = openconfig_lldplldp

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
        if issubclass(GetOpenconfigLldpLldp, dict):
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
        if not isinstance(other, GetOpenconfigLldpLldp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

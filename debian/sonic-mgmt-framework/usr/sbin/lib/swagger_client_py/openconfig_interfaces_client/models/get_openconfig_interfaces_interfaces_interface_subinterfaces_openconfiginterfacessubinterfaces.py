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

from openconfig_interfaces_client.models.get_openconfig_interfaces_interfaces_interface_subinterfaces_openconfiginterfacessubinterfaces_subinterface import GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfacesSubinterface  # noqa: F401,E501


class GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces(object):
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
        'subinterface': 'list[GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfacesSubinterface]'
    }

    attribute_map = {
        'subinterface': 'subinterface'
    }

    def __init__(self, subinterface=None):  # noqa: E501
        """GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces - a model defined in Swagger"""  # noqa: E501

        self._subinterface = None
        self.discriminator = None

        if subinterface is not None:
            self.subinterface = subinterface

    @property
    def subinterface(self):
        """Gets the subinterface of this GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces.  # noqa: E501


        :return: The subinterface of this GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces.  # noqa: E501
        :rtype: list[GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfacesSubinterface]
        """
        return self._subinterface

    @subinterface.setter
    def subinterface(self, subinterface):
        """Sets the subinterface of this GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces.


        :param subinterface: The subinterface of this GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces.  # noqa: E501
        :type: list[GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfacesSubinterface]
        """

        self._subinterface = subinterface

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
        if issubclass(GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces, dict):
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
        if not isinstance(other, GetOpenconfigInterfacesInterfacesInterfaceSubinterfacesOpenconfiginterfacessubinterfaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

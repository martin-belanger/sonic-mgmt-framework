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

from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_interface import OpenconfigInterfacesInterfacesInterface  # noqa: F401,E501
from openconfig_interfaces_client.models.openconfig_interfaces_interfaces_openconfiginterfacesinterfaces_interface import OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface  # noqa: F401,E501


class PatchListOpenconfigInterfacesInterfacesInterface(object):
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
        'openconfig_interfacesinterface': 'list[OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface]'
    }

    attribute_map = {
        'openconfig_interfacesinterface': 'openconfig-interfaces:interface'
    }

    def __init__(self, openconfig_interfacesinterface=None):  # noqa: E501
        """PatchListOpenconfigInterfacesInterfacesInterface - a model defined in Swagger"""  # noqa: E501

        self._openconfig_interfacesinterface = None
        self.discriminator = None

        if openconfig_interfacesinterface is not None:
            self.openconfig_interfacesinterface = openconfig_interfacesinterface

    @property
    def openconfig_interfacesinterface(self):
        """Gets the openconfig_interfacesinterface of this PatchListOpenconfigInterfacesInterfacesInterface.  # noqa: E501


        :return: The openconfig_interfacesinterface of this PatchListOpenconfigInterfacesInterfacesInterface.  # noqa: E501
        :rtype: list[OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface]
        """
        return self._openconfig_interfacesinterface

    @openconfig_interfacesinterface.setter
    def openconfig_interfacesinterface(self, openconfig_interfacesinterface):
        """Sets the openconfig_interfacesinterface of this PatchListOpenconfigInterfacesInterfacesInterface.


        :param openconfig_interfacesinterface: The openconfig_interfacesinterface of this PatchListOpenconfigInterfacesInterfacesInterface.  # noqa: E501
        :type: list[OpenconfigInterfacesInterfacesOpenconfiginterfacesinterfacesInterface]
        """

        self._openconfig_interfacesinterface = openconfig_interfacesinterface

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
        if issubclass(PatchListOpenconfigInterfacesInterfacesInterface, dict):
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
        if not isinstance(other, PatchListOpenconfigInterfacesInterfacesInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

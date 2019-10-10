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

from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_openconfigspanningtreestp_rstp_interfaces_interface import OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfacesInterface  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_rstp_interfaces_interface import OpenconfigSpanningTreeStpRstpInterfacesInterface  # noqa: F401,E501


class PostListOpenconfigSpanningTreeStpRstpInterfacesInterface(object):
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
        'openconfig_spanning_treeinterface': 'list[OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfacesInterface]'
    }

    attribute_map = {
        'openconfig_spanning_treeinterface': 'openconfig-spanning-tree:interface'
    }

    def __init__(self, openconfig_spanning_treeinterface=None):  # noqa: E501
        """PostListOpenconfigSpanningTreeStpRstpInterfacesInterface - a model defined in Swagger"""  # noqa: E501

        self._openconfig_spanning_treeinterface = None
        self.discriminator = None

        if openconfig_spanning_treeinterface is not None:
            self.openconfig_spanning_treeinterface = openconfig_spanning_treeinterface

    @property
    def openconfig_spanning_treeinterface(self):
        """Gets the openconfig_spanning_treeinterface of this PostListOpenconfigSpanningTreeStpRstpInterfacesInterface.  # noqa: E501


        :return: The openconfig_spanning_treeinterface of this PostListOpenconfigSpanningTreeStpRstpInterfacesInterface.  # noqa: E501
        :rtype: list[OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfacesInterface]
        """
        return self._openconfig_spanning_treeinterface

    @openconfig_spanning_treeinterface.setter
    def openconfig_spanning_treeinterface(self, openconfig_spanning_treeinterface):
        """Sets the openconfig_spanning_treeinterface of this PostListOpenconfigSpanningTreeStpRstpInterfacesInterface.


        :param openconfig_spanning_treeinterface: The openconfig_spanning_treeinterface of this PostListOpenconfigSpanningTreeStpRstpInterfacesInterface.  # noqa: E501
        :type: list[OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfacesInterface]
        """

        self._openconfig_spanning_treeinterface = openconfig_spanning_treeinterface

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
        if issubclass(PostListOpenconfigSpanningTreeStpRstpInterfacesInterface, dict):
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
        if not isinstance(other, PostListOpenconfigSpanningTreeStpRstpInterfacesInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

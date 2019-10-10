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

from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_openconfigspanningtreestp_rstp_interfaces import OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces  # noqa: F401,E501


class OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces(object):
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
        'openconfig_spanning_treeinterfaces': 'OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces'
    }

    attribute_map = {
        'openconfig_spanning_treeinterfaces': 'openconfig-spanning-tree:interfaces'
    }

    def __init__(self, openconfig_spanning_treeinterfaces=None):  # noqa: E501
        """OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces - a model defined in Swagger"""  # noqa: E501

        self._openconfig_spanning_treeinterfaces = None
        self.discriminator = None

        if openconfig_spanning_treeinterfaces is not None:
            self.openconfig_spanning_treeinterfaces = openconfig_spanning_treeinterfaces

    @property
    def openconfig_spanning_treeinterfaces(self):
        """Gets the openconfig_spanning_treeinterfaces of this OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces.  # noqa: E501


        :return: The openconfig_spanning_treeinterfaces of this OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces.  # noqa: E501
        :rtype: OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces
        """
        return self._openconfig_spanning_treeinterfaces

    @openconfig_spanning_treeinterfaces.setter
    def openconfig_spanning_treeinterfaces(self, openconfig_spanning_treeinterfaces):
        """Sets the openconfig_spanning_treeinterfaces of this OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces.


        :param openconfig_spanning_treeinterfaces: The openconfig_spanning_treeinterfaces of this OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces.  # noqa: E501
        :type: OpenconfigSpanningTreeStpOpenconfigspanningtreestpRstpInterfaces
        """

        self._openconfig_spanning_treeinterfaces = openconfig_spanning_treeinterfaces

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
        if issubclass(OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces, dict):
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
        if not isinstance(other, OpenconfigSpanningTreeStpMstpMstInstancesMstInstanceInterfaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

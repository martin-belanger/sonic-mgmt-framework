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

from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_openconfigspanningtreestp_mstp import OpenconfigSpanningTreeStpOpenconfigspanningtreestpMstp  # noqa: F401,E501


class OpenconfigSpanningTreeStpMstp(object):
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
        'openconfig_spanning_treemstp': 'OpenconfigSpanningTreeStpOpenconfigspanningtreestpMstp'
    }

    attribute_map = {
        'openconfig_spanning_treemstp': 'openconfig-spanning-tree:mstp'
    }

    def __init__(self, openconfig_spanning_treemstp=None):  # noqa: E501
        """OpenconfigSpanningTreeStpMstp - a model defined in Swagger"""  # noqa: E501

        self._openconfig_spanning_treemstp = None
        self.discriminator = None

        if openconfig_spanning_treemstp is not None:
            self.openconfig_spanning_treemstp = openconfig_spanning_treemstp

    @property
    def openconfig_spanning_treemstp(self):
        """Gets the openconfig_spanning_treemstp of this OpenconfigSpanningTreeStpMstp.  # noqa: E501


        :return: The openconfig_spanning_treemstp of this OpenconfigSpanningTreeStpMstp.  # noqa: E501
        :rtype: OpenconfigSpanningTreeStpOpenconfigspanningtreestpMstp
        """
        return self._openconfig_spanning_treemstp

    @openconfig_spanning_treemstp.setter
    def openconfig_spanning_treemstp(self, openconfig_spanning_treemstp):
        """Sets the openconfig_spanning_treemstp of this OpenconfigSpanningTreeStpMstp.


        :param openconfig_spanning_treemstp: The openconfig_spanning_treemstp of this OpenconfigSpanningTreeStpMstp.  # noqa: E501
        :type: OpenconfigSpanningTreeStpOpenconfigspanningtreestpMstp
        """

        self._openconfig_spanning_treemstp = openconfig_spanning_treemstp

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
        if issubclass(OpenconfigSpanningTreeStpMstp, dict):
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
        if not isinstance(other, OpenconfigSpanningTreeStpMstp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

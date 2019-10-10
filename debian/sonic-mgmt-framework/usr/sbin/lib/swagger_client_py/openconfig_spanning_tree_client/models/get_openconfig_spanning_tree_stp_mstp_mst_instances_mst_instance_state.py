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

from openconfig_spanning_tree_client.models.get_openconfig_spanning_tree_stp_openconfigspanningtreestp_mstp_mstinstances_state import GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpMstpMstinstancesState  # noqa: F401,E501


class GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState(object):
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
        'openconfig_spanning_treestate': 'GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpMstpMstinstancesState'
    }

    attribute_map = {
        'openconfig_spanning_treestate': 'openconfig-spanning-tree:state'
    }

    def __init__(self, openconfig_spanning_treestate=None):  # noqa: E501
        """GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState - a model defined in Swagger"""  # noqa: E501

        self._openconfig_spanning_treestate = None
        self.discriminator = None

        if openconfig_spanning_treestate is not None:
            self.openconfig_spanning_treestate = openconfig_spanning_treestate

    @property
    def openconfig_spanning_treestate(self):
        """Gets the openconfig_spanning_treestate of this GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState.  # noqa: E501


        :return: The openconfig_spanning_treestate of this GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState.  # noqa: E501
        :rtype: GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpMstpMstinstancesState
        """
        return self._openconfig_spanning_treestate

    @openconfig_spanning_treestate.setter
    def openconfig_spanning_treestate(self, openconfig_spanning_treestate):
        """Sets the openconfig_spanning_treestate of this GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState.


        :param openconfig_spanning_treestate: The openconfig_spanning_treestate of this GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState.  # noqa: E501
        :type: GetOpenconfigSpanningTreeStpOpenconfigspanningtreestpMstpMstinstancesState
        """

        self._openconfig_spanning_treestate = openconfig_spanning_treestate

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
        if issubclass(GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState, dict):
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
        if not isinstance(other, GetOpenconfigSpanningTreeStpMstpMstInstancesMstInstanceState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

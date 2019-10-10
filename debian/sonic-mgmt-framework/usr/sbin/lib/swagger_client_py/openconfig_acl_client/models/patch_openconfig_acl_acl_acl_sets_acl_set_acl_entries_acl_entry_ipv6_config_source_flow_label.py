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

from openconfig_acl_client.models.openconfig_acl_acl_acl_sets_acl_set_acl_entries_acl_entry_ipv6_config_source_flow_label import OpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel  # noqa: F401,E501


class PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel(object):
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
        'openconfig_aclsource_flow_label': 'int'
    }

    attribute_map = {
        'openconfig_aclsource_flow_label': 'openconfig-acl:source-flow-label'
    }

    def __init__(self, openconfig_aclsource_flow_label=None):  # noqa: E501
        """PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel - a model defined in Swagger"""  # noqa: E501

        self._openconfig_aclsource_flow_label = None
        self.discriminator = None

        if openconfig_aclsource_flow_label is not None:
            self.openconfig_aclsource_flow_label = openconfig_aclsource_flow_label

    @property
    def openconfig_aclsource_flow_label(self):
        """Gets the openconfig_aclsource_flow_label of this PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel.  # noqa: E501


        :return: The openconfig_aclsource_flow_label of this PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_aclsource_flow_label

    @openconfig_aclsource_flow_label.setter
    def openconfig_aclsource_flow_label(self, openconfig_aclsource_flow_label):
        """Sets the openconfig_aclsource_flow_label of this PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel.


        :param openconfig_aclsource_flow_label: The openconfig_aclsource_flow_label of this PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel.  # noqa: E501
        :type: int
        """

        self._openconfig_aclsource_flow_label = openconfig_aclsource_flow_label

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
        if issubclass(PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel, dict):
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
        if not isinstance(other, PatchOpenconfigAclAclAclSetsAclSetAclEntriesAclEntryIpv6ConfigSourceFlowLabel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_global_config_bpdu_filter import OpenconfigSpanningTreeStpGlobalConfigBpduFilter  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_global_config_bpdu_guard import OpenconfigSpanningTreeStpGlobalConfigBpduGuard  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_global_config_bpduguard_timeout_recovery import OpenconfigSpanningTreeStpGlobalConfigBpduguardTimeoutRecovery  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_global_config_bridge_assurance import OpenconfigSpanningTreeStpGlobalConfigBridgeAssurance  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_global_config_enabled_protocol import OpenconfigSpanningTreeStpGlobalConfigEnabledProtocol  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_global_config_etherchannel_misconfig_guard import OpenconfigSpanningTreeStpGlobalConfigEtherchannelMisconfigGuard  # noqa: F401,E501
from openconfig_spanning_tree_client.models.openconfig_spanning_tree_stp_global_config_loop_guard import OpenconfigSpanningTreeStpGlobalConfigLoopGuard  # noqa: F401,E501


class PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol(object):
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
        'openconfig_spanning_treeenabled_protocol': 'list[str]',
        'openconfig_spanning_treebridge_assurance': 'bool',
        'openconfig_spanning_treeetherchannel_misconfig_guard': 'bool',
        'openconfig_spanning_treebpduguard_timeout_recovery': 'int',
        'openconfig_spanning_treeloop_guard': 'bool',
        'openconfig_spanning_treebpdu_guard': 'bool',
        'openconfig_spanning_treebpdu_filter': 'bool'
    }

    attribute_map = {
        'openconfig_spanning_treeenabled_protocol': 'openconfig-spanning-tree:enabled-protocol',
        'openconfig_spanning_treebridge_assurance': 'openconfig-spanning-tree:bridge-assurance',
        'openconfig_spanning_treeetherchannel_misconfig_guard': 'openconfig-spanning-tree:etherchannel-misconfig-guard',
        'openconfig_spanning_treebpduguard_timeout_recovery': 'openconfig-spanning-tree:bpduguard-timeout-recovery',
        'openconfig_spanning_treeloop_guard': 'openconfig-spanning-tree:loop-guard',
        'openconfig_spanning_treebpdu_guard': 'openconfig-spanning-tree:bpdu-guard',
        'openconfig_spanning_treebpdu_filter': 'openconfig-spanning-tree:bpdu-filter'
    }

    def __init__(self, openconfig_spanning_treeenabled_protocol=None, openconfig_spanning_treebridge_assurance=None, openconfig_spanning_treeetherchannel_misconfig_guard=None, openconfig_spanning_treebpduguard_timeout_recovery=None, openconfig_spanning_treeloop_guard=None, openconfig_spanning_treebpdu_guard=None, openconfig_spanning_treebpdu_filter=None):  # noqa: E501
        """PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol - a model defined in Swagger"""  # noqa: E501

        self._openconfig_spanning_treeenabled_protocol = None
        self._openconfig_spanning_treebridge_assurance = None
        self._openconfig_spanning_treeetherchannel_misconfig_guard = None
        self._openconfig_spanning_treebpduguard_timeout_recovery = None
        self._openconfig_spanning_treeloop_guard = None
        self._openconfig_spanning_treebpdu_guard = None
        self._openconfig_spanning_treebpdu_filter = None
        self.discriminator = None

        if openconfig_spanning_treeenabled_protocol is not None:
            self.openconfig_spanning_treeenabled_protocol = openconfig_spanning_treeenabled_protocol
        if openconfig_spanning_treebridge_assurance is not None:
            self.openconfig_spanning_treebridge_assurance = openconfig_spanning_treebridge_assurance
        if openconfig_spanning_treeetherchannel_misconfig_guard is not None:
            self.openconfig_spanning_treeetherchannel_misconfig_guard = openconfig_spanning_treeetherchannel_misconfig_guard
        if openconfig_spanning_treebpduguard_timeout_recovery is not None:
            self.openconfig_spanning_treebpduguard_timeout_recovery = openconfig_spanning_treebpduguard_timeout_recovery
        if openconfig_spanning_treeloop_guard is not None:
            self.openconfig_spanning_treeloop_guard = openconfig_spanning_treeloop_guard
        if openconfig_spanning_treebpdu_guard is not None:
            self.openconfig_spanning_treebpdu_guard = openconfig_spanning_treebpdu_guard
        if openconfig_spanning_treebpdu_filter is not None:
            self.openconfig_spanning_treebpdu_filter = openconfig_spanning_treebpdu_filter

    @property
    def openconfig_spanning_treeenabled_protocol(self):
        """Gets the openconfig_spanning_treeenabled_protocol of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501


        :return: The openconfig_spanning_treeenabled_protocol of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :rtype: list[str]
        """
        return self._openconfig_spanning_treeenabled_protocol

    @openconfig_spanning_treeenabled_protocol.setter
    def openconfig_spanning_treeenabled_protocol(self, openconfig_spanning_treeenabled_protocol):
        """Sets the openconfig_spanning_treeenabled_protocol of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.


        :param openconfig_spanning_treeenabled_protocol: The openconfig_spanning_treeenabled_protocol of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :type: list[str]
        """

        self._openconfig_spanning_treeenabled_protocol = openconfig_spanning_treeenabled_protocol

    @property
    def openconfig_spanning_treebridge_assurance(self):
        """Gets the openconfig_spanning_treebridge_assurance of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501


        :return: The openconfig_spanning_treebridge_assurance of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_spanning_treebridge_assurance

    @openconfig_spanning_treebridge_assurance.setter
    def openconfig_spanning_treebridge_assurance(self, openconfig_spanning_treebridge_assurance):
        """Sets the openconfig_spanning_treebridge_assurance of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.


        :param openconfig_spanning_treebridge_assurance: The openconfig_spanning_treebridge_assurance of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :type: bool
        """

        self._openconfig_spanning_treebridge_assurance = openconfig_spanning_treebridge_assurance

    @property
    def openconfig_spanning_treeetherchannel_misconfig_guard(self):
        """Gets the openconfig_spanning_treeetherchannel_misconfig_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501


        :return: The openconfig_spanning_treeetherchannel_misconfig_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_spanning_treeetherchannel_misconfig_guard

    @openconfig_spanning_treeetherchannel_misconfig_guard.setter
    def openconfig_spanning_treeetherchannel_misconfig_guard(self, openconfig_spanning_treeetherchannel_misconfig_guard):
        """Sets the openconfig_spanning_treeetherchannel_misconfig_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.


        :param openconfig_spanning_treeetherchannel_misconfig_guard: The openconfig_spanning_treeetherchannel_misconfig_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :type: bool
        """

        self._openconfig_spanning_treeetherchannel_misconfig_guard = openconfig_spanning_treeetherchannel_misconfig_guard

    @property
    def openconfig_spanning_treebpduguard_timeout_recovery(self):
        """Gets the openconfig_spanning_treebpduguard_timeout_recovery of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501


        :return: The openconfig_spanning_treebpduguard_timeout_recovery of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_spanning_treebpduguard_timeout_recovery

    @openconfig_spanning_treebpduguard_timeout_recovery.setter
    def openconfig_spanning_treebpduguard_timeout_recovery(self, openconfig_spanning_treebpduguard_timeout_recovery):
        """Sets the openconfig_spanning_treebpduguard_timeout_recovery of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.


        :param openconfig_spanning_treebpduguard_timeout_recovery: The openconfig_spanning_treebpduguard_timeout_recovery of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :type: int
        """

        self._openconfig_spanning_treebpduguard_timeout_recovery = openconfig_spanning_treebpduguard_timeout_recovery

    @property
    def openconfig_spanning_treeloop_guard(self):
        """Gets the openconfig_spanning_treeloop_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501


        :return: The openconfig_spanning_treeloop_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_spanning_treeloop_guard

    @openconfig_spanning_treeloop_guard.setter
    def openconfig_spanning_treeloop_guard(self, openconfig_spanning_treeloop_guard):
        """Sets the openconfig_spanning_treeloop_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.


        :param openconfig_spanning_treeloop_guard: The openconfig_spanning_treeloop_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :type: bool
        """

        self._openconfig_spanning_treeloop_guard = openconfig_spanning_treeloop_guard

    @property
    def openconfig_spanning_treebpdu_guard(self):
        """Gets the openconfig_spanning_treebpdu_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501


        :return: The openconfig_spanning_treebpdu_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_spanning_treebpdu_guard

    @openconfig_spanning_treebpdu_guard.setter
    def openconfig_spanning_treebpdu_guard(self, openconfig_spanning_treebpdu_guard):
        """Sets the openconfig_spanning_treebpdu_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.


        :param openconfig_spanning_treebpdu_guard: The openconfig_spanning_treebpdu_guard of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :type: bool
        """

        self._openconfig_spanning_treebpdu_guard = openconfig_spanning_treebpdu_guard

    @property
    def openconfig_spanning_treebpdu_filter(self):
        """Gets the openconfig_spanning_treebpdu_filter of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501


        :return: The openconfig_spanning_treebpdu_filter of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_spanning_treebpdu_filter

    @openconfig_spanning_treebpdu_filter.setter
    def openconfig_spanning_treebpdu_filter(self, openconfig_spanning_treebpdu_filter):
        """Sets the openconfig_spanning_treebpdu_filter of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.


        :param openconfig_spanning_treebpdu_filter: The openconfig_spanning_treebpdu_filter of this PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol.  # noqa: E501
        :type: bool
        """

        self._openconfig_spanning_treebpdu_filter = openconfig_spanning_treebpdu_filter

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
        if issubclass(PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol, dict):
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
        if not isinstance(other, PostOpenconfigSpanningTreeStpGlobalConfigEnabledProtocol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

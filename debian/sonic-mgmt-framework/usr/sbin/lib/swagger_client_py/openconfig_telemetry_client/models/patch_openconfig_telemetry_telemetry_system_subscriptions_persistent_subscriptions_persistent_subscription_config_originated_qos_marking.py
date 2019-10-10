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

from openconfig_telemetry_client.models.openconfig_telemetry_telemetry_system_subscriptions_persistent_subscriptions_persistent_subscription_config_originated_qos_marking import OpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking  # noqa: F401,E501


class PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking(object):
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
        'openconfig_telemetryoriginated_qos_marking': 'int'
    }

    attribute_map = {
        'openconfig_telemetryoriginated_qos_marking': 'openconfig-telemetry:originated-qos-marking'
    }

    def __init__(self, openconfig_telemetryoriginated_qos_marking=None):  # noqa: E501
        """PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking - a model defined in Swagger"""  # noqa: E501

        self._openconfig_telemetryoriginated_qos_marking = None
        self.discriminator = None

        if openconfig_telemetryoriginated_qos_marking is not None:
            self.openconfig_telemetryoriginated_qos_marking = openconfig_telemetryoriginated_qos_marking

    @property
    def openconfig_telemetryoriginated_qos_marking(self):
        """Gets the openconfig_telemetryoriginated_qos_marking of this PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking.  # noqa: E501


        :return: The openconfig_telemetryoriginated_qos_marking of this PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking.  # noqa: E501
        :rtype: int
        """
        return self._openconfig_telemetryoriginated_qos_marking

    @openconfig_telemetryoriginated_qos_marking.setter
    def openconfig_telemetryoriginated_qos_marking(self, openconfig_telemetryoriginated_qos_marking):
        """Sets the openconfig_telemetryoriginated_qos_marking of this PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking.


        :param openconfig_telemetryoriginated_qos_marking: The openconfig_telemetryoriginated_qos_marking of this PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking.  # noqa: E501
        :type: int
        """

        self._openconfig_telemetryoriginated_qos_marking = openconfig_telemetryoriginated_qos_marking

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
        if issubclass(PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking, dict):
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
        if not isinstance(other, PatchOpenconfigTelemetryTelemetrySystemSubscriptionsPersistentSubscriptionsPersistentSubscriptionConfigOriginatedQosMarking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

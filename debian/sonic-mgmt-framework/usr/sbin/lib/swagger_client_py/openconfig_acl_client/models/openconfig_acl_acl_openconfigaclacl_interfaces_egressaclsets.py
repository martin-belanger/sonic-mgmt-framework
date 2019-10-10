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

from openconfig_acl_client.models.openconfig_acl_acl_openconfigaclacl_interfaces_ingressaclsets_ingressaclset import OpenconfigAclAclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset  # noqa: F401,E501


class OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets(object):
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
        'egress_acl_set': 'list[OpenconfigAclAclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset]'
    }

    attribute_map = {
        'egress_acl_set': 'egress-acl-set'
    }

    def __init__(self, egress_acl_set=None):  # noqa: E501
        """OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets - a model defined in Swagger"""  # noqa: E501

        self._egress_acl_set = None
        self.discriminator = None

        if egress_acl_set is not None:
            self.egress_acl_set = egress_acl_set

    @property
    def egress_acl_set(self):
        """Gets the egress_acl_set of this OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets.  # noqa: E501


        :return: The egress_acl_set of this OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets.  # noqa: E501
        :rtype: list[OpenconfigAclAclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset]
        """
        return self._egress_acl_set

    @egress_acl_set.setter
    def egress_acl_set(self, egress_acl_set):
        """Sets the egress_acl_set of this OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets.


        :param egress_acl_set: The egress_acl_set of this OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets.  # noqa: E501
        :type: list[OpenconfigAclAclOpenconfigaclaclInterfacesIngressaclsetsIngressaclset]
        """

        self._egress_acl_set = egress_acl_set

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
        if issubclass(OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets, dict):
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
        if not isinstance(other, OpenconfigAclAclOpenconfigaclaclInterfacesEgressaclsets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

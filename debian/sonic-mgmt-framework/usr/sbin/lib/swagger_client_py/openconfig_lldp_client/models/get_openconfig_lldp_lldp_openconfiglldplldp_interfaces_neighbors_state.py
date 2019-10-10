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


class GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState(object):
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
        'system_name': 'str',
        'system_description': 'str',
        'chassis_id': 'str',
        'chassis_id_type': 'str',
        'id': 'str',
        'age': 'int',
        'last_update': 'int',
        'ttl': 'int',
        'port_id': 'str',
        'port_id_type': 'str',
        'port_description': 'str',
        'management_address': 'str',
        'management_address_type': 'str'
    }

    attribute_map = {
        'system_name': 'system-name',
        'system_description': 'system-description',
        'chassis_id': 'chassis-id',
        'chassis_id_type': 'chassis-id-type',
        'id': 'id',
        'age': 'age',
        'last_update': 'last-update',
        'ttl': 'ttl',
        'port_id': 'port-id',
        'port_id_type': 'port-id-type',
        'port_description': 'port-description',
        'management_address': 'management-address',
        'management_address_type': 'management-address-type'
    }

    def __init__(self, system_name=None, system_description=None, chassis_id=None, chassis_id_type=None, id=None, age=None, last_update=None, ttl=None, port_id=None, port_id_type=None, port_description=None, management_address=None, management_address_type=None):  # noqa: E501
        """GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState - a model defined in Swagger"""  # noqa: E501

        self._system_name = None
        self._system_description = None
        self._chassis_id = None
        self._chassis_id_type = None
        self._id = None
        self._age = None
        self._last_update = None
        self._ttl = None
        self._port_id = None
        self._port_id_type = None
        self._port_description = None
        self._management_address = None
        self._management_address_type = None
        self.discriminator = None

        if system_name is not None:
            self.system_name = system_name
        if system_description is not None:
            self.system_description = system_description
        if chassis_id is not None:
            self.chassis_id = chassis_id
        if chassis_id_type is not None:
            self.chassis_id_type = chassis_id_type
        if id is not None:
            self.id = id
        if age is not None:
            self.age = age
        if last_update is not None:
            self.last_update = last_update
        if ttl is not None:
            self.ttl = ttl
        if port_id is not None:
            self.port_id = port_id
        if port_id_type is not None:
            self.port_id_type = port_id_type
        if port_description is not None:
            self.port_description = port_description
        if management_address is not None:
            self.management_address = management_address
        if management_address_type is not None:
            self.management_address_type = management_address_type

    @property
    def system_name(self):
        """Gets the system_name of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The system_name of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """Sets the system_name of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param system_name: The system_name of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._system_name = system_name

    @property
    def system_description(self):
        """Gets the system_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The system_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._system_description

    @system_description.setter
    def system_description(self, system_description):
        """Sets the system_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param system_description: The system_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._system_description = system_description

    @property
    def chassis_id(self):
        """Gets the chassis_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The chassis_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        """Sets the chassis_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param chassis_id: The chassis_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._chassis_id = chassis_id

    @property
    def chassis_id_type(self):
        """Gets the chassis_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The chassis_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._chassis_id_type

    @chassis_id_type.setter
    def chassis_id_type(self, chassis_id_type):
        """Sets the chassis_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param chassis_id_type: The chassis_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """
        allowed_values = ["CHASSIS_COMPONENT", "INTERFACE_ALIAS", "PORT_COMPONENT", "MAC_ADDRESS", "NETWORK_ADDRESS", "INTERFACE_NAME", "LOCAL"]  # noqa: E501
        if chassis_id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `chassis_id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(chassis_id_type, allowed_values)
            )

        self._chassis_id_type = chassis_id_type

    @property
    def id(self):
        """Gets the id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param id: The id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def age(self):
        """Gets the age of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The age of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param age: The age of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: int
        """

        self._age = age

    @property
    def last_update(self):
        """Gets the last_update of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The last_update of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param last_update: The last_update of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: int
        """

        self._last_update = last_update

    @property
    def ttl(self):
        """Gets the ttl of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The ttl of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param ttl: The ttl of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: int
        """

        self._ttl = ttl

    @property
    def port_id(self):
        """Gets the port_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The port_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        """Sets the port_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param port_id: The port_id of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._port_id = port_id

    @property
    def port_id_type(self):
        """Gets the port_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The port_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._port_id_type

    @port_id_type.setter
    def port_id_type(self, port_id_type):
        """Sets the port_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param port_id_type: The port_id_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """
        allowed_values = ["INTERFACE_ALIAS", "PORT_COMPONENT", "MAC_ADDRESS", "NETWORK_ADDRESS", "INTERFACE_NAME", "AGENT_CIRCUIT_ID", "LOCAL"]  # noqa: E501
        if port_id_type not in allowed_values:
            raise ValueError(
                "Invalid value for `port_id_type` ({0}), must be one of {1}"  # noqa: E501
                .format(port_id_type, allowed_values)
            )

        self._port_id_type = port_id_type

    @property
    def port_description(self):
        """Gets the port_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The port_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._port_description

    @port_description.setter
    def port_description(self, port_description):
        """Sets the port_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param port_description: The port_description of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._port_description = port_description

    @property
    def management_address(self):
        """Gets the management_address of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The management_address of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._management_address

    @management_address.setter
    def management_address(self, management_address):
        """Sets the management_address of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param management_address: The management_address of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._management_address = management_address

    @property
    def management_address_type(self):
        """Gets the management_address_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501


        :return: The management_address_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :rtype: str
        """
        return self._management_address_type

    @management_address_type.setter
    def management_address_type(self, management_address_type):
        """Sets the management_address_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.


        :param management_address_type: The management_address_type of this GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState.  # noqa: E501
        :type: str
        """

        self._management_address_type = management_address_type

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
        if issubclass(GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState, dict):
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
        if not isinstance(other, GetOpenconfigLldpLldpOpenconfiglldplldpInterfacesNeighborsState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

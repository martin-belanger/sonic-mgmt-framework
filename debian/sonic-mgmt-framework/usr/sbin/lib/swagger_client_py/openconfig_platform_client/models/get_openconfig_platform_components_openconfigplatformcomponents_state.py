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

from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_state_memory import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateMemory  # noqa: F401,E501
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_state_temperature import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateTemperature  # noqa: F401,E501


class GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState(object):
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
        'name': 'str',
        'type': 'str',
        'id': 'str',
        'location': 'str',
        'description': 'str',
        'mfg_name': 'str',
        'mfg_date': 'str',
        'hardware_version': 'str',
        'firmware_version': 'str',
        'software_version': 'str',
        'serial_no': 'str',
        'part_no': 'str',
        'removable': 'bool',
        'oper_status': 'str',
        'empty': 'bool',
        'parent': 'str',
        'temperature': 'GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateTemperature',
        'memory': 'GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateMemory',
        'allocated_power': 'int',
        'used_power': 'int',
        'openconfig_alarmsequipment_failure': 'bool',
        'openconfig_alarmsequipment_mismatch': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'id': 'id',
        'location': 'location',
        'description': 'description',
        'mfg_name': 'mfg-name',
        'mfg_date': 'mfg-date',
        'hardware_version': 'hardware-version',
        'firmware_version': 'firmware-version',
        'software_version': 'software-version',
        'serial_no': 'serial-no',
        'part_no': 'part-no',
        'removable': 'removable',
        'oper_status': 'oper-status',
        'empty': 'empty',
        'parent': 'parent',
        'temperature': 'temperature',
        'memory': 'memory',
        'allocated_power': 'allocated-power',
        'used_power': 'used-power',
        'openconfig_alarmsequipment_failure': 'openconfig-alarms:equipment-failure',
        'openconfig_alarmsequipment_mismatch': 'openconfig-alarms:equipment-mismatch'
    }

    def __init__(self, name=None, type=None, id=None, location=None, description=None, mfg_name=None, mfg_date=None, hardware_version=None, firmware_version=None, software_version=None, serial_no=None, part_no=None, removable=None, oper_status=None, empty=None, parent=None, temperature=None, memory=None, allocated_power=None, used_power=None, openconfig_alarmsequipment_failure=None, openconfig_alarmsequipment_mismatch=None):  # noqa: E501
        """GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._type = None
        self._id = None
        self._location = None
        self._description = None
        self._mfg_name = None
        self._mfg_date = None
        self._hardware_version = None
        self._firmware_version = None
        self._software_version = None
        self._serial_no = None
        self._part_no = None
        self._removable = None
        self._oper_status = None
        self._empty = None
        self._parent = None
        self._temperature = None
        self._memory = None
        self._allocated_power = None
        self._used_power = None
        self._openconfig_alarmsequipment_failure = None
        self._openconfig_alarmsequipment_mismatch = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if location is not None:
            self.location = location
        if description is not None:
            self.description = description
        if mfg_name is not None:
            self.mfg_name = mfg_name
        if mfg_date is not None:
            self.mfg_date = mfg_date
        if hardware_version is not None:
            self.hardware_version = hardware_version
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if software_version is not None:
            self.software_version = software_version
        if serial_no is not None:
            self.serial_no = serial_no
        if part_no is not None:
            self.part_no = part_no
        if removable is not None:
            self.removable = removable
        if oper_status is not None:
            self.oper_status = oper_status
        if empty is not None:
            self.empty = empty
        if parent is not None:
            self.parent = parent
        if temperature is not None:
            self.temperature = temperature
        if memory is not None:
            self.memory = memory
        if allocated_power is not None:
            self.allocated_power = allocated_power
        if used_power is not None:
            self.used_power = used_power
        if openconfig_alarmsequipment_failure is not None:
            self.openconfig_alarmsequipment_failure = openconfig_alarmsequipment_failure
        if openconfig_alarmsequipment_mismatch is not None:
            self.openconfig_alarmsequipment_mismatch = openconfig_alarmsequipment_mismatch

    @property
    def name(self):
        """Gets the name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param name: The name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The type of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param type: The type of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The id of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param id: The id of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def location(self):
        """Gets the location of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The location of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param location: The location of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def description(self):
        """Gets the description of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The description of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param description: The description of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mfg_name(self):
        """Gets the mfg_name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The mfg_name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._mfg_name

    @mfg_name.setter
    def mfg_name(self, mfg_name):
        """Sets the mfg_name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param mfg_name: The mfg_name of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._mfg_name = mfg_name

    @property
    def mfg_date(self):
        """Gets the mfg_date of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The mfg_date of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._mfg_date

    @mfg_date.setter
    def mfg_date(self, mfg_date):
        """Sets the mfg_date of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param mfg_date: The mfg_date of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._mfg_date = mfg_date

    @property
    def hardware_version(self):
        """Gets the hardware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The hardware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._hardware_version

    @hardware_version.setter
    def hardware_version(self, hardware_version):
        """Sets the hardware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param hardware_version: The hardware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._hardware_version = hardware_version

    @property
    def firmware_version(self):
        """Gets the firmware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The firmware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param firmware_version: The firmware_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._firmware_version = firmware_version

    @property
    def software_version(self):
        """Gets the software_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The software_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param software_version: The software_version of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def serial_no(self):
        """Gets the serial_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The serial_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._serial_no

    @serial_no.setter
    def serial_no(self, serial_no):
        """Sets the serial_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param serial_no: The serial_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._serial_no = serial_no

    @property
    def part_no(self):
        """Gets the part_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The part_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._part_no

    @part_no.setter
    def part_no(self, part_no):
        """Sets the part_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param part_no: The part_no of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._part_no = part_no

    @property
    def removable(self):
        """Gets the removable of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The removable of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: bool
        """
        return self._removable

    @removable.setter
    def removable(self, removable):
        """Sets the removable of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param removable: The removable of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: bool
        """

        self._removable = removable

    @property
    def oper_status(self):
        """Gets the oper_status of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The oper_status of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._oper_status

    @oper_status.setter
    def oper_status(self, oper_status):
        """Sets the oper_status of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param oper_status: The oper_status of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._oper_status = oper_status

    @property
    def empty(self):
        """Gets the empty of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The empty of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param empty: The empty of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: bool
        """

        self._empty = empty

    @property
    def parent(self):
        """Gets the parent of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The parent of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param parent: The parent of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def temperature(self):
        """Gets the temperature of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The temperature of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param temperature: The temperature of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateTemperature
        """

        self._temperature = temperature

    @property
    def memory(self):
        """Gets the memory of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The memory of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateMemory
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param memory: The memory of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateMemory
        """

        self._memory = memory

    @property
    def allocated_power(self):
        """Gets the allocated_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The allocated_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: int
        """
        return self._allocated_power

    @allocated_power.setter
    def allocated_power(self, allocated_power):
        """Sets the allocated_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param allocated_power: The allocated_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: int
        """

        self._allocated_power = allocated_power

    @property
    def used_power(self):
        """Gets the used_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The used_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: int
        """
        return self._used_power

    @used_power.setter
    def used_power(self, used_power):
        """Sets the used_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param used_power: The used_power of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: int
        """

        self._used_power = used_power

    @property
    def openconfig_alarmsequipment_failure(self):
        """Gets the openconfig_alarmsequipment_failure of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The openconfig_alarmsequipment_failure of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_alarmsequipment_failure

    @openconfig_alarmsequipment_failure.setter
    def openconfig_alarmsequipment_failure(self, openconfig_alarmsequipment_failure):
        """Sets the openconfig_alarmsequipment_failure of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param openconfig_alarmsequipment_failure: The openconfig_alarmsequipment_failure of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: bool
        """

        self._openconfig_alarmsequipment_failure = openconfig_alarmsequipment_failure

    @property
    def openconfig_alarmsequipment_mismatch(self):
        """Gets the openconfig_alarmsequipment_mismatch of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501


        :return: The openconfig_alarmsequipment_mismatch of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :rtype: bool
        """
        return self._openconfig_alarmsequipment_mismatch

    @openconfig_alarmsequipment_mismatch.setter
    def openconfig_alarmsequipment_mismatch(self, openconfig_alarmsequipment_mismatch):
        """Sets the openconfig_alarmsequipment_mismatch of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.


        :param openconfig_alarmsequipment_mismatch: The openconfig_alarmsequipment_mismatch of this GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState.  # noqa: E501
        :type: bool
        """

        self._openconfig_alarmsequipment_mismatch = openconfig_alarmsequipment_mismatch

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
        if issubclass(GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState, dict):
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
        if not isinstance(other, GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

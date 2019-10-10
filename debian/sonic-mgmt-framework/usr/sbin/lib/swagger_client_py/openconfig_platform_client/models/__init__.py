# coding: utf-8

# flake8: noqa
"""
    Sonic Network Management APIs

    Network management Open APIs for Sonic.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from openconfig_platform_client.models.get_openconfig_alarms_components_component_state_equipment_failure import GetOpenconfigAlarmsComponentsComponentStateEquipmentFailure
from openconfig_platform_client.models.get_openconfig_alarms_components_component_state_equipment_mismatch import GetOpenconfigAlarmsComponentsComponentStateEquipmentMismatch
from openconfig_platform_client.models.get_openconfig_platform_components import GetOpenconfigPlatformComponents
from openconfig_platform_client.models.get_openconfig_platform_components_component import GetOpenconfigPlatformComponentsComponent
from openconfig_platform_client.models.get_openconfig_platform_components_component_backplane import GetOpenconfigPlatformComponentsComponentBackplane
from openconfig_platform_client.models.get_openconfig_platform_components_component_chassis import GetOpenconfigPlatformComponentsComponentChassis
from openconfig_platform_client.models.get_openconfig_platform_components_component_config import GetOpenconfigPlatformComponentsComponentConfig
from openconfig_platform_client.models.get_openconfig_platform_components_component_cpu import GetOpenconfigPlatformComponentsComponentCpu
from openconfig_platform_client.models.get_openconfig_platform_components_component_fabric import GetOpenconfigPlatformComponentsComponentFabric
from openconfig_platform_client.models.get_openconfig_platform_components_component_fan import GetOpenconfigPlatformComponentsComponentFan
from openconfig_platform_client.models.get_openconfig_platform_components_component_integrated_circuit import GetOpenconfigPlatformComponentsComponentIntegratedCircuit
from openconfig_platform_client.models.get_openconfig_platform_components_component_port import GetOpenconfigPlatformComponentsComponentPort
from openconfig_platform_client.models.get_openconfig_platform_components_component_power_supply import GetOpenconfigPlatformComponentsComponentPowerSupply
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties import GetOpenconfigPlatformComponentsComponentProperties
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties_property import GetOpenconfigPlatformComponentsComponentPropertiesProperty
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties_property_config import GetOpenconfigPlatformComponentsComponentPropertiesPropertyConfig
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties_property_config_value import GetOpenconfigPlatformComponentsComponentPropertiesPropertyConfigValue
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties_property_state import GetOpenconfigPlatformComponentsComponentPropertiesPropertyState
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties_property_state_configurable import GetOpenconfigPlatformComponentsComponentPropertiesPropertyStateConfigurable
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties_property_state_name import GetOpenconfigPlatformComponentsComponentPropertiesPropertyStateName
from openconfig_platform_client.models.get_openconfig_platform_components_component_properties_property_state_value import GetOpenconfigPlatformComponentsComponentPropertiesPropertyStateValue
from openconfig_platform_client.models.get_openconfig_platform_components_component_state import GetOpenconfigPlatformComponentsComponentState
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_allocated_power import GetOpenconfigPlatformComponentsComponentStateAllocatedPower
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_description import GetOpenconfigPlatformComponentsComponentStateDescription
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_empty import GetOpenconfigPlatformComponentsComponentStateEmpty
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_firmware_version import GetOpenconfigPlatformComponentsComponentStateFirmwareVersion
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_hardware_version import GetOpenconfigPlatformComponentsComponentStateHardwareVersion
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_id import GetOpenconfigPlatformComponentsComponentStateId
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_location import GetOpenconfigPlatformComponentsComponentStateLocation
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_memory import GetOpenconfigPlatformComponentsComponentStateMemory
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_memory_available import GetOpenconfigPlatformComponentsComponentStateMemoryAvailable
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_memory_utilized import GetOpenconfigPlatformComponentsComponentStateMemoryUtilized
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_mfg_date import GetOpenconfigPlatformComponentsComponentStateMfgDate
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_mfg_name import GetOpenconfigPlatformComponentsComponentStateMfgName
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_name import GetOpenconfigPlatformComponentsComponentStateName
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_oper_status import GetOpenconfigPlatformComponentsComponentStateOperStatus
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_parent import GetOpenconfigPlatformComponentsComponentStateParent
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_part_no import GetOpenconfigPlatformComponentsComponentStatePartNo
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_removable import GetOpenconfigPlatformComponentsComponentStateRemovable
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_serial_no import GetOpenconfigPlatformComponentsComponentStateSerialNo
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_software_version import GetOpenconfigPlatformComponentsComponentStateSoftwareVersion
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature import GetOpenconfigPlatformComponentsComponentStateTemperature
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_alarm_severity import GetOpenconfigPlatformComponentsComponentStateTemperatureAlarmSeverity
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_alarm_status import GetOpenconfigPlatformComponentsComponentStateTemperatureAlarmStatus
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_alarm_threshold import GetOpenconfigPlatformComponentsComponentStateTemperatureAlarmThreshold
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_avg import GetOpenconfigPlatformComponentsComponentStateTemperatureAvg
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_instant import GetOpenconfigPlatformComponentsComponentStateTemperatureInstant
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_interval import GetOpenconfigPlatformComponentsComponentStateTemperatureInterval
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_max import GetOpenconfigPlatformComponentsComponentStateTemperatureMax
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_max_time import GetOpenconfigPlatformComponentsComponentStateTemperatureMaxTime
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_min import GetOpenconfigPlatformComponentsComponentStateTemperatureMin
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_temperature_min_time import GetOpenconfigPlatformComponentsComponentStateTemperatureMinTime
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_type import GetOpenconfigPlatformComponentsComponentStateType
from openconfig_platform_client.models.get_openconfig_platform_components_component_state_used_power import GetOpenconfigPlatformComponentsComponentStateUsedPower
from openconfig_platform_client.models.get_openconfig_platform_components_component_storage import GetOpenconfigPlatformComponentsComponentStorage
from openconfig_platform_client.models.get_openconfig_platform_components_component_subcomponents import GetOpenconfigPlatformComponentsComponentSubcomponents
from openconfig_platform_client.models.get_openconfig_platform_components_component_subcomponents_subcomponent import GetOpenconfigPlatformComponentsComponentSubcomponentsSubcomponent
from openconfig_platform_client.models.get_openconfig_platform_components_component_subcomponents_subcomponent_config import GetOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig
from openconfig_platform_client.models.get_openconfig_platform_components_component_subcomponents_subcomponent_state import GetOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentState
from openconfig_platform_client.models.get_openconfig_platform_components_component_subcomponents_subcomponent_state_name import GetOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentStateName
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents import GetOpenconfigPlatformComponentsOpenconfigplatformcomponents
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_component import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsComponent
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_properties import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsProperties
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_properties_property import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsPropertiesProperty
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_properties_state import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsPropertiesState
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_state import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsState
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_state_memory import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateMemory
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_state_temperature import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsStateTemperature
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_subcomponents import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponents
from openconfig_platform_client.models.get_openconfig_platform_components_openconfigplatformcomponents_subcomponents_subcomponent import GetOpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent
from openconfig_platform_client.models.openconfig_platform_components import OpenconfigPlatformComponents
from openconfig_platform_client.models.openconfig_platform_components_component import OpenconfigPlatformComponentsComponent
from openconfig_platform_client.models.openconfig_platform_components_component_backplane import OpenconfigPlatformComponentsComponentBackplane
from openconfig_platform_client.models.openconfig_platform_components_component_chassis import OpenconfigPlatformComponentsComponentChassis
from openconfig_platform_client.models.openconfig_platform_components_component_config import OpenconfigPlatformComponentsComponentConfig
from openconfig_platform_client.models.openconfig_platform_components_component_cpu import OpenconfigPlatformComponentsComponentCpu
from openconfig_platform_client.models.openconfig_platform_components_component_fabric import OpenconfigPlatformComponentsComponentFabric
from openconfig_platform_client.models.openconfig_platform_components_component_fan import OpenconfigPlatformComponentsComponentFan
from openconfig_platform_client.models.openconfig_platform_components_component_integrated_circuit import OpenconfigPlatformComponentsComponentIntegratedCircuit
from openconfig_platform_client.models.openconfig_platform_components_component_port import OpenconfigPlatformComponentsComponentPort
from openconfig_platform_client.models.openconfig_platform_components_component_power_supply import OpenconfigPlatformComponentsComponentPowerSupply
from openconfig_platform_client.models.openconfig_platform_components_component_properties import OpenconfigPlatformComponentsComponentProperties
from openconfig_platform_client.models.openconfig_platform_components_component_properties_property import OpenconfigPlatformComponentsComponentPropertiesProperty
from openconfig_platform_client.models.openconfig_platform_components_component_properties_property_config import OpenconfigPlatformComponentsComponentPropertiesPropertyConfig
from openconfig_platform_client.models.openconfig_platform_components_component_properties_property_config_value import OpenconfigPlatformComponentsComponentPropertiesPropertyConfigValue
from openconfig_platform_client.models.openconfig_platform_components_component_storage import OpenconfigPlatformComponentsComponentStorage
from openconfig_platform_client.models.openconfig_platform_components_component_subcomponents import OpenconfigPlatformComponentsComponentSubcomponents
from openconfig_platform_client.models.openconfig_platform_components_component_subcomponents_subcomponent import OpenconfigPlatformComponentsComponentSubcomponentsSubcomponent
from openconfig_platform_client.models.openconfig_platform_components_component_subcomponents_subcomponent_config import OpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents import OpenconfigPlatformComponentsOpenconfigplatformcomponents
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_component import OpenconfigPlatformComponentsOpenconfigplatformcomponentsComponent
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_config import OpenconfigPlatformComponentsOpenconfigplatformcomponentsConfig
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_properties import OpenconfigPlatformComponentsOpenconfigplatformcomponentsProperties
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_properties_config import OpenconfigPlatformComponentsOpenconfigplatformcomponentsPropertiesConfig
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_properties_property import OpenconfigPlatformComponentsOpenconfigplatformcomponentsPropertiesProperty
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_subcomponents import OpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponents
from openconfig_platform_client.models.openconfig_platform_components_openconfigplatformcomponents_subcomponents_subcomponent import OpenconfigPlatformComponentsOpenconfigplatformcomponentsSubcomponentsSubcomponent
from openconfig_platform_client.models.patch_list_openconfig_platform_components_component import PatchListOpenconfigPlatformComponentsComponent
from openconfig_platform_client.models.patch_list_openconfig_platform_components_component_properties_property import PatchListOpenconfigPlatformComponentsComponentPropertiesProperty
from openconfig_platform_client.models.patch_list_openconfig_platform_components_component_subcomponents_subcomponent import PatchListOpenconfigPlatformComponentsComponentSubcomponentsSubcomponent
from openconfig_platform_client.models.patch_openconfig_platform_components import PatchOpenconfigPlatformComponents
from openconfig_platform_client.models.patch_openconfig_platform_components_component import PatchOpenconfigPlatformComponentsComponent
from openconfig_platform_client.models.patch_openconfig_platform_components_component_backplane import PatchOpenconfigPlatformComponentsComponentBackplane
from openconfig_platform_client.models.patch_openconfig_platform_components_component_chassis import PatchOpenconfigPlatformComponentsComponentChassis
from openconfig_platform_client.models.patch_openconfig_platform_components_component_config import PatchOpenconfigPlatformComponentsComponentConfig
from openconfig_platform_client.models.patch_openconfig_platform_components_component_cpu import PatchOpenconfigPlatformComponentsComponentCpu
from openconfig_platform_client.models.patch_openconfig_platform_components_component_fabric import PatchOpenconfigPlatformComponentsComponentFabric
from openconfig_platform_client.models.patch_openconfig_platform_components_component_fan import PatchOpenconfigPlatformComponentsComponentFan
from openconfig_platform_client.models.patch_openconfig_platform_components_component_integrated_circuit import PatchOpenconfigPlatformComponentsComponentIntegratedCircuit
from openconfig_platform_client.models.patch_openconfig_platform_components_component_port import PatchOpenconfigPlatformComponentsComponentPort
from openconfig_platform_client.models.patch_openconfig_platform_components_component_power_supply import PatchOpenconfigPlatformComponentsComponentPowerSupply
from openconfig_platform_client.models.patch_openconfig_platform_components_component_properties import PatchOpenconfigPlatformComponentsComponentProperties
from openconfig_platform_client.models.patch_openconfig_platform_components_component_properties_property import PatchOpenconfigPlatformComponentsComponentPropertiesProperty
from openconfig_platform_client.models.patch_openconfig_platform_components_component_properties_property_config import PatchOpenconfigPlatformComponentsComponentPropertiesPropertyConfig
from openconfig_platform_client.models.patch_openconfig_platform_components_component_properties_property_config_value import PatchOpenconfigPlatformComponentsComponentPropertiesPropertyConfigValue
from openconfig_platform_client.models.patch_openconfig_platform_components_component_storage import PatchOpenconfigPlatformComponentsComponentStorage
from openconfig_platform_client.models.patch_openconfig_platform_components_component_subcomponents import PatchOpenconfigPlatformComponentsComponentSubcomponents
from openconfig_platform_client.models.patch_openconfig_platform_components_component_subcomponents_subcomponent import PatchOpenconfigPlatformComponentsComponentSubcomponentsSubcomponent
from openconfig_platform_client.models.patch_openconfig_platform_components_component_subcomponents_subcomponent_config import PatchOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig
from openconfig_platform_client.models.post_list_openconfig_platform_components_component import PostListOpenconfigPlatformComponentsComponent
from openconfig_platform_client.models.post_list_openconfig_platform_components_component_properties_property import PostListOpenconfigPlatformComponentsComponentPropertiesProperty
from openconfig_platform_client.models.post_list_openconfig_platform_components_component_subcomponents_subcomponent import PostListOpenconfigPlatformComponentsComponentSubcomponentsSubcomponent
from openconfig_platform_client.models.post_openconfig_platform_components import PostOpenconfigPlatformComponents
from openconfig_platform_client.models.post_openconfig_platform_components_component_config import PostOpenconfigPlatformComponentsComponentConfig
from openconfig_platform_client.models.post_openconfig_platform_components_component_properties_property_config import PostOpenconfigPlatformComponentsComponentPropertiesPropertyConfig
from openconfig_platform_client.models.post_openconfig_platform_components_component_properties_property_config_value import PostOpenconfigPlatformComponentsComponentPropertiesPropertyConfigValue
from openconfig_platform_client.models.post_openconfig_platform_components_component_subcomponents_subcomponent_config import PostOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig
from openconfig_platform_client.models.put_list_openconfig_platform_components_component import PutListOpenconfigPlatformComponentsComponent
from openconfig_platform_client.models.put_list_openconfig_platform_components_component_properties_property import PutListOpenconfigPlatformComponentsComponentPropertiesProperty
from openconfig_platform_client.models.put_list_openconfig_platform_components_component_subcomponents_subcomponent import PutListOpenconfigPlatformComponentsComponentSubcomponentsSubcomponent
from openconfig_platform_client.models.put_openconfig_platform_components import PutOpenconfigPlatformComponents
from openconfig_platform_client.models.put_openconfig_platform_components_component import PutOpenconfigPlatformComponentsComponent
from openconfig_platform_client.models.put_openconfig_platform_components_component_backplane import PutOpenconfigPlatformComponentsComponentBackplane
from openconfig_platform_client.models.put_openconfig_platform_components_component_chassis import PutOpenconfigPlatformComponentsComponentChassis
from openconfig_platform_client.models.put_openconfig_platform_components_component_config import PutOpenconfigPlatformComponentsComponentConfig
from openconfig_platform_client.models.put_openconfig_platform_components_component_cpu import PutOpenconfigPlatformComponentsComponentCpu
from openconfig_platform_client.models.put_openconfig_platform_components_component_fabric import PutOpenconfigPlatformComponentsComponentFabric
from openconfig_platform_client.models.put_openconfig_platform_components_component_fan import PutOpenconfigPlatformComponentsComponentFan
from openconfig_platform_client.models.put_openconfig_platform_components_component_integrated_circuit import PutOpenconfigPlatformComponentsComponentIntegratedCircuit
from openconfig_platform_client.models.put_openconfig_platform_components_component_port import PutOpenconfigPlatformComponentsComponentPort
from openconfig_platform_client.models.put_openconfig_platform_components_component_power_supply import PutOpenconfigPlatformComponentsComponentPowerSupply
from openconfig_platform_client.models.put_openconfig_platform_components_component_properties import PutOpenconfigPlatformComponentsComponentProperties
from openconfig_platform_client.models.put_openconfig_platform_components_component_properties_property import PutOpenconfigPlatformComponentsComponentPropertiesProperty
from openconfig_platform_client.models.put_openconfig_platform_components_component_properties_property_config import PutOpenconfigPlatformComponentsComponentPropertiesPropertyConfig
from openconfig_platform_client.models.put_openconfig_platform_components_component_properties_property_config_value import PutOpenconfigPlatformComponentsComponentPropertiesPropertyConfigValue
from openconfig_platform_client.models.put_openconfig_platform_components_component_storage import PutOpenconfigPlatformComponentsComponentStorage
from openconfig_platform_client.models.put_openconfig_platform_components_component_subcomponents import PutOpenconfigPlatformComponentsComponentSubcomponents
from openconfig_platform_client.models.put_openconfig_platform_components_component_subcomponents_subcomponent import PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponent
from openconfig_platform_client.models.put_openconfig_platform_components_component_subcomponents_subcomponent_config import PutOpenconfigPlatformComponentsComponentSubcomponentsSubcomponentConfig

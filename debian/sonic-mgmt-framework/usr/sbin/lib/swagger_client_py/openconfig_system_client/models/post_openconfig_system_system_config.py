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

from openconfig_system_client.models.openconfig_system_system_aaa import OpenconfigSystemSystemAaa  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_clock import OpenconfigSystemSystemClock  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_config import OpenconfigSystemSystemConfig  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_dns import OpenconfigSystemSystemDns  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_grpc_server import OpenconfigSystemSystemGrpcServer  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_logging import OpenconfigSystemSystemLogging  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_memory import OpenconfigSystemSystemMemory  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_messages import OpenconfigSystemSystemMessages  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_ntp import OpenconfigSystemSystemNtp  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_aaa import OpenconfigSystemSystemOpenconfigsystemsystemAaa  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_clock import OpenconfigSystemSystemOpenconfigsystemsystemClock  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_config import OpenconfigSystemSystemOpenconfigsystemsystemConfig  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_dns import OpenconfigSystemSystemOpenconfigsystemsystemDns  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_grpcserver import OpenconfigSystemSystemOpenconfigsystemsystemGrpcserver  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_logging import OpenconfigSystemSystemOpenconfigsystemsystemLogging  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_messages import OpenconfigSystemSystemOpenconfigsystemsystemMessages  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_ntp import OpenconfigSystemSystemOpenconfigsystemsystemNtp  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_sshserver import OpenconfigSystemSystemOpenconfigsystemsystemSshserver  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_openconfigsystemsystem_telnetserver import OpenconfigSystemSystemOpenconfigsystemsystemTelnetserver  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_processes import OpenconfigSystemSystemProcesses  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_ssh_server import OpenconfigSystemSystemSshServer  # noqa: F401,E501
from openconfig_system_client.models.openconfig_system_system_telnet_server import OpenconfigSystemSystemTelnetServer  # noqa: F401,E501


class PostOpenconfigSystemSystemConfig(object):
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
        'openconfig_systemconfig': 'OpenconfigSystemSystemOpenconfigsystemsystemConfig',
        'openconfig_systemclock': 'OpenconfigSystemSystemOpenconfigsystemsystemClock',
        'openconfig_systemdns': 'OpenconfigSystemSystemOpenconfigsystemsystemDns',
        'openconfig_systemntp': 'OpenconfigSystemSystemOpenconfigsystemsystemNtp',
        'openconfig_systemgrpc_server': 'OpenconfigSystemSystemOpenconfigsystemsystemGrpcserver',
        'openconfig_systemssh_server': 'OpenconfigSystemSystemOpenconfigsystemsystemSshserver',
        'openconfig_systemtelnet_server': 'OpenconfigSystemSystemOpenconfigsystemsystemTelnetserver',
        'openconfig_systemlogging': 'OpenconfigSystemSystemOpenconfigsystemsystemLogging',
        'openconfig_systemaaa': 'OpenconfigSystemSystemOpenconfigsystemsystemAaa',
        'openconfig_systemmemory': 'object',
        'openconfig_systemprocesses': 'object',
        'openconfig_systemmessages': 'OpenconfigSystemSystemOpenconfigsystemsystemMessages'
    }

    attribute_map = {
        'openconfig_systemconfig': 'openconfig-system:config',
        'openconfig_systemclock': 'openconfig-system:clock',
        'openconfig_systemdns': 'openconfig-system:dns',
        'openconfig_systemntp': 'openconfig-system:ntp',
        'openconfig_systemgrpc_server': 'openconfig-system:grpc-server',
        'openconfig_systemssh_server': 'openconfig-system:ssh-server',
        'openconfig_systemtelnet_server': 'openconfig-system:telnet-server',
        'openconfig_systemlogging': 'openconfig-system:logging',
        'openconfig_systemaaa': 'openconfig-system:aaa',
        'openconfig_systemmemory': 'openconfig-system:memory',
        'openconfig_systemprocesses': 'openconfig-system:processes',
        'openconfig_systemmessages': 'openconfig-system:messages'
    }

    def __init__(self, openconfig_systemconfig=None, openconfig_systemclock=None, openconfig_systemdns=None, openconfig_systemntp=None, openconfig_systemgrpc_server=None, openconfig_systemssh_server=None, openconfig_systemtelnet_server=None, openconfig_systemlogging=None, openconfig_systemaaa=None, openconfig_systemmemory=None, openconfig_systemprocesses=None, openconfig_systemmessages=None):  # noqa: E501
        """PostOpenconfigSystemSystemConfig - a model defined in Swagger"""  # noqa: E501

        self._openconfig_systemconfig = None
        self._openconfig_systemclock = None
        self._openconfig_systemdns = None
        self._openconfig_systemntp = None
        self._openconfig_systemgrpc_server = None
        self._openconfig_systemssh_server = None
        self._openconfig_systemtelnet_server = None
        self._openconfig_systemlogging = None
        self._openconfig_systemaaa = None
        self._openconfig_systemmemory = None
        self._openconfig_systemprocesses = None
        self._openconfig_systemmessages = None
        self.discriminator = None

        if openconfig_systemconfig is not None:
            self.openconfig_systemconfig = openconfig_systemconfig
        if openconfig_systemclock is not None:
            self.openconfig_systemclock = openconfig_systemclock
        if openconfig_systemdns is not None:
            self.openconfig_systemdns = openconfig_systemdns
        if openconfig_systemntp is not None:
            self.openconfig_systemntp = openconfig_systemntp
        if openconfig_systemgrpc_server is not None:
            self.openconfig_systemgrpc_server = openconfig_systemgrpc_server
        if openconfig_systemssh_server is not None:
            self.openconfig_systemssh_server = openconfig_systemssh_server
        if openconfig_systemtelnet_server is not None:
            self.openconfig_systemtelnet_server = openconfig_systemtelnet_server
        if openconfig_systemlogging is not None:
            self.openconfig_systemlogging = openconfig_systemlogging
        if openconfig_systemaaa is not None:
            self.openconfig_systemaaa = openconfig_systemaaa
        if openconfig_systemmemory is not None:
            self.openconfig_systemmemory = openconfig_systemmemory
        if openconfig_systemprocesses is not None:
            self.openconfig_systemprocesses = openconfig_systemprocesses
        if openconfig_systemmessages is not None:
            self.openconfig_systemmessages = openconfig_systemmessages

    @property
    def openconfig_systemconfig(self):
        """Gets the openconfig_systemconfig of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemconfig of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemConfig
        """
        return self._openconfig_systemconfig

    @openconfig_systemconfig.setter
    def openconfig_systemconfig(self, openconfig_systemconfig):
        """Sets the openconfig_systemconfig of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemconfig: The openconfig_systemconfig of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemConfig
        """

        self._openconfig_systemconfig = openconfig_systemconfig

    @property
    def openconfig_systemclock(self):
        """Gets the openconfig_systemclock of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemclock of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemClock
        """
        return self._openconfig_systemclock

    @openconfig_systemclock.setter
    def openconfig_systemclock(self, openconfig_systemclock):
        """Sets the openconfig_systemclock of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemclock: The openconfig_systemclock of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemClock
        """

        self._openconfig_systemclock = openconfig_systemclock

    @property
    def openconfig_systemdns(self):
        """Gets the openconfig_systemdns of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemdns of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemDns
        """
        return self._openconfig_systemdns

    @openconfig_systemdns.setter
    def openconfig_systemdns(self, openconfig_systemdns):
        """Sets the openconfig_systemdns of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemdns: The openconfig_systemdns of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemDns
        """

        self._openconfig_systemdns = openconfig_systemdns

    @property
    def openconfig_systemntp(self):
        """Gets the openconfig_systemntp of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemntp of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemNtp
        """
        return self._openconfig_systemntp

    @openconfig_systemntp.setter
    def openconfig_systemntp(self, openconfig_systemntp):
        """Sets the openconfig_systemntp of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemntp: The openconfig_systemntp of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemNtp
        """

        self._openconfig_systemntp = openconfig_systemntp

    @property
    def openconfig_systemgrpc_server(self):
        """Gets the openconfig_systemgrpc_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemgrpc_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemGrpcserver
        """
        return self._openconfig_systemgrpc_server

    @openconfig_systemgrpc_server.setter
    def openconfig_systemgrpc_server(self, openconfig_systemgrpc_server):
        """Sets the openconfig_systemgrpc_server of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemgrpc_server: The openconfig_systemgrpc_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemGrpcserver
        """

        self._openconfig_systemgrpc_server = openconfig_systemgrpc_server

    @property
    def openconfig_systemssh_server(self):
        """Gets the openconfig_systemssh_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemssh_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemSshserver
        """
        return self._openconfig_systemssh_server

    @openconfig_systemssh_server.setter
    def openconfig_systemssh_server(self, openconfig_systemssh_server):
        """Sets the openconfig_systemssh_server of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemssh_server: The openconfig_systemssh_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemSshserver
        """

        self._openconfig_systemssh_server = openconfig_systemssh_server

    @property
    def openconfig_systemtelnet_server(self):
        """Gets the openconfig_systemtelnet_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemtelnet_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemTelnetserver
        """
        return self._openconfig_systemtelnet_server

    @openconfig_systemtelnet_server.setter
    def openconfig_systemtelnet_server(self, openconfig_systemtelnet_server):
        """Sets the openconfig_systemtelnet_server of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemtelnet_server: The openconfig_systemtelnet_server of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemTelnetserver
        """

        self._openconfig_systemtelnet_server = openconfig_systemtelnet_server

    @property
    def openconfig_systemlogging(self):
        """Gets the openconfig_systemlogging of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemlogging of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemLogging
        """
        return self._openconfig_systemlogging

    @openconfig_systemlogging.setter
    def openconfig_systemlogging(self, openconfig_systemlogging):
        """Sets the openconfig_systemlogging of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemlogging: The openconfig_systemlogging of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemLogging
        """

        self._openconfig_systemlogging = openconfig_systemlogging

    @property
    def openconfig_systemaaa(self):
        """Gets the openconfig_systemaaa of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemaaa of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemAaa
        """
        return self._openconfig_systemaaa

    @openconfig_systemaaa.setter
    def openconfig_systemaaa(self, openconfig_systemaaa):
        """Sets the openconfig_systemaaa of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemaaa: The openconfig_systemaaa of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemAaa
        """

        self._openconfig_systemaaa = openconfig_systemaaa

    @property
    def openconfig_systemmemory(self):
        """Gets the openconfig_systemmemory of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemmemory of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: object
        """
        return self._openconfig_systemmemory

    @openconfig_systemmemory.setter
    def openconfig_systemmemory(self, openconfig_systemmemory):
        """Sets the openconfig_systemmemory of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemmemory: The openconfig_systemmemory of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: object
        """

        self._openconfig_systemmemory = openconfig_systemmemory

    @property
    def openconfig_systemprocesses(self):
        """Gets the openconfig_systemprocesses of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemprocesses of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: object
        """
        return self._openconfig_systemprocesses

    @openconfig_systemprocesses.setter
    def openconfig_systemprocesses(self, openconfig_systemprocesses):
        """Sets the openconfig_systemprocesses of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemprocesses: The openconfig_systemprocesses of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: object
        """

        self._openconfig_systemprocesses = openconfig_systemprocesses

    @property
    def openconfig_systemmessages(self):
        """Gets the openconfig_systemmessages of this PostOpenconfigSystemSystemConfig.  # noqa: E501


        :return: The openconfig_systemmessages of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :rtype: OpenconfigSystemSystemOpenconfigsystemsystemMessages
        """
        return self._openconfig_systemmessages

    @openconfig_systemmessages.setter
    def openconfig_systemmessages(self, openconfig_systemmessages):
        """Sets the openconfig_systemmessages of this PostOpenconfigSystemSystemConfig.


        :param openconfig_systemmessages: The openconfig_systemmessages of this PostOpenconfigSystemSystemConfig.  # noqa: E501
        :type: OpenconfigSystemSystemOpenconfigsystemsystemMessages
        """

        self._openconfig_systemmessages = openconfig_systemmessages

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
        if issubclass(PostOpenconfigSystemSystemConfig, dict):
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
        if not isinstance(other, PostOpenconfigSystemSystemConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

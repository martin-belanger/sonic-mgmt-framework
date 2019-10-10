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


class GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal(object):
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
        'instant': 'int',
        'avg': 'int',
        'min': 'int',
        'max': 'int',
        'interval': 'int',
        'min_time': 'int',
        'max_time': 'int'
    }

    attribute_map = {
        'instant': 'instant',
        'avg': 'avg',
        'min': 'min',
        'max': 'max',
        'interval': 'interval',
        'min_time': 'min-time',
        'max_time': 'max-time'
    }

    def __init__(self, instant=None, avg=None, min=None, max=None, interval=None, min_time=None, max_time=None):  # noqa: E501
        """GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal - a model defined in Swagger"""  # noqa: E501

        self._instant = None
        self._avg = None
        self._min = None
        self._max = None
        self._interval = None
        self._min_time = None
        self._max_time = None
        self.discriminator = None

        if instant is not None:
            self.instant = instant
        if avg is not None:
            self.avg = avg
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if interval is not None:
            self.interval = interval
        if min_time is not None:
            self.min_time = min_time
        if max_time is not None:
            self.max_time = max_time

    @property
    def instant(self):
        """Gets the instant of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501


        :return: The instant of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :rtype: int
        """
        return self._instant

    @instant.setter
    def instant(self, instant):
        """Sets the instant of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.


        :param instant: The instant of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :type: int
        """

        self._instant = instant

    @property
    def avg(self):
        """Gets the avg of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501


        :return: The avg of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :rtype: int
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.


        :param avg: The avg of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :type: int
        """

        self._avg = avg

    @property
    def min(self):
        """Gets the min of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501


        :return: The min of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.


        :param min: The min of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501


        :return: The max of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.


        :param max: The max of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def interval(self):
        """Gets the interval of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501


        :return: The interval of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.


        :param interval: The interval of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :type: int
        """

        self._interval = interval

    @property
    def min_time(self):
        """Gets the min_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501


        :return: The min_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :rtype: int
        """
        return self._min_time

    @min_time.setter
    def min_time(self, min_time):
        """Sets the min_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.


        :param min_time: The min_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :type: int
        """

        self._min_time = min_time

    @property
    def max_time(self):
        """Gets the max_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501


        :return: The max_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :rtype: int
        """
        return self._max_time

    @max_time.setter
    def max_time(self, max_time):
        """Sets the max_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.


        :param max_time: The max_time of this GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal.  # noqa: E501
        :type: int
        """

        self._max_time = max_time

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
        if issubclass(GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal, dict):
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
        if not isinstance(other, GetOpenconfigSystemSystemOpenconfigsystemsystemCpusStateTotal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

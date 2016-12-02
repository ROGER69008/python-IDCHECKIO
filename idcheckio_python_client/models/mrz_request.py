# coding: utf-8

"""
    IdCheck.IO API

    Check identity documents

    OpenAPI spec version: 0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class MrzRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, line1=None, line2=None, line3=None):
        """
        MrzRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'line1': 'str',
            'line2': 'str',
            'line3': 'str'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'line1': 'line1',
            'line2': 'line2',
            'line3': 'line3'
        }

        self._api_version = api_version
        self._line1 = line1
        self._line2 = line2
        self._line3 = line3

    @property
    def api_version(self):
        """
        Gets the api_version of this MrzRequest.
        API version (for backward compatibility purpose)

        :return: The api_version of this MrzRequest.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this MrzRequest.
        API version (for backward compatibility purpose)

        :param api_version: The api_version of this MrzRequest.
        :type: str
        """

        self._api_version = api_version

    @property
    def line1(self):
        """
        Gets the line1 of this MrzRequest.
        ligne1 containing MRZ line number 1

        :return: The line1 of this MrzRequest.
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """
        Sets the line1 of this MrzRequest.
        ligne1 containing MRZ line number 1

        :param line1: The line1 of this MrzRequest.
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """
        Gets the line2 of this MrzRequest.
        ligne2 containing MRZ line number 2

        :return: The line2 of this MrzRequest.
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """
        Sets the line2 of this MrzRequest.
        ligne2 containing MRZ line number 2

        :param line2: The line2 of this MrzRequest.
        :type: str
        """

        self._line2 = line2

    @property
    def line3(self):
        """
        Gets the line3 of this MrzRequest.
        ligne3 containing MRZ line number 3

        :return: The line3 of this MrzRequest.
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """
        Sets the line3 of this MrzRequest.
        ligne3 containing MRZ line number 3

        :param line3: The line3 of this MrzRequest.
        :type: str
        """

        self._line3 = line3

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

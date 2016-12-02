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

from __future__ import absolute_import

import os
import sys
import unittest

import idcheckio_python_client
from idcheckio_python_client.rest import ApiException
from idcheckio_python_client.models.mrz_list_response import MrzListResponse


class TestMrzListResponse(unittest.TestCase):
    """ MrzListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMrzListResponse(self):
        """
        Test MrzListResponse
        """
        model = idcheckio_python_client.models.mrz_list_response.MrzListResponse()


if __name__ == '__main__':
    unittest.main()

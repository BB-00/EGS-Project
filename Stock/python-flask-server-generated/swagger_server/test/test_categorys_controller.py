# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.arrayof_category import ArrayofCategory  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCategorysController(BaseTestCase):
    """CategorysController integration test stubs"""

    def test_type_delete(self):
        """Test case for type_delete

        
        """
        response = self.client.open(
            '/MysteryShirt/Stock/1/type',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_type_get(self):
        """Test case for type_get

        
        """
        query_string = [('offset', 56),
                        ('limit', 56),
                        ('type_id', 56),
                        ('name', 'name_example')]
        response = self.client.open(
            '/MysteryShirt/Stock/1/type',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_type_post(self):
        """Test case for type_post

        
        """
        data = dict(type_id=56,
                    name='name_example')
        response = self.client.open(
            '/MysteryShirt/Stock/1/type',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

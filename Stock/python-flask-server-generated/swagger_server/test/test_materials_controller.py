# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.arrayof_material import ArrayofMaterial  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMaterialsController(BaseTestCase):
    """MaterialsController integration test stubs"""

    def test_materials_delete(self):
        """Test case for materials_delete

        
        """
        response = self.client.open(
            '/MysteryShirt/Stock/1/materials',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_materials_get(self):
        """Test case for materials_get

        
        """
        query_string = [('offset', 56),
                        ('limit', 56),
                        ('materials_id', 56),
                        ('name', 'name_example')]
        response = self.client.open(
            '/MysteryShirt/Stock/1/materials',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_materials_post(self):
        """Test case for materials_post

        
        """
        data = dict(materials_id=56,
                    name='name_example')
        response = self.client.open(
            '/MysteryShirt/Stock/1/materials',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

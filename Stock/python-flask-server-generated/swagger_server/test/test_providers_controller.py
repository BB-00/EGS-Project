# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.arrayof_providers import ArrayofProviders  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProvidersController(BaseTestCase):
    """ProvidersController integration test stubs"""

    def test_providers_delete(self):
        """Test case for providers_delete

        
        """
        response = self.client.open(
            '/MysteryShirt/Stock/1/providers',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_providers_get(self):
        """Test case for providers_get

        
        """
        query_string = [('offset', 56),
                        ('limit', 56),
                        ('providers_id', 56),
                        ('name', 'name_example'),
                        ('address', 'address_example'),
                        ('email', 'email_example'),
                        ('site', 'site_example'),
                        ('phone', 56)]
        response = self.client.open(
            '/MysteryShirt/Stock/1/providers',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_providers_post(self):
        """Test case for providers_post

        
        """
        data = dict(providers_id=56,
                    name='name_example',
                    country='country_example',
                    city='city_example',
                    zip=56,
                    address='address_example',
                    email='email_example',
                    site='site_example',
                    phone=56)
        response = self.client.open(
            '/MysteryShirt/Stock/1/providers',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

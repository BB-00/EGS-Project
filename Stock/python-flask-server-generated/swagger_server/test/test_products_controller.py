# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.arrayof_articles import ArrayofArticles  # noqa: E501
from swagger_server.models.arrayof_products import ArrayofProducts  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_article_delete(self):
        """Test case for article_delete

        
        """
        response = self.client.open(
            '/MysteryShirt/Stock/1/article',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_article_get(self):
        """Test case for article_get

        
        """
        query_string = [('offset', 56),
                        ('limit', 56),
                        ('type_id', 56),
                        ('name', 'name_example'),
                        ('quantity', 56)]
        response = self.client.open(
            '/MysteryShirt/Stock/1/article',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_article_post(self):
        """Test case for article_post

        
        """
        data = dict(type_id=56,
                    name='name_example')
        response = self.client.open(
            '/MysteryShirt/Stock/1/article',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_delete(self):
        """Test case for products_delete

        
        """
        response = self.client.open(
            '/MysteryShirt/Stock/1/products',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_get(self):
        """Test case for products_get

        
        """
        query_string = [('offset', 56),
                        ('limit', 56),
                        ('product_id', 56),
                        ('name', 'name_example'),
                        ('reference', 56),
                        ('quantity', 56),
                        ('size', 56)]
        response = self.client.open(
            '/MysteryShirt/Stock/1/products',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_post(self):
        """Test case for products_post

        
        """
        data = dict(product_id=56,
                    name='name_example',
                    size=56,
                    material=56,
                    provider=56,
                    product_type=56,
                    reference=56,
                    quantity=56,
                    buy_price=1.2)
        response = self.client.open(
            '/MysteryShirt/Stock/1/products',
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

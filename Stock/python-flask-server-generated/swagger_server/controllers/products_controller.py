import connexion
import six
import json
import mariadb

from swagger_server.models.arrayof_articles import ArrayofArticles  # noqa: E501
from swagger_server.models.arrayof_products import ArrayofProducts  # noqa: E501
from swagger_server import util



def article_delete():  # noqa: E501
    """article_delete

    removes one product # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def article_get(offset=None, limit=None, type_id=None, name=None, quantity=None):  # noqa: E501
    config = {
        'host' : '127.0.0.1',
        'port' : 3306,
        'user' : 'resende',
        'password' : '',
        'database' : 'egs'
    }

    conn = mariadb.connect(**config)

    cur = conn.cursor()

    cur.execute("select * from article")

    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    # return the results!
    return json.dumps(json_data)

    """article_get

    gets type of product # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :param type_id: Return the article_ID
    :type type_id: int
    :param name: Return the name of the article
    :type name: str
    :param quantity: Return the quantity of the article
    :type quantity: int

    :rtype: ArrayofArticles
    """
    return 'do some magic!'


def article_post(type_id, name):  # noqa: E501
    """article_post

    add a new type # noqa: E501

    :param type_id: 
    :type type_id: int
    :param name: 
    :type name: str

    :rtype: None
    """
    return 'do some magic!'


def products_delete():  # noqa: E501
    """products_delete

    removes one product # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def products_get(offset=None, limit=None, product_id=None, name=None, reference=None, quantity=None, size=None):  # noqa: E501
    config = {
        'host' : '127.0.0.1',
        'port' : 3306,
        'user' : 'resende',
        'password' : '',
        'database' : 'egs'
    }

    conn = mariadb.connect(**config)

    cur = conn.cursor()

    cur.execute("select * from products")

    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    # return the results!
    return json.dumps(json_data)
    """products_get

    gets all available products # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :param product_id: Return the product_ID
    :type product_id: int
    :param name: Return the name of the product
    :type name: str
    :param reference: Return the reference of the product
    :type reference: int
    :param quantity: Return the quantity of products
    :type quantity: int
    :param size: Return the size of the product
    :type size: int

    :rtype: ArrayofProducts
    """
    return 'do some magic!'


def products_post(product_id, name, size, material, provider, product_type, reference, quantity, buy_price):  # noqa: E501
    """products_post

    adds a new product to the available ones # noqa: E501

    :param product_id: 
    :type product_id: int
    :param name: 
    :type name: str
    :param size: 
    :type size: int
    :param material: 
    :type material: int
    :param provider: 
    :type provider: int
    :param product_type: 
    :type product_type: int
    :param reference: 
    :type reference: int
    :param quantity: 
    :type quantity: int
    :param buy_price: 
    :type buy_price: float

    :rtype: None
    """
    return 'do some magic!'

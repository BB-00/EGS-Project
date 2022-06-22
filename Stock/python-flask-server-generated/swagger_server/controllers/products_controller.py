from operator import truediv
import re
import connexion
import six
import json
import mariadb
from unicodedata import name
from flask import jsonify, request

from swagger_server.models.arrayof_articles import ArrayofArticles  # noqa: E501
from swagger_server.models.arrayof_products import ArrayofProducts  # noqa: E501
from swagger_server import util
config = {
    'host' : 'stocks_db',
    'port' : 3306,
    'user' : 'egs',
    'password' : 'egs',
    'database' : 'stock_db'
}

conn = mariadb.connect(**config)

cur = conn.cursor()

product_ID = 0
article_ID = 0


def article_delete():  # noqa: E501
    """article_delete

    removes one product # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def article_get(offset=None, limit=None, type_id=None, name=None, quantity=None):  # noqa: E501


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


def article_post():  # noqa: E501
    article_ID = int(request.json["type_ID"]) #should be article id, but there was a mistake creating the api documentation 
    name = request.json["name"]
    cur.execute("insert into article (article_ID, name) values (?,?)", (article_ID, name))
    conn.commit()


    """materials_post

    adds one material # noqa: E501

    :param materials_id: 
    :type materials_id: int
    :param name: 
    :type name: str

    :rtype: None
    """
    return 'added to db'
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


def products_post():  # noqa: E501
    product_ID = int(request.json["product_ID"]) 
    name = request.json["name"]
    size = request.json["size"]
    material = request.json["material"]
    provider = request.json["provider"]
    product_type = request.json["product_type"]
    reference = request.json["reference"]
    quantity = request.json["quantity"]
    buy_price = request.json["buy_price"]

    
    cur.execute("select product_ID from products")
    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))


    found = True

    for x in json_data:
        if(x["product_ID"] == product_ID):
            found = False
            break
        

    if (found):
        cur.execute("insert into products (product_ID, name, size, material, provider, product_type, reference, quantity, buy_price) values (?,?,?,?,?,?,?,?,?)", (product_ID, name, size, material, provider, product_type, reference, quantity, buy_price))
        conn.commit()

    else:
        cur.execute("select quantity from products where (product_ID = ?)", (product_ID,))
        row_headers=[x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        
        print(json_data)

        newquantity= int(json_data[0]["quantity"]) + quantity

        print(newquantity , " jasdjasjd", product_ID)

        cur.execute("update products set quantity= ? where product_ID = ?", (newquantity,product_ID))
        conn.commit()

    """materials_post

    adds one material # noqa: E501

    :param materials_id: 
    :type materials_id: int
    :param name: 
    :type name: str

    :rtype: None
    """
    return 'added to db'
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

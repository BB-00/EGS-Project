import connexion
import six
import json
import mariadb
from unicodedata import name
from flask import jsonify, request


from swagger_server.models.arrayof_providers import ArrayofProviders  # noqa: E501
from swagger_server import util
config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'egs',
    'password' : 'egs',
    'database' : 'stock_db'
}

conn = mariadb.connect(**config)

cur = conn.cursor()

providers_ID = 0;

def providers_delete():  # noqa: E501
    """providers_delete

    removes one product # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def providers_get(offset=None, limit=None, providers_id=None, name=None, address=None, email=None, site=None, phone=None):  # noqa: E501

    cur.execute("select * from providers")

    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    # return the results!
    return json.dumps(json_data)
    """providers_get

    gets all providers # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :param providers_id: Return the providers_ID
    :type providers_id: int
    :param name: Return the name of the provider
    :type name: str
    :param address: Return the address of the provider
    :type address: str
    :param email: Return the email of the provider
    :type email: str
    :param site: Return the site of the provider
    :type site: str
    :param phone: Return the phone number of the provider
    :type phone: int

    :rtype: ArrayofProviders
    """
    return 'do some magic!'


def providers_post():  # noqa: E501
    providers_ID = int(request.json["providers_ID"]) 
    name = request.json["name"]
    address = request.json["address"]
    email = request.json["email"]
    site = request.json["site"]
    phone = int(request.json["phone"])
    
    if(cur.execute("select providers_ID from providers")== None):
        providers_ID = providers_ID+1
        cur.execute("insert into providers (providers_ID, name,address,email,site,phone) values (?,?,?,?,?,?)", (providers_ID, name, address,email,site,phone))
        conn.commit()

        return
    
    return "Provider already exists"

    """materials_post

    adds one material # noqa: E501

    :param materials_id: 
    :type materials_id: int
    :param name: 
    :type name: str

    :rtype: None
    """
    return 'added to db'
    """providers_post

    adds a new provider # noqa: E501

    :param providers_id: 
    :type providers_id: int
    :param name: 
    :type name: str
    :param country: 
    :type country: str
    :param city: 
    :type city: str
    :param zip: 
    :type zip: int
    :param address: 
    :type address: str
    :param email: 
    :type email: str
    :param site: 
    :type site: str
    :param phone: 
    :type phone: int

    :rtype: None
    """
    return 'do some magic!'


from unicodedata import name
from flask import jsonify, request
import connexion
import six
import json
import mariadb

from swagger_server.models.arrayof_material import ArrayofMaterial  # noqa: E501
from swagger_server import util

config = {
    'host' : '127.0.0.1',
    'port' : 3306,
    'user' : 'resende',
    'password' : '',
    'database' : 'egs'
}

conn = mariadb.connect(**config)

cur = conn.cursor()

materials_ID=0

def materials_delete():  # noqa: E501
    """materials_delete

    removes one product # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def materials_get(offset=None, limit=None, materials_id=None, name=None):  # noqa: E501

    cur.execute("select * from materials")

    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    # return the results!
    return json.dumps(json_data)
    """materials_get

    gets all materials # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :param materials_id: Return the materials_ID
    :type materials_id: int
    :param name: Return the name of the material
    :type name: str

    :rtype: ArrayofMaterial
    """
    return 'do some magic!'


def materials_post():  # noqa: E501
    materials_ID = int(request.json["materials_ID"]) 
    name = request.json["name"]

    #if(cur.execute("select materials_id from materials")== None):
    cur.execute("insert into materials (materials_ID, name) values (?,?)", (materials_ID, name))
    conn.commit()
    conn.close()
    return
    
    return "materials id already exists"

    """materials_post

    adds one material # noqa: E501

    :param materials_id: 
    :type materials_id: int
    :param name: 
    :type name: str

    :rtype: None
    """
    return 'added to db'

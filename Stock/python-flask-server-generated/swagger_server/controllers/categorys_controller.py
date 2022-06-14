import connexion
import six
import json
import mariadb



from swagger_server.models.arrayof_category import ArrayofCategory  # noqa: E501
from swagger_server import util


def type_delete():  # noqa: E501
    """type_delete

    removes one product # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def type_get(offset=None, limit=None, type_id=None, name=None):  # noqa: E501
    config = {
        'host' : '127.0.0.1',
        'port' : 3306,
        'user' : 'resende',
        'password' : '',
        'database' : 'egs'
    }

    conn = mariadb.connect(**config)

    cur = conn.cursor()

    cur.execute("select * from type")

    row_headers=[x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data=[]
    for result in rv:
        json_data.append(dict(zip(row_headers,result)))

    # return the results!
    return json.dumps(json_data)

    """type_get

    gets type of product # noqa: E501

    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param limit: The numbers of items to return.
    :type limit: int
    :param type_id: Return the type_ID
    :type type_id: int
    :param name: Return the name of the type
    :type name: str

    :rtype: ArrayofCategory
    """
    return 'do some magic!'


def type_post(type_id, name):  # noqa: E501
    """type_post

    add a new type # noqa: E501

    :param type_id: 
    :type type_id: int
    :param name: 
    :type name: str

    :rtype: None
    """
    return 'do some magic!'

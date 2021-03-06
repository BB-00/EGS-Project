# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TypeBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type_id: int=None, name: str=None):  # noqa: E501
        """TypeBody - a model defined in Swagger

        :param type_id: The type_id of this TypeBody.  # noqa: E501
        :type type_id: int
        :param name: The name of this TypeBody.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'type_id': int,
            'name': str
        }

        self.attribute_map = {
            'type_id': 'type_ID',
            'name': 'name'
        }
        self._type_id = type_id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'TypeBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The type_body of this TypeBody.  # noqa: E501
        :rtype: TypeBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type_id(self) -> int:
        """Gets the type_id of this TypeBody.


        :return: The type_id of this TypeBody.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id: int):
        """Sets the type_id of this TypeBody.


        :param type_id: The type_id of this TypeBody.
        :type type_id: int
        """

        self._type_id = type_id

    @property
    def name(self) -> str:
        """Gets the name of this TypeBody.


        :return: The name of this TypeBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this TypeBody.


        :param name: The name of this TypeBody.
        :type name: str
        """

        self._name = name

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Article(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type_id: int=None, lim: int=None, ofset: int=None, name: str=None, quantity: int=None):  # noqa: E501
        """Article - a model defined in Swagger

        :param type_id: The type_id of this Article.  # noqa: E501
        :type type_id: int
        :param lim: The lim of this Article.  # noqa: E501
        :type lim: int
        :param ofset: The ofset of this Article.  # noqa: E501
        :type ofset: int
        :param name: The name of this Article.  # noqa: E501
        :type name: str
        :param quantity: The quantity of this Article.  # noqa: E501
        :type quantity: int
        """
        self.swagger_types = {
            'type_id': int,
            'lim': int,
            'ofset': int,
            'name': str,
            'quantity': int
        }

        self.attribute_map = {
            'type_id': 'type_ID',
            'lim': 'lim',
            'ofset': 'ofset',
            'name': 'name',
            'quantity': 'quantity'
        }
        self._type_id = type_id
        self._lim = lim
        self._ofset = ofset
        self._name = name
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt) -> 'Article':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Article of this Article.  # noqa: E501
        :rtype: Article
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type_id(self) -> int:
        """Gets the type_id of this Article.

        article id  # noqa: E501

        :return: The type_id of this Article.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id: int):
        """Sets the type_id of this Article.

        article id  # noqa: E501

        :param type_id: The type_id of this Article.
        :type type_id: int
        """

        self._type_id = type_id

    @property
    def lim(self) -> int:
        """Gets the lim of this Article.

        number of items to return  # noqa: E501

        :return: The lim of this Article.
        :rtype: int
        """
        return self._lim

    @lim.setter
    def lim(self, lim: int):
        """Sets the lim of this Article.

        number of items to return  # noqa: E501

        :param lim: The lim of this Article.
        :type lim: int
        """

        self._lim = lim

    @property
    def ofset(self) -> int:
        """Gets the ofset of this Article.

        nuumber of items to skip before starting  # noqa: E501

        :return: The ofset of this Article.
        :rtype: int
        """
        return self._ofset

    @ofset.setter
    def ofset(self, ofset: int):
        """Sets the ofset of this Article.

        nuumber of items to skip before starting  # noqa: E501

        :param ofset: The ofset of this Article.
        :type ofset: int
        """

        self._ofset = ofset

    @property
    def name(self) -> str:
        """Gets the name of this Article.

        name of article  # noqa: E501

        :return: The name of this Article.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Article.

        name of article  # noqa: E501

        :param name: The name of this Article.
        :type name: str
        """

        self._name = name

    @property
    def quantity(self) -> int:
        """Gets the quantity of this Article.

        quantity of  # noqa: E501

        :return: The quantity of this Article.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        """Sets the quantity of this Article.

        quantity of  # noqa: E501

        :param quantity: The quantity of this Article.
        :type quantity: int
        """

        self._quantity = quantity

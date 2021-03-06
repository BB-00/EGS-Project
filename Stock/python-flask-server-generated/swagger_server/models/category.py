# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Category(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, category_id: int=None, ofset: int=None, lim: int=None, name: str=None):  # noqa: E501
        """Category - a model defined in Swagger

        :param category_id: The category_id of this Category.  # noqa: E501
        :type category_id: int
        :param ofset: The ofset of this Category.  # noqa: E501
        :type ofset: int
        :param lim: The lim of this Category.  # noqa: E501
        :type lim: int
        :param name: The name of this Category.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'category_id': int,
            'ofset': int,
            'lim': int,
            'name': str
        }

        self.attribute_map = {
            'category_id': 'category_ID',
            'ofset': 'ofset',
            'lim': 'lim',
            'name': 'name'
        }
        self._category_id = category_id
        self._ofset = ofset
        self._lim = lim
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Category':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Category of this Category.  # noqa: E501
        :rtype: Category
        """
        return util.deserialize_model(dikt, cls)

    @property
    def category_id(self) -> int:
        """Gets the category_id of this Category.

        category id  # noqa: E501

        :return: The category_id of this Category.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id: int):
        """Sets the category_id of this Category.

        category id  # noqa: E501

        :param category_id: The category_id of this Category.
        :type category_id: int
        """

        self._category_id = category_id

    @property
    def ofset(self) -> int:
        """Gets the ofset of this Category.

        number of items to skip before starting  # noqa: E501

        :return: The ofset of this Category.
        :rtype: int
        """
        return self._ofset

    @ofset.setter
    def ofset(self, ofset: int):
        """Sets the ofset of this Category.

        number of items to skip before starting  # noqa: E501

        :param ofset: The ofset of this Category.
        :type ofset: int
        """

        self._ofset = ofset

    @property
    def lim(self) -> int:
        """Gets the lim of this Category.

        number of items to return  # noqa: E501

        :return: The lim of this Category.
        :rtype: int
        """
        return self._lim

    @lim.setter
    def lim(self, lim: int):
        """Sets the lim of this Category.

        number of items to return  # noqa: E501

        :param lim: The lim of this Category.
        :type lim: int
        """

        self._lim = lim

    @property
    def name(self) -> str:
        """Gets the name of this Category.

        name of the category  # noqa: E501

        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Category.

        name of the category  # noqa: E501

        :param name: The name of this Category.
        :type name: str
        """

        self._name = name

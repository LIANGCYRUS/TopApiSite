from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemAddSchemaGetRequest(BaseRequest):

    def __init__(
        self,
        category_id: int = None,
        product_id: int = None,
        type: str = None,
        isv_init: bool = None
    ):
        """
            商品发布的目标类目，必须是叶子类目
        """
        self._category_id = category_id
        """
            商品发布的目标product_id
        """
        self._product_id = product_id
        """
            发布商品类型，一口价填“b”，拍卖填"a"
        """
        self._type = type
        """
            正常接口调用时，请忽略这个参数或者填FALSE。这个参数提供给ISV对接Schema时，如果想先获取了解所有字段和规则，可以将此字段设置为true，product_id也就不需要提供了，设置为0即可
        """
        self._isv_init = isv_init

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int):
            self._category_id = category_id
        else:
            raise TypeError("category_id must be int")

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self._product_id = product_id
        else:
            raise TypeError("product_id must be int")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")

    @property
    def isv_init(self):
        return self._isv_init

    @isv_init.setter
    def isv_init(self, isv_init):
        if isinstance(isv_init, bool):
            self._isv_init = isv_init
        else:
            raise TypeError("isv_init must be bool")


    def get_api_name(self):
        return "tmall.item.add.schema.get"

    def to_dict(self):
        request_dict = {}
        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._isv_init is not None:
            request_dict["isv_init"] = convert_basic(self._isv_init)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


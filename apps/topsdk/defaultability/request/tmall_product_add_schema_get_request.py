from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallProductAddSchemaGetRequest(BaseRequest):

    def __init__(
        self,
        category_id: int = None,
        brand_id: int = None
    ):
        """
            商品发布的目标类目，必须是叶子类目
        """
        self._category_id = category_id
        """
            品牌ID
        """
        self._brand_id = brand_id

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
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        if isinstance(brand_id, int):
            self._brand_id = brand_id
        else:
            raise TypeError("brand_id must be int")


    def get_api_name(self):
        return "tmall.product.add.schema.get"

    def to_dict(self):
        request_dict = {}
        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._brand_id is not None:
            request_dict["brand_id"] = convert_basic(self._brand_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


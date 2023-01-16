from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoShopSellerGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None
    ):
        """
            需返回的字段列表。可选值：Shop 结构中的所有字段；多个字段之间用逗号(,)分隔
        """
        self._fields = fields

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")


    def get_api_name(self):
        return "taobao.shop.seller.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


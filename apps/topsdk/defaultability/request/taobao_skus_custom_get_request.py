from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSkusCustomGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        outer_id: str = None
    ):
        """
            需返回的字段列表。可选值：Sku结构体中的所有字段；字段之间用“,”隔开
        """
        self._fields = fields
        """
            Sku的外部商家ID
        """
        self._outer_id = outer_id

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")

    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")


    def get_api_name(self):
        return "taobao.skus.custom.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


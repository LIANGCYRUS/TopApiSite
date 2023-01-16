from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemSkusGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        num_iids: list = None
    ):
        """
            需返回的字段列表。可选值：Sku结构体中的所有字段；字段之间用“,”分隔。
        """
        self._fields = fields
        """
            sku所属商品数字id，必选。num_iid个数不能超过40个
        """
        self._num_iids = num_iids

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
    def num_iids(self):
        return self._num_iids

    @num_iids.setter
    def num_iids(self, num_iids):
        if isinstance(num_iids, list):
            self._num_iids = num_iids
        else:
            raise TypeError("num_iids must be list")


    def get_api_name(self):
        return "taobao.item.skus.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._num_iids is not None:
            request_dict["num_iids"] = convert_basic_list(self._num_iids)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


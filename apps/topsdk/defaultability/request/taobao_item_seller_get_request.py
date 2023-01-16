from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemSellerGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        num_iid: int = None
    ):
        """
            需要返回的商品字段列表。可选值：Item商品结构体中所有字段均可返回，多个字段用“,”分隔。
        """
        self._fields = fields
        """
            商品数字ID
        """
        self._num_iid = num_iid

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
    def num_iid(self):
        return self._num_iid

    @num_iid.setter
    def num_iid(self, num_iid):
        if isinstance(num_iid, int):
            self._num_iid = num_iid
        else:
            raise TypeError("num_iid must be int")


    def get_api_name(self):
        return "taobao.item.seller.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


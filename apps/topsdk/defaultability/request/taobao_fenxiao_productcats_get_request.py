from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductcatsGetRequest(BaseRequest):

    def __init__(
        self,
        fields: str = None
    ):
        """
            返回字段列表
        """
        self._fields = fields

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, str):
            self._fields = fields
        else:
            raise TypeError("fields must be str")


    def get_api_name(self):
        return "taobao.fenxiao.productcats.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


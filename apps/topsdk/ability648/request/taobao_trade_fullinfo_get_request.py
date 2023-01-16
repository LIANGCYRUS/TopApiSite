from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradeFullinfoGetRequest(BaseRequest):

    def __init__(
        self,
        include_oaid: str = None,
        fields: list = None,
        tid: int = None
    ):
        """
            include_oaid
        """
        self._include_oaid = include_oaid
        """
            需要返回的字段列表，多个字段用半角逗号分隔，可选值为返回示例中能看到的所有字段。
        """
        self._fields = fields
        """
            交易编号
        """
        self._tid = tid

    @property
    def include_oaid(self):
        return self._include_oaid

    @include_oaid.setter
    def include_oaid(self, include_oaid):
        if isinstance(include_oaid, str):
            self._include_oaid = include_oaid
        else:
            raise TypeError("include_oaid must be str")

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
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, int):
            self._tid = tid
        else:
            raise TypeError("tid must be int")


    def get_api_name(self):
        return "taobao.trade.fullinfo.get"

    def to_dict(self):
        request_dict = {}
        if self._include_oaid is not None:
            request_dict["include_oaid"] = convert_basic(self._include_oaid)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


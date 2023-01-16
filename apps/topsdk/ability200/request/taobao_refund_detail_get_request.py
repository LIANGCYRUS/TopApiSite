from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRefundDetailGetRequest(BaseRequest):

    def __init__(
        self,
        refund_id: int = None,
        fields: list = None
    ):
        """
            退款编号
        """
        self._refund_id = refund_id
        """
            需要返回的字段。目前支持有：allowedOperations,refund_version
        """
        self._fields = fields

    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        if isinstance(refund_id, int):
            self._refund_id = refund_id
        else:
            raise TypeError("refund_id must be int")

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
        return "taobao.refund.detail.get"

    def to_dict(self):
        request_dict = {}
        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


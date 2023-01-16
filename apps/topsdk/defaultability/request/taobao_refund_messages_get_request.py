from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRefundMessagesGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        page_no: int = None,
        page_size: int = None,
        refund_id: int = None,
        refund_phase: str = None
    ):
        """
            需返回的字段列表。可选值：RefundMessage结构体中的所有字段，以半角逗号(,)分隔。
        """
        self._fields = fields
        """
            页码
        """
        self._page_no = page_no
        """
            每页条数
        """
        self._page_size = page_size
        """
            退款单号
        """
        self._refund_id = refund_id
        """
            退款阶段，可选值：onsale（售中），aftersale（售后），天猫退款为必传。
        """
        self._refund_phase = refund_phase

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

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
    def refund_phase(self):
        return self._refund_phase

    @refund_phase.setter
    def refund_phase(self, refund_phase):
        if isinstance(refund_phase, str):
            self._refund_phase = refund_phase
        else:
            raise TypeError("refund_phase must be str")


    def get_api_name(self):
        return "taobao.refund.messages.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._refund_phase is not None:
            request_dict["refund_phase"] = convert_basic(self._refund_phase)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


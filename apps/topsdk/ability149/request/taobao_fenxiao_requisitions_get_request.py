from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoRequisitionsGetRequest(BaseRequest):

    def __init__(
        self,
        status: int = None,
        apply_start: datetime = None,
        apply_end: datetime = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            申请状态（1-申请中、2-成功、3-被退回、4-已撤消、5-过期）
        """
        self._status = status
        """
            申请开始时间yyyy-MM-dd
        """
        self._apply_start = apply_start
        """
            申请结束时间yyyy-MM-dd
        """
        self._apply_end = apply_end
        """
            页码（大于0的整数，默认1）
        """
        self._page_no = page_no
        """
            每页记录数（默认20，最大50）
        """
        self._page_size = page_size

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, int):
            self._status = status
        else:
            raise TypeError("status must be int")

    @property
    def apply_start(self):
        return self._apply_start

    @apply_start.setter
    def apply_start(self, apply_start):
        if isinstance(apply_start, datetime):
            self._apply_start = apply_start
        else:
            raise TypeError("apply_start must be datetime")

    @property
    def apply_end(self):
        return self._apply_end

    @apply_end.setter
    def apply_end(self, apply_end):
        if isinstance(apply_end, datetime):
            self._apply_end = apply_end
        else:
            raise TypeError("apply_end must be datetime")

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


    def get_api_name(self):
        return "taobao.fenxiao.requisitions.get"

    def to_dict(self):
        request_dict = {}
        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._apply_start is not None:
            request_dict["apply_start"] = convert_basic(self._apply_start)

        if self._apply_end is not None:
            request_dict["apply_end"] = convert_basic(self._apply_end)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


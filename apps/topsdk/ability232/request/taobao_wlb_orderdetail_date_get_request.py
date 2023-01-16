from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderdetailDateGetRequest(BaseRequest):

    def __init__(
        self,
        start_time: datetime = None,
        end_time: datetime = None,
        page_size: int = None,
        page_no: int = None
    ):
        """
            创建时间起始
        """
        self._start_time = start_time
        """
            创建时间结束
        """
        self._end_time = end_time
        """
            分页大小
        """
        self._page_size = page_size
        """
            分页下标
        """
        self._page_no = page_no

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if isinstance(start_time, datetime):
            self._start_time = start_time
        else:
            raise TypeError("start_time must be datetime")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        if isinstance(end_time, datetime):
            self._end_time = end_time
        else:
            raise TypeError("end_time must be datetime")

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")


    def get_api_name(self):
        return "taobao.wlb.orderdetail.date.get"

    def to_dict(self):
        request_dict = {}
        if self._start_time is not None:
            request_dict["start_time"] = convert_basic(self._start_time)

        if self._end_time is not None:
            request_dict["end_time"] = convert_basic(self._end_time)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


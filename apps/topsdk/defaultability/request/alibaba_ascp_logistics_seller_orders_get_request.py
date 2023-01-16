from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaAscpLogisticsSellerOrdersGetRequest(BaseRequest):

    def __init__(
        self,
        write_off_date: str = None,
        page_index: int = None,
        receive_code: str = None,
        page_size: int = None,
        tid: str = None,
        write_off_status: str = None
    ):
        """
            核销日期
        """
        self._write_off_date = write_off_date
        """
            分页索引
        """
        self._page_index = page_index
        """
            收货码
        """
        self._receive_code = receive_code
        """
            分页大小
        """
        self._page_size = page_size
        """
            淘系交易id
        """
        self._tid = tid
        """
            1代表未核销，2代表已核销
        """
        self._write_off_status = write_off_status

    @property
    def write_off_date(self):
        return self._write_off_date

    @write_off_date.setter
    def write_off_date(self, write_off_date):
        if isinstance(write_off_date, str):
            self._write_off_date = write_off_date
        else:
            raise TypeError("write_off_date must be str")

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        if isinstance(page_index, int):
            self._page_index = page_index
        else:
            raise TypeError("page_index must be int")

    @property
    def receive_code(self):
        return self._receive_code

    @receive_code.setter
    def receive_code(self, receive_code):
        if isinstance(receive_code, str):
            self._receive_code = receive_code
        else:
            raise TypeError("receive_code must be str")

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
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, str):
            self._tid = tid
        else:
            raise TypeError("tid must be str")

    @property
    def write_off_status(self):
        return self._write_off_status

    @write_off_status.setter
    def write_off_status(self, write_off_status):
        if isinstance(write_off_status, str):
            self._write_off_status = write_off_status
        else:
            raise TypeError("write_off_status must be str")


    def get_api_name(self):
        return "alibaba.ascp.logistics.seller.orders.get"

    def to_dict(self):
        request_dict = {}
        if self._write_off_date is not None:
            request_dict["write_off_date"] = convert_basic(self._write_off_date)

        if self._page_index is not None:
            request_dict["page_index"] = convert_basic(self._page_index)

        if self._receive_code is not None:
            request_dict["receive_code"] = convert_basic(self._receive_code)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._write_off_status is not None:
            request_dict["write_off_status"] = convert_basic(self._write_off_status)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


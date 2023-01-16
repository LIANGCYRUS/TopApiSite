from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbNotifyMessagePageGetRequest(BaseRequest):

    def __init__(
        self,
        msg_code: str = None,
        page_no: int = None,
        page_size: int = None,
        start_date: datetime = None,
        end_date: datetime = None,
        status: str = None
    ):
        """
            通知消息编码： STOCK_IN_NOT_CONSISTENT---入库单不一致 CANCEL_ORDER_SUCCESS---取消订单成功 INVENTORY_CHECK---盘点 CANCEL_ORDER_FAILURE---取消订单失败 ORDER_REJECT--wms拒单 ORDER_CONFIRMED--订单处理成功
        """
        self._msg_code = msg_code
        """
            分页查询页数
        """
        self._page_no = page_no
        """
            分页查询的每页页数
        """
        self._page_size = page_size
        """
            记录开始时间
        """
        self._start_date = start_date
        """
            记录截至时间
        """
        self._end_date = end_date
        """
            消息状态： 不需要确认：NO_NEED_CONFIRM 已确认：CONFIRMED 待确认：TO_BE_CONFIRM
        """
        self._status = status

    @property
    def msg_code(self):
        return self._msg_code

    @msg_code.setter
    def msg_code(self, msg_code):
        if isinstance(msg_code, str):
            self._msg_code = msg_code
        else:
            raise TypeError("msg_code must be str")

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
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, datetime):
            self._start_date = start_date
        else:
            raise TypeError("start_date must be datetime")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, datetime):
            self._end_date = end_date
        else:
            raise TypeError("end_date must be datetime")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")


    def get_api_name(self):
        return "taobao.wlb.notify.message.page.get"

    def to_dict(self):
        request_dict = {}
        if self._msg_code is not None:
            request_dict["msg_code"] = convert_basic(self._msg_code)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._start_date is not None:
            request_dict["start_date"] = convert_basic(self._start_date)

        if self._end_date is not None:
            request_dict["end_date"] = convert_basic(self._end_date)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


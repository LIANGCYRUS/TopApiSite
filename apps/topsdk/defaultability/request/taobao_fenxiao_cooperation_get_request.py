from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoCooperationGetRequest(BaseRequest):

    def __init__(
        self,
        status: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
        trade_type: str = None,
        page_no: int = None,
        page_size: int = None,
        channel_code: str = None,
        role_type: int = None
    ):
        """
            合作状态： NORMAL(合作中)、 ENDING(终止中) 、END (终止)
        """
        self._status = status
        """
            合作开始时间yyyy-MM-dd HH:mm:ss
        """
        self._start_date = start_date
        """
            合作结束时间yyyy-MM-dd HH:mm:ss
        """
        self._end_date = end_date
        """
            分销方式：AGENT(代销) 、DEALER（经销）
        """
        self._trade_type = trade_type
        """
            页码（大于0的整数，默认1）
        """
        self._page_no = page_no
        """
            每页记录数（默认20，最大50）
        """
        self._page_size = page_size
        """
            渠道code
        """
        self._channel_code = channel_code
        """
            1是供应商，2 是分销商
        """
        self._role_type = role_type

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")

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
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        if isinstance(trade_type, str):
            self._trade_type = trade_type
        else:
            raise TypeError("trade_type must be str")

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
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, channel_code):
        if isinstance(channel_code, str):
            self._channel_code = channel_code
        else:
            raise TypeError("channel_code must be str")

    @property
    def role_type(self):
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        if isinstance(role_type, int):
            self._role_type = role_type
        else:
            raise TypeError("role_type must be int")


    def get_api_name(self):
        return "taobao.fenxiao.cooperation.get"

    def to_dict(self):
        request_dict = {}
        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._start_date is not None:
            request_dict["start_date"] = convert_basic(self._start_date)

        if self._end_date is not None:
            request_dict["end_date"] = convert_basic(self._end_date)

        if self._trade_type is not None:
            request_dict["trade_type"] = convert_basic(self._trade_type)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._channel_code is not None:
            request_dict["channel_code"] = convert_basic(self._channel_code)

        if self._role_type is not None:
            request_dict["role_type"] = convert_basic(self._role_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


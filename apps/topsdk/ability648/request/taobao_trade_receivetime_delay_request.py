from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradeReceivetimeDelayRequest(BaseRequest):

    def __init__(
        self,
        tid: int = None,
        days: int = None
    ):
        """
            主订单号
        """
        self._tid = tid
        """
            延长收货的天数，可选值为：3, 5, 7, 10。
        """
        self._days = days

    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, int):
            self._tid = tid
        else:
            raise TypeError("tid must be int")

    @property
    def days(self):
        return self._days

    @days.setter
    def days(self, days):
        if isinstance(days, int):
            self._days = days
        else:
            raise TypeError("days must be int")


    def get_api_name(self):
        return "taobao.trade.receivetime.delay"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._days is not None:
            request_dict["days"] = convert_basic(self._days)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


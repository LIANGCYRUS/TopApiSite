from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsTraceSearchRequest(BaseRequest):

    def __init__(
        self,
        tid: int = None,
        is_split: int = None,
        sub_tid: list = None
    ):
        """
            淘宝交易号，请勿传非淘宝交易号
        """
        self._tid = tid
        """
            表明是否是拆单，默认值0，1表示拆单
        """
        self._is_split = is_split
        """
            拆单子订单列表，当is_split=1时，需要传人；对应的数据是：子订单号的列表。
        """
        self._sub_tid = sub_tid

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
    def is_split(self):
        return self._is_split

    @is_split.setter
    def is_split(self, is_split):
        if isinstance(is_split, int):
            self._is_split = is_split
        else:
            raise TypeError("is_split must be int")

    @property
    def sub_tid(self):
        return self._sub_tid

    @sub_tid.setter
    def sub_tid(self, sub_tid):
        if isinstance(sub_tid, list):
            self._sub_tid = sub_tid
        else:
            raise TypeError("sub_tid must be list")


    def get_api_name(self):
        return "taobao.logistics.trace.search"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._is_split is not None:
            request_dict["is_split"] = convert_basic(self._is_split)

        if self._sub_tid is not None:
            request_dict["sub_tid"] = convert_basic_list(self._sub_tid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


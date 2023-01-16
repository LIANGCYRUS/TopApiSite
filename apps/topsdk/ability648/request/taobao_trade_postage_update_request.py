from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradePostageUpdateRequest(BaseRequest):

    def __init__(
        self,
        tid: int = None,
        post_fee: str = None
    ):
        """
            主订单编号
        """
        self._tid = tid
        """
            邮费价格(邮费单位是元）
        """
        self._post_fee = post_fee

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
    def post_fee(self):
        return self._post_fee

    @post_fee.setter
    def post_fee(self, post_fee):
        if isinstance(post_fee, str):
            self._post_fee = post_fee
        else:
            raise TypeError("post_fee must be str")


    def get_api_name(self):
        return "taobao.trade.postage.update"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._post_fee is not None:
            request_dict["post_fee"] = convert_basic(self._post_fee)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


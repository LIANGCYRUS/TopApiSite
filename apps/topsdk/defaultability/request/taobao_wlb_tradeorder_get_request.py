from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbTradeorderGetRequest(BaseRequest):

    def __init__(
        self,
        trade_type: str = None,
        sub_trade_id: str = None,
        trade_id: str = None
    ):
        """
            交易类型: TAOBAO--淘宝交易 OTHER_TRADE--其它交易
        """
        self._trade_type = trade_type
        """
            子交易号
        """
        self._sub_trade_id = sub_trade_id
        """
            指定交易类型的交易号
        """
        self._trade_id = trade_id

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
    def sub_trade_id(self):
        return self._sub_trade_id

    @sub_trade_id.setter
    def sub_trade_id(self, sub_trade_id):
        if isinstance(sub_trade_id, str):
            self._sub_trade_id = sub_trade_id
        else:
            raise TypeError("sub_trade_id must be str")

    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        if isinstance(trade_id, str):
            self._trade_id = trade_id
        else:
            raise TypeError("trade_id must be str")


    def get_api_name(self):
        return "taobao.wlb.tradeorder.get"

    def to_dict(self):
        request_dict = {}
        if self._trade_type is not None:
            request_dict["trade_type"] = convert_basic(self._trade_type)

        if self._sub_trade_id is not None:
            request_dict["sub_trade_id"] = convert_basic(self._sub_trade_id)

        if self._trade_id is not None:
            request_dict["trade_id"] = convert_basic(self._trade_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


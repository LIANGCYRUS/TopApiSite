from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class CainiaoBimTradeorderConsignRequest(BaseRequest):

    def __init__(
        self,
        trade_id: str = None,
        store_code: str = None,
        res_id: str = None
    ):
        """
            交易单号
        """
        self._trade_id = trade_id
        """
            仓储编码，ERP指定仓库发货时需要传值，编码由菜鸟提供
        """
        self._store_code = store_code
        """
            选择的线路ID非必填字段
        """
        self._res_id = res_id

    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        if isinstance(trade_id, str):
            self._trade_id = trade_id
        else:
            raise TypeError("trade_id must be str")

    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, store_code):
        if isinstance(store_code, str):
            self._store_code = store_code
        else:
            raise TypeError("store_code must be str")

    @property
    def res_id(self):
        return self._res_id

    @res_id.setter
    def res_id(self, res_id):
        if isinstance(res_id, str):
            self._res_id = res_id
        else:
            raise TypeError("res_id must be str")


    def get_api_name(self):
        return "cainiao.bim.tradeorder.consign"

    def to_dict(self):
        request_dict = {}
        if self._trade_id is not None:
            request_dict["trade_id"] = convert_basic(self._trade_id)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._res_id is not None:
            request_dict["res_id"] = convert_basic(self._res_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsSnInfoQueryRequest(BaseRequest):

    def __init__(
        self,
        order_code: str = None,
        order_code_type: int = None,
        page_index: int = None
    ):
        """
            订单编码
        """
        self._order_code = order_code
        """
            订单类型（1:仓配订单 10：配送扫码 20：增值扫码 40:ERP单号; 50：交易订单 ）
        """
        self._order_code_type = order_code_type
        """
            页数，默认每页50条
        """
        self._page_index = page_index

    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        if isinstance(order_code, str):
            self._order_code = order_code
        else:
            raise TypeError("order_code must be str")

    @property
    def order_code_type(self):
        return self._order_code_type

    @order_code_type.setter
    def order_code_type(self, order_code_type):
        if isinstance(order_code_type, int):
            self._order_code_type = order_code_type
        else:
            raise TypeError("order_code_type must be int")

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        if isinstance(page_index, int):
            self._page_index = page_index
        else:
            raise TypeError("page_index must be int")


    def get_api_name(self):
        return "taobao.wlb.wms.sn.info.query"

    def to_dict(self):
        request_dict = {}
        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._order_code_type is not None:
            request_dict["order_code_type"] = convert_basic(self._order_code_type)

        if self._page_index is not None:
            request_dict["page_index"] = convert_basic(self._page_index)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


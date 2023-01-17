from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportsWaybillGetRequest(BaseRequest):

    def __init__(
        self,
        order_code: str = None
    ):
        """
            物流订单号
        """
        self._order_code = order_code

    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        if isinstance(order_code, str):
            self._order_code = order_code
        else:
            raise TypeError("order_code must be str")


    def get_api_name(self):
        return "taobao.wlb.imports.waybill.get"

    def to_dict(self):
        request_dict = {}
        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


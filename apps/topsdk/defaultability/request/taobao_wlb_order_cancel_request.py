from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderCancelRequest(BaseRequest):

    def __init__(
        self,
        wlb_order_code: str = None
    ):
        """
            物流宝订单编号
        """
        self._wlb_order_code = wlb_order_code

    @property
    def wlb_order_code(self):
        return self._wlb_order_code

    @wlb_order_code.setter
    def wlb_order_code(self, wlb_order_code):
        if isinstance(wlb_order_code, str):
            self._wlb_order_code = wlb_order_code
        else:
            raise TypeError("wlb_order_code must be str")


    def get_api_name(self):
        return "taobao.wlb.order.cancel"

    def to_dict(self):
        request_dict = {}
        if self._wlb_order_code is not None:
            request_dict["wlb_order_code"] = convert_basic(self._wlb_order_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


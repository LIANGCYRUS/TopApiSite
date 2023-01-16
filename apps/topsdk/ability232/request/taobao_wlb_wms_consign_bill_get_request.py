from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsConsignBillGetRequest(BaseRequest):

    def __init__(
        self,
        cn_order_code: str = None,
        order_code: str = None
    ):
        """
            菜鸟订单编码,cnOrderCode与orderCode必须有一个值不可为空
        """
        self._cn_order_code = cn_order_code
        """
            ERP订单编码,cnOrderCode与orderCode必须有一个值不可为空
        """
        self._order_code = order_code

    @property
    def cn_order_code(self):
        return self._cn_order_code

    @cn_order_code.setter
    def cn_order_code(self, cn_order_code):
        if isinstance(cn_order_code, str):
            self._cn_order_code = cn_order_code
        else:
            raise TypeError("cn_order_code must be str")

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
        return "taobao.wlb.wms.consign.bill.get"

    def to_dict(self):
        request_dict = {}
        if self._cn_order_code is not None:
            request_dict["cn_order_code"] = convert_basic(self._cn_order_code)

        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


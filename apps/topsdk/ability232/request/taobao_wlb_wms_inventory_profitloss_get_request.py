from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsInventoryProfitlossGetRequest(BaseRequest):

    def __init__(
        self,
        cn_order_code: str = None
    ):
        """
            菜鸟订单编码
        """
        self._cn_order_code = cn_order_code

    @property
    def cn_order_code(self):
        return self._cn_order_code

    @cn_order_code.setter
    def cn_order_code(self, cn_order_code):
        if isinstance(cn_order_code, str):
            self._cn_order_code = cn_order_code
        else:
            raise TypeError("cn_order_code must be str")


    def get_api_name(self):
        return "taobao.wlb.wms.inventory.profitloss.get"

    def to_dict(self):
        request_dict = {}
        if self._cn_order_code is not None:
            request_dict["cn_order_code"] = convert_basic(self._cn_order_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


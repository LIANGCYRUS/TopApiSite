from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportsVasIdentityResultRequest(BaseRequest):

    def __init__(
        self,
        lg_order_code: str = None
    ):
        """
            物流订单编号
        """
        self._lg_order_code = lg_order_code

    @property
    def lg_order_code(self):
        return self._lg_order_code

    @lg_order_code.setter
    def lg_order_code(self, lg_order_code):
        if isinstance(lg_order_code, str):
            self._lg_order_code = lg_order_code
        else:
            raise TypeError("lg_order_code must be str")


    def get_api_name(self):
        return "taobao.wlb.imports.vas.identity.result"

    def to_dict(self):
        request_dict = {}
        if self._lg_order_code is not None:
            request_dict["lg_order_code"] = convert_basic(self._lg_order_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


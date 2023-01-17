from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportsOrderCancelRequest(BaseRequest):

    def __init__(
        self,
        lgorder_code: str = None
    ):
        """
            物流订单编号
        """
        self._lgorder_code = lgorder_code

    @property
    def lgorder_code(self):
        return self._lgorder_code

    @lgorder_code.setter
    def lgorder_code(self, lgorder_code):
        if isinstance(lgorder_code, str):
            self._lgorder_code = lgorder_code
        else:
            raise TypeError("lgorder_code must be str")


    def get_api_name(self):
        return "taobao.wlb.imports.order.cancel"

    def to_dict(self):
        request_dict = {}
        if self._lgorder_code is not None:
            request_dict["lgorder_code"] = convert_basic(self._lgorder_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoScitemOutercodeGetRequest(BaseRequest):

    def __init__(
        self,
        outer_code: str = None
    ):
        """
            商品编码
        """
        self._outer_code = outer_code

    @property
    def outer_code(self):
        return self._outer_code

    @outer_code.setter
    def outer_code(self, outer_code):
        if isinstance(outer_code, str):
            self._outer_code = outer_code
        else:
            raise TypeError("outer_code must be str")


    def get_api_name(self):
        return "taobao.scitem.outercode.get"

    def to_dict(self):
        request_dict = {}
        if self._outer_code is not None:
            request_dict["outer_code"] = convert_basic(self._outer_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductcatDeleteRequest(BaseRequest):

    def __init__(
        self,
        product_line_id: int = None
    ):
        """
            产品线ID
        """
        self._product_line_id = product_line_id

    @property
    def product_line_id(self):
        return self._product_line_id

    @product_line_id.setter
    def product_line_id(self, product_line_id):
        if isinstance(product_line_id, int):
            self._product_line_id = product_line_id
        else:
            raise TypeError("product_line_id must be int")


    def get_api_name(self):
        return "taobao.fenxiao.productcat.delete"

    def to_dict(self):
        request_dict = {}
        if self._product_line_id is not None:
            request_dict["product_line_id"] = convert_basic(self._product_line_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


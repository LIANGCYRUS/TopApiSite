from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderitemPageGetRequest(BaseRequest):

    def __init__(
        self,
        order_code: str = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            物流宝订单编码
        """
        self._order_code = order_code
        """
            分页查询参数，指定查询页数，默认为1
        """
        self._page_no = page_no
        """
            分页查询参数，每页查询数量，默认20，最大值50,大于50时按照50条查询
        """
        self._page_size = page_size

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")


    def get_api_name(self):
        return "taobao.wlb.orderitem.page.get"

    def to_dict(self):
        request_dict = {}
        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


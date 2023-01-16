from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderPageGetRequest(BaseRequest):

    def __init__(
        self,
        order_type: str = None,
        order_sub_type: str = None,
        page_size: int = None,
        page_no: int = None,
        order_status: int = None,
        order_code: str = None,
        end_time: datetime = None,
        start_time: datetime = None
    ):
        """
            订单类型: （1）NORMAL_OUT ：正常出库 （2）NORMAL_IN：正常入库 （3）RETURN_IN：退货入库 （4）EXCHANGE_OUT：换货出库
        """
        self._order_type = order_type
        """
            订单子类型： （1）OTHER： 其他 （2）TAOBAO_TRADE： 淘宝交易 （3）OTHER_TRADE：其他交易 （4）ALLCOATE： 调拨 （5）CHECK: 盘点单 （6）PURCHASE: 采购单
        """
        self._order_sub_type = order_sub_type
        """
            每页多少条
        """
        self._page_size = page_size
        """
            分页的第几页
        """
        self._page_no = page_no
        """
            TMS拒签：-100 接收方拒签：-200
        """
        self._order_status = order_status
        """
            物流订单编号
        """
        self._order_code = order_code
        """
            查询截止时间
        """
        self._end_time = end_time
        """
            查询开始时间
        """
        self._start_time = start_time

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, str):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be str")

    @property
    def order_sub_type(self):
        return self._order_sub_type

    @order_sub_type.setter
    def order_sub_type(self, order_sub_type):
        if isinstance(order_sub_type, str):
            self._order_sub_type = order_sub_type
        else:
            raise TypeError("order_sub_type must be str")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

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
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        if isinstance(order_status, int):
            self._order_status = order_status
        else:
            raise TypeError("order_status must be int")

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
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        if isinstance(end_time, datetime):
            self._end_time = end_time
        else:
            raise TypeError("end_time must be datetime")

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if isinstance(start_time, datetime):
            self._start_time = start_time
        else:
            raise TypeError("start_time must be datetime")


    def get_api_name(self):
        return "taobao.wlb.order.page.get"

    def to_dict(self):
        request_dict = {}
        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._order_sub_type is not None:
            request_dict["order_sub_type"] = convert_basic(self._order_sub_type)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._order_status is not None:
            request_dict["order_status"] = convert_basic(self._order_status)

        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._end_time is not None:
            request_dict["end_time"] = convert_basic(self._end_time)

        if self._start_time is not None:
            request_dict["start_time"] = convert_basic(self._start_time)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


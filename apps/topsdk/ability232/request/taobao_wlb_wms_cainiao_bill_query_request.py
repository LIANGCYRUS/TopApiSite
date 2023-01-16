from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsCainiaoBillQueryRequest(BaseRequest):

    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        order_type: str = None,
        end_modified_time: datetime = None,
        start_modified_time: datetime = None
    ):
        """
            每页条数。（每页条数不超过50条。默认为50）
        """
        self._page_size = page_size
        """
            页码。（大于0的整数。默认为1）
        """
        self._page_no = page_no
        """
            订单类型 201 销售出库 501 退货入库 502 换货出库 503 补发出库904 普通入库 903 普通出库单 306 B2B入库单 305 B2B出库单 601 采购入库 901 退供出库单 701 盘点出库 702 盘点入库 711 库存异动单
        """
        self._order_type = order_type
        """
            起始时间，此字段检索订单最后修改时间， 格式 yyyy-MM-dd HH:mm:ss。
        """
        self._end_modified_time = end_modified_time
        """
            结束时间，此字段检索订单最后修改时间， 格式 yyyy-MM-dd HH:mm:ss。
        """
        self._start_modified_time = start_modified_time

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
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, str):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be str")

    @property
    def end_modified_time(self):
        return self._end_modified_time

    @end_modified_time.setter
    def end_modified_time(self, end_modified_time):
        if isinstance(end_modified_time, datetime):
            self._end_modified_time = end_modified_time
        else:
            raise TypeError("end_modified_time must be datetime")

    @property
    def start_modified_time(self):
        return self._start_modified_time

    @start_modified_time.setter
    def start_modified_time(self, start_modified_time):
        if isinstance(start_modified_time, datetime):
            self._start_modified_time = start_modified_time
        else:
            raise TypeError("start_modified_time must be datetime")


    def get_api_name(self):
        return "taobao.wlb.wms.cainiao.bill.query"

    def to_dict(self):
        request_dict = {}
        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._end_modified_time is not None:
            request_dict["end_modified_time"] = convert_basic(self._end_modified_time)

        if self._start_modified_time is not None:
            request_dict["start_modified_time"] = convert_basic(self._start_modified_time)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsOrderCancelNotifyRequest(BaseRequest):

    def __init__(
        self,
        order_code: str = None,
        order_type: str = None,
        store_code: str = None
    ):
        """
            订单类型
        """
        self._order_code = order_code
        """
            单据类型 601普通入库单、501销退入库单、302 调拨入库单、904其他入库单、301 调拨出库单、901普通出库单、903 其他出库单、201 一般交易出库单 202 B2B交易出库单 502 换货出库单 503 补发出库单、1102 仓内加工作业单、 701 盘亏单、702盘盈单、711 库存状态调整单
        """
        self._order_type = order_type
        """
            仓库编码
        """
        self._store_code = store_code

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
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, str):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be str")

    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, store_code):
        if isinstance(store_code, str):
            self._store_code = store_code
        else:
            raise TypeError("store_code must be str")


    def get_api_name(self):
        return "taobao.wlb.wms.order.cancel.notify"

    def to_dict(self):
        request_dict = {}
        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


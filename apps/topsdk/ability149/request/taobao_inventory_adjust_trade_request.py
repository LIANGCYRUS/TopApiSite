from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoInventoryAdjustTradeRequest(BaseRequest):

    def __init__(
        self,
        tb_order_type: str = None,
        operate_time: datetime = None,
        biz_unique_code: str = None,
        items: str = None
    ):
        """
            订单类型：B2C、B2B
        """
        self._tb_order_type = tb_order_type
        """
            业务操作时间
        """
        self._operate_time = operate_time
        """
            商家外部定单号
        """
        self._biz_unique_code = biz_unique_code
        """
            商品初始库存信息： [{ "TBOrderCode”:”淘宝交易号”,"TBSubOrderCode ":"淘宝子交易单号,赠品可以不填","”isGift”:”TRUE或者FALSE,是否赠品”,storeCode":"商家仓库编码"," scItemId ":"商品后端ID","scItemCode":"商品商家编码"," originScItemId ":"原商品ID","inventoryType":"","quantity":"111","isComplete":"TRUE或者FALSE，是否全部确认出库"}]
        """
        self._items = items

    @property
    def tb_order_type(self):
        return self._tb_order_type

    @tb_order_type.setter
    def tb_order_type(self, tb_order_type):
        if isinstance(tb_order_type, str):
            self._tb_order_type = tb_order_type
        else:
            raise TypeError("tb_order_type must be str")

    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        if isinstance(operate_time, datetime):
            self._operate_time = operate_time
        else:
            raise TypeError("operate_time must be datetime")

    @property
    def biz_unique_code(self):
        return self._biz_unique_code

    @biz_unique_code.setter
    def biz_unique_code(self, biz_unique_code):
        if isinstance(biz_unique_code, str):
            self._biz_unique_code = biz_unique_code
        else:
            raise TypeError("biz_unique_code must be str")

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        if isinstance(items, str):
            self._items = items
        else:
            raise TypeError("items must be str")


    def get_api_name(self):
        return "taobao.inventory.adjust.trade"

    def to_dict(self):
        request_dict = {}
        if self._tb_order_type is not None:
            request_dict["tb_order_type"] = convert_basic(self._tb_order_type)

        if self._operate_time is not None:
            request_dict["operate_time"] = convert_basic(self._operate_time)

        if self._biz_unique_code is not None:
            request_dict["biz_unique_code"] = convert_basic(self._biz_unique_code)

        if self._items is not None:
            request_dict["items"] = convert_basic(self._items)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


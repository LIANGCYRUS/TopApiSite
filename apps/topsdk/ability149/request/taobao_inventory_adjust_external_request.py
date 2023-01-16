from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoInventoryAdjustExternalRequest(BaseRequest):

    def __init__(
        self,
        biz_unique_code: str = None,
        occupy_operate_code: str = None,
        operate_type: str = None,
        biz_type: str = None,
        operate_time: str = None,
        store_code: str = None,
        items: str = None,
        reduce_type: str = None
    ):
        """
            商家外部定单号
        """
        self._biz_unique_code = biz_unique_code
        """
            库存占用返回的操作码.operate_type 为OUTBOUND时，如果是确认事先进行过的库存占用，需要传入当时返回的操作码，并且明细必须与申请时保持一致
        """
        self._occupy_operate_code = occupy_operate_code
        """
            test
        """
        self._operate_type = operate_type
        """
            外部订单类型, BALANCE:盘点、NON_TAOBAO_TRADE:非淘宝交易、ALLOCATE:调拨、OTHERS:其他
        """
        self._biz_type = biz_type
        """
            业务操作时间
        """
        self._operate_time = operate_time
        """
            商家仓库编码
        """
        self._store_code = store_code
        """
            商品初始库存信息： [{"scItemId":"商品后端ID，如果有传scItemCode,参数可以为0","scItemCode":"商品商家编码","inventoryType":"库存类型  1：正常,”direction”: 1: 盘盈 -1: 盘亏,参数可选,"quantity":"数量(正数)"}]
        """
        self._items = items
        """
            test
        """
        self._reduce_type = reduce_type

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
    def occupy_operate_code(self):
        return self._occupy_operate_code

    @occupy_operate_code.setter
    def occupy_operate_code(self, occupy_operate_code):
        if isinstance(occupy_operate_code, str):
            self._occupy_operate_code = occupy_operate_code
        else:
            raise TypeError("occupy_operate_code must be str")

    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        if isinstance(operate_type, str):
            self._operate_type = operate_type
        else:
            raise TypeError("operate_type must be str")

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, str):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be str")

    @property
    def operate_time(self):
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        if isinstance(operate_time, str):
            self._operate_time = operate_time
        else:
            raise TypeError("operate_time must be str")

    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, store_code):
        if isinstance(store_code, str):
            self._store_code = store_code
        else:
            raise TypeError("store_code must be str")

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        if isinstance(items, str):
            self._items = items
        else:
            raise TypeError("items must be str")

    @property
    def reduce_type(self):
        return self._reduce_type

    @reduce_type.setter
    def reduce_type(self, reduce_type):
        if isinstance(reduce_type, str):
            self._reduce_type = reduce_type
        else:
            raise TypeError("reduce_type must be str")


    def get_api_name(self):
        return "taobao.inventory.adjust.external"

    def to_dict(self):
        request_dict = {}
        if self._biz_unique_code is not None:
            request_dict["biz_unique_code"] = convert_basic(self._biz_unique_code)

        if self._occupy_operate_code is not None:
            request_dict["occupy_operate_code"] = convert_basic(self._occupy_operate_code)

        if self._operate_type is not None:
            request_dict["operate_type"] = convert_basic(self._operate_type)

        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._operate_time is not None:
            request_dict["operate_time"] = convert_basic(self._operate_time)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._items is not None:
            request_dict["items"] = convert_basic(self._items)

        if self._reduce_type is not None:
            request_dict["reduce_type"] = convert_basic(self._reduce_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


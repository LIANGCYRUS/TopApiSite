from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoInventoryInitialRequest(BaseRequest):

    def __init__(
        self,
        store_code: str = None,
        items: str = None
    ):
        """
            商家仓库编码
        """
        self._store_code = store_code
        """
            商品初始库存信息： [{"scItemId":"商品后端ID，如果有传scItemCode,参数可以为0","scItemCode":"商品商家编码","inventoryType":"库存类型  1：正常,2：损坏,3：冻结,10：质押,11-20:用户自定义","quantity":"数量"}]
        """
        self._items = items

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


    def get_api_name(self):
        return "taobao.inventory.initial"

    def to_dict(self):
        request_dict = {}
        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._items is not None:
            request_dict["items"] = convert_basic(self._items)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


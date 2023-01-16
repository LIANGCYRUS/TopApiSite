from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoInventoryInitialItemRequest(BaseRequest):

    def __init__(
        self,
        sc_item_id: int = None,
        store_inventorys: str = None
    ):
        """
            后端商品id
        """
        self._sc_item_id = sc_item_id
        """
            商品初始库存信息： [{"storeCode":"必选,商家仓库编号","inventoryType":"可选，库存类型 1：正常,2：损坏,3：冻结,10：质押,11-20:用户自定义,默认为1","quantity":"必选,数量"}]
        """
        self._store_inventorys = store_inventorys

    @property
    def sc_item_id(self):
        return self._sc_item_id

    @sc_item_id.setter
    def sc_item_id(self, sc_item_id):
        if isinstance(sc_item_id, int):
            self._sc_item_id = sc_item_id
        else:
            raise TypeError("sc_item_id must be int")

    @property
    def store_inventorys(self):
        return self._store_inventorys

    @store_inventorys.setter
    def store_inventorys(self, store_inventorys):
        if isinstance(store_inventorys, str):
            self._store_inventorys = store_inventorys
        else:
            raise TypeError("store_inventorys must be str")


    def get_api_name(self):
        return "taobao.inventory.initial.item"

    def to_dict(self):
        request_dict = {}
        if self._sc_item_id is not None:
            request_dict["sc_item_id"] = convert_basic(self._sc_item_id)

        if self._store_inventorys is not None:
            request_dict["store_inventorys"] = convert_basic(self._store_inventorys)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


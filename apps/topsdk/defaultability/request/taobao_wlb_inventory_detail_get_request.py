from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbInventoryDetailGetRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        inventory_type_list: list = None,
        store_code: str = None
    ):
        """
            商品ID
        """
        self._item_id = item_id
        """
            库存类型列表，值包括：
VENDIBLE--可销售库存
FREEZE--冻结库存
ONWAY--在途库存
DEFECT--残次品库存
ENGINE_DAMAGE--机损
BOX_DAMAGE--箱损
EXPIRATION--过保
        """
        self._inventory_type_list = inventory_type_list
        """
            仓库编码
        """
        self._store_code = store_code

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, int):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be int")

    @property
    def inventory_type_list(self):
        return self._inventory_type_list

    @inventory_type_list.setter
    def inventory_type_list(self, inventory_type_list):
        if isinstance(inventory_type_list, list):
            self._inventory_type_list = inventory_type_list
        else:
            raise TypeError("inventory_type_list must be list")

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
        return "taobao.wlb.inventory.detail.get"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._inventory_type_list is not None:
            request_dict["inventory_type_list"] = convert_basic_list(self._inventory_type_list)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


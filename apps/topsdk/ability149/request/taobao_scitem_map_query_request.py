from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoScitemMapQueryRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        sku_id: int = None
    ):
        """
            map_type为1：前台ic商品id
map_type为2：分销productid
        """
        self._item_id = item_id
        """
            map_type为1：前台ic商品skuid 
map_type为2：分销商品的skuid
        """
        self._sku_id = sku_id

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
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, sku_id):
        if isinstance(sku_id, int):
            self._sku_id = sku_id
        else:
            raise TypeError("sku_id must be int")


    def get_api_name(self):
        return "taobao.scitem.map.query"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


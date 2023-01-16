from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRegionSaleQueryRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        sku_id: int = None,
        sale_region_level: int = None
    ):
        """
            商品id
        """
        self._item_id = item_id
        """
            无sku传0
        """
        self._sku_id = sku_id
        """
            1:国家;2:省;3: 市;4:区县
        """
        self._sale_region_level = sale_region_level

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

    @property
    def sale_region_level(self):
        return self._sale_region_level

    @sale_region_level.setter
    def sale_region_level(self, sale_region_level):
        if isinstance(sale_region_level, int):
            self._sale_region_level = sale_region_level
        else:
            raise TypeError("sale_region_level must be int")


    def get_api_name(self):
        return "taobao.region.sale.query"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        if self._sale_region_level is not None:
            request_dict["sale_region_level"] = convert_basic(self._sale_region_level)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


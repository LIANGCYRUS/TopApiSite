from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemOuteridUpdateRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        outer_id: str = None,
        sku_outers: list = None
    ):
        """
            商品ID
        """
        self._item_id = item_id
        """
            商品维度商家编码，如果不修改可以不传；清空请设置空串
        """
        self._outer_id = outer_id
        """
            商品SKU更新OuterId时候用的数据
        """
        self._sku_outers = sku_outers

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
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")

    @property
    def sku_outers(self):
        return self._sku_outers

    @sku_outers.setter
    def sku_outers(self, sku_outers):
        if isinstance(sku_outers, list):
            self._sku_outers = sku_outers
        else:
            raise TypeError("sku_outers must be list")


    def get_api_name(self):
        return "tmall.item.outerid.update"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._sku_outers is not None:
            request_dict["sku_outers"] = convert_struct_list(self._sku_outers)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TmallItemOuteridUpdateUpdateSkuOuterId:
    def __init__(
        self,
        outer_id: str = None,
        properties: str = None,
        sku_id: int = None
    ):
        """
            被更新的Sku的商家外部id
        """
        self.outer_id = outer_id
        """
            Sku属性串。格式:pid:vid;pid:vid,如: 1627207:3232483;1630696:3284570,表示机身颜色:军绿色;手机套餐:一电一充；如果填写将以属性对形式查找被更新SKU
        """
        self.properties = properties
        """
            SkuID，如果填写，将以SKUID查找被更新的SKU
        """
        self.sku_id = sku_id


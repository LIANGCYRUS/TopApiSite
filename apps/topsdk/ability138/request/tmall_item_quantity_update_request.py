from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemQuantityUpdateRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        item_quantity: int = None,
        sku_quantities: list = None,
        options: object = None
    ):
        """
            商品id
        """
        self._item_id = item_id
        """
            商品库存数；增量编辑方式支持正数、负数。（无SKU商品使用这个字段）
        """
        self._item_quantity = item_quantity
        """
            更新SKU库存时候的SKU库存对象；如果没有SKU或者不更新SKU库存，可以不填;查找SKU目前支持ID，属性串和商家编码三种模式，建议选用一种最合适的，切勿滥用，一次调用中如果混合使用，更新结果不可预期！
        """
        self._sku_quantities = sku_quantities
        """
            商品库存更新时候的可选参数
        """
        self._options = options

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
    def item_quantity(self):
        return self._item_quantity

    @item_quantity.setter
    def item_quantity(self, item_quantity):
        if isinstance(item_quantity, int):
            self._item_quantity = item_quantity
        else:
            raise TypeError("item_quantity must be int")

    @property
    def sku_quantities(self):
        return self._sku_quantities

    @sku_quantities.setter
    def sku_quantities(self, sku_quantities):
        if isinstance(sku_quantities, list):
            self._sku_quantities = sku_quantities
        else:
            raise TypeError("sku_quantities must be list")

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, options):
        if isinstance(options, object):
            self._options = options
        else:
            raise TypeError("options must be object")


    def get_api_name(self):
        return "tmall.item.quantity.update"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._item_quantity is not None:
            request_dict["item_quantity"] = convert_basic(self._item_quantity)

        if self._sku_quantities is not None:
            request_dict["sku_quantities"] = convert_struct_list(self._sku_quantities)

        if self._options is not None:
            request_dict["options"] = convert_struct(self._options)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TmallItemQuantityUpdateUpdateSkuQuantity:
    def __init__(
        self,
        outer_id: str = None,
        properties: str = None,
        quantity: int = None,
        sku_id: int = None
    ):
        """
            Sku的商家外部id，用于指定被修改库存的SKU
        """
        self.outer_id = outer_id
        """
            Sku属性串。格式:pid:vid;pid:vid,如: 1627207:3232483;1630696:3284570,表示机身颜色:军绿色;手机套餐:一电一充，用于指定被修改库存的SKU
        """
        self.properties = properties
        """
            SKU属于这个sku的商品的库存；增量编辑方式支持正数、负数
        """
        self.quantity = quantity
        """
            SkuID，用于指定被修改库存的
        """
        self.sku_id = sku_id

class TmallItemQuantityUpdateUpdateItemQuantityOption:
    def __init__(
        self,
        outer_biz_key: str = None,
        type: int = None
    ):
        """
            增量更新时幂等外部编码，只能包含十六进制字符(0-9,a-f,A-F)
        """
        self.outer_biz_key = outer_biz_key
        """
            库存更新方式: 1是全量更新 2是增量更新；默认是1。
        """
        self.type = type


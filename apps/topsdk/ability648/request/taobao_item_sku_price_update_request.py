from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemSkuPriceUpdateRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        properties: str = None,
        quantity: int = None,
        price: str = None,
        outer_id: str = None,
        lang: str = None,
        item_price: str = None,
        ignorewarning: str = None
    ):
        """
            Sku所属商品数字id，可通过 taobao.item.get 获取
        """
        self._num_iid = num_iid
        """
            Sku属性串。格式:pid:vid;pid:vid,如: 1627207:3232483;1630696:3284570,表示机身颜色:军绿色;手机套餐:一电一充
        """
        self._properties = properties
        """
            Sku的库存数量。sku的总数量应该小于等于商品总数量(Item的NUM)，sku数量变化后item的总数量也会随着变化。取值范围:大于等于零的整数
        """
        self._quantity = quantity
        """
            Sku的销售价格。精确到2位小数;单位:元。如:200.07，表示:200元7分。修改后的sku价格要保证商品的价格在所有sku价格所形成的价格区间内（例如：商品价格为6元，sku价格有5元、10元两种，如果要修改5元sku的价格，那么修改的范围只能是0-6元之间；如果要修改10元的sku，那么修改的范围只能是6到无穷大的区间中）
        """
        self._price = price
        """
            Sku的商家外部id
        """
        self._outer_id = outer_id
        """
            Sku文字的版本。可选值:zh_HK(繁体),zh_CN(简体);默认值:zh_CN
        """
        self._lang = lang
        """
            sku所属商品的价格。当用户更新sku，使商品价格不属于sku价格之间的时候，用于修改商品的价格，使sku能够更新成功
        """
        self._item_price = item_price
        """
            忽略警告提示.
        """
        self._ignorewarning = ignorewarning

    @property
    def num_iid(self):
        return self._num_iid

    @num_iid.setter
    def num_iid(self, num_iid):
        if isinstance(num_iid, int):
            self._num_iid = num_iid
        else:
            raise TypeError("num_iid must be int")

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        if isinstance(properties, str):
            self._properties = properties
        else:
            raise TypeError("properties must be str")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
        else:
            raise TypeError("quantity must be int")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, str):
            self._price = price
        else:
            raise TypeError("price must be str")

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
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang):
        if isinstance(lang, str):
            self._lang = lang
        else:
            raise TypeError("lang must be str")

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, item_price):
        if isinstance(item_price, str):
            self._item_price = item_price
        else:
            raise TypeError("item_price must be str")

    @property
    def ignorewarning(self):
        return self._ignorewarning

    @ignorewarning.setter
    def ignorewarning(self, ignorewarning):
        if isinstance(ignorewarning, str):
            self._ignorewarning = ignorewarning
        else:
            raise TypeError("ignorewarning must be str")


    def get_api_name(self):
        return "taobao.item.sku.price.update"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        if self._quantity is not None:
            request_dict["quantity"] = convert_basic(self._quantity)

        if self._price is not None:
            request_dict["price"] = convert_basic(self._price)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._lang is not None:
            request_dict["lang"] = convert_basic(self._lang)

        if self._item_price is not None:
            request_dict["item_price"] = convert_basic(self._item_price)

        if self._ignorewarning is not None:
            request_dict["ignorewarning"] = convert_basic(self._ignorewarning)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


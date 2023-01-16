from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemSkuDeleteRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        properties: str = None,
        lang: str = None,
        item_price: str = None,
        item_num: int = None,
        ignorewarning: str = None
    ):
        """
            Sku所属商品数字id，可通过 taobao.item.get 获取。必选
        """
        self._num_iid = num_iid
        """
            Sku属性串。格式:pid:vid;pid:vid,如: 1627207:3232483;1630696:3284570,表示机身颜色:军绿色;手机套餐:一电一充
        """
        self._properties = properties
        """
            Sku文字的版本。可选值:zh_HK(繁体),zh_CN(简体);默认值:zh_CN
        """
        self._lang = lang
        """
            sku所属商品的价格。当用户删除sku，使商品价格不属于sku价格之间的时候，用于修改商品的价格，使sku能够删除成功
        """
        self._item_price = item_price
        """
            sku所属商品的数量,大于0的整数。当用户删除sku，使商品数量不等于sku数量之和时候，用于修改商品的数量，使sku能够删除成功。特别是删除最后一个sku的时候，一定要设置商品数量到正常的值，否则删除失败
        """
        self._item_num = item_num
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
    def item_num(self):
        return self._item_num

    @item_num.setter
    def item_num(self, item_num):
        if isinstance(item_num, int):
            self._item_num = item_num
        else:
            raise TypeError("item_num must be int")

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
        return "taobao.item.sku.delete"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        if self._lang is not None:
            request_dict["lang"] = convert_basic(self._lang)

        if self._item_price is not None:
            request_dict["item_price"] = convert_basic(self._item_price)

        if self._item_num is not None:
            request_dict["item_num"] = convert_basic(self._item_num)

        if self._ignorewarning is not None:
            request_dict["ignorewarning"] = convert_basic(self._ignorewarning)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


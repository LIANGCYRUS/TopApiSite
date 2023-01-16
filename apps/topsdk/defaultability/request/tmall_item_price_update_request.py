from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemPriceUpdateRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        item_price: str = None,
        sku_prices: list = None,
        options: object = None
    ):
        """
            商品ID
        """
        self._item_id = item_id
        """
            被更新商品价格
        """
        self._item_price = item_price
        """
            更新SKU价格时候的SKU价格对象；如果没有SKU或者不更新SKU价格，可以不填;查找SKU目前支持ID，属性串和商家编码三种模式，建议选用一种最合适的，切勿滥用，一次调用中如果混合使用，更新结果不可预期！
        """
        self._sku_prices = sku_prices
        """
            商品价格更新时候的可选参数
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
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, item_price):
        if isinstance(item_price, str):
            self._item_price = item_price
        else:
            raise TypeError("item_price must be str")

    @property
    def sku_prices(self):
        return self._sku_prices

    @sku_prices.setter
    def sku_prices(self, sku_prices):
        if isinstance(sku_prices, list):
            self._sku_prices = sku_prices
        else:
            raise TypeError("sku_prices must be list")

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
        return "tmall.item.price.update"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._item_price is not None:
            request_dict["item_price"] = convert_basic(self._item_price)

        if self._sku_prices is not None:
            request_dict["sku_prices"] = convert_struct_list(self._sku_prices)

        if self._options is not None:
            request_dict["options"] = convert_struct(self._options)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TmallItemPriceUpdateUpdateSkuPrice:
    def __init__(
        self,
        sku_id: int = None,
        properties: str = None,
        outer_id: str = None,
        price: str = None
    ):
        """
            SkuID，用于指定被修改价格的SKU
        """
        self.sku_id = sku_id
        """
            Sku属性串。格式:pid:vid;pid:vid,如: 1627207:3232483;1630696:3284570,表示机身颜色:军绿色;手机套餐:一电一充，用于指定被修改价格的SKU
        """
        self.properties = properties
        """
            Sku的商家外部id，用于指定被修改价格的SKU
        """
        self.outer_id = outer_id
        """
            属于这个sku的商品的价格 取值范围:0-100000000;精确到2位小数;单位:元。如:200.07，表示:200元7分。
        """
        self.price = price

class TmallItemPriceUpdateUpdateItemPriceOption:
    def __init__(
        self,
        ignore_fake_credit: bool = None,
        currency_type: str = None
    ):
        """
            是否忽略涉嫌炒信警告信息
        """
        self.ignore_fake_credit = ignore_fake_credit
        """
            目标币种，非必填，仅支持天猫国际官网同购商家将外币价格修改成人民币价格时使用
        """
        self.currency_type = currency_type


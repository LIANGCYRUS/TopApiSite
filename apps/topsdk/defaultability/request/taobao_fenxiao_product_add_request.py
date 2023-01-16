from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductAddRequest(BaseRequest):

    def __init__(
        self,
        category_id: int = None,
        name: str = None,
        productcat_id: int = None,
        standard_price: str = None,
        standard_retail_price: str = None,
        retail_price_low: str = None,
        retail_price_high: str = None,
        cost_price: str = None,
        dealer_cost_price: str = None,
        outer_id: str = None,
        quantity: int = None,
        desc: str = None,
        prov: str = None,
        city: str = None,
        postage_type: str = None,
        postage_id: int = None,
        postage_ordinary: str = None,
        postage_fast: str = None,
        postage_ems: str = None,
        have_invoice: str = None,
        have_quarantee: str = None,
        discount_id: int = None,
        trade_type: str = None,
        is_authz: str = None,
        pic_path: str = None,
        image: bytes = None,
        properties: str = None,
        property_alias: str = None,
        input_properties: str = None,
        sku_standard_prices: str = None,
        sku_cost_prices: str = None,
        sku_outer_ids: str = None,
        sku_quantitys: str = None,
        sku_properties: str = None,
        sku_dealer_cost_prices: str = None,
        item_id: int = None,
        spu_id: int = None
    ):
        """
            所属类目id，参考Taobao.itemcats.get，不支持成人等类目，输入成人类目id保存提示类目属性错误。
        """
        self._category_id = category_id
        """
            产品名称，长度不超过60个字节。
        """
        self._name = name
        """
            产品线ID
        """
        self._productcat_id = productcat_id
        """
            采购基准价格，单位：元。例：“10.56”。必须在0.01元到10000000元之间。
        """
        self._standard_price = standard_price
        """
            零售基准价，单位：元。例：“10.56”。必须在0.01元到10000000元之间。
        """
        self._standard_retail_price = standard_retail_price
        """
            最低零售价，单位：元。例：“10.56”。必须在0.01元到10000000元之间。
        """
        self._retail_price_low = retail_price_low
        """
            最高零售价，单位：元。例：“10.56”。必须在0.01元到10000000元之间，最高零售价必须大于最低零售价。
        """
        self._retail_price_high = retail_price_high
        """
            代销采购价格，单位：元。例：“10.56”。必须在0.01元到10000000元之间。
        """
        self._cost_price = cost_price
        """
            经销采购价，单位：元。例：“10.56”。必须在0.01元到10000000元之间。
        """
        self._dealer_cost_price = dealer_cost_price
        """
            商家编码，长度不能超过60个字节。
        """
        self._outer_id = outer_id
        """
            产品库存必须是1到999999。
        """
        self._quantity = quantity
        """
            产品描述，长度为5到25000字符。
        """
        self._desc = desc
        """
            所在地：省，例：“浙江”
        """
        self._prov = prov
        """
            所在地：市，例：“杭州”
        """
        self._city = city
        """
            运费类型，可选值：seller（供应商承担运费）、buyer（分销商承担运费）,默认seller。
        """
        self._postage_type = postage_type
        """
            运费模板ID，参考taobao.postages.get。
        """
        self._postage_id = postage_id
        """
            平邮费用，单位：元。例：“10.56”。 大小为0.01元到999999元之间。
        """
        self._postage_ordinary = postage_ordinary
        """
            快递费用，单位：元。例：“10.56”。 大小为0.01元到999999元之间。
        """
        self._postage_fast = postage_fast
        """
            ems费用，单位：元。例：“10.56”。 大小为0.00元到999999元之间。
        """
        self._postage_ems = postage_ems
        """
            是否有发票，可选值：false（否）、true（是），默认false。
        """
        self._have_invoice = have_invoice
        """
            是否有保修，可选值：false（否）、true（是），默认false。
        """
        self._have_quarantee = have_quarantee
        """
            折扣ID
        """
        self._discount_id = discount_id
        """
            分销方式：AGENT（只做代销，默认值）、DEALER（只做经销）、ALL（代销和经销都做）
        """
        self._trade_type = trade_type
        """
            添加产品时，添加入参isAuthz:yes|no 
yes:需要授权 
no:不需要授权 
默认是需要授权
        """
        self._is_authz = is_authz
        """
            产品主图图片空间相对路径或绝对路径
        """
        self._pic_path = pic_path
        """
            产品主图，大小不超过500k，格式为gif,jpg,jpeg,png,bmp等图片
        """
        self._image = image
        """
            产品属性，格式为pid:vid;pid:vid
        """
        self._properties = properties
        """
            属性别名，格式为：pid:vid:alias;pid:vid:alias（alias为别名）
        """
        self._property_alias = property_alias
        """
            自定义属性。格式为pid:value;pid:value
        """
        self._input_properties = input_properties
        """
            sku的采购基准价。如果多个，用逗号分隔，并与其他sku信息保持相同顺序
        """
        self._sku_standard_prices = sku_standard_prices
        """
            sku的采购价。如果多个，用逗号分隔，并与其他sku信息保持相同顺序
        """
        self._sku_cost_prices = sku_cost_prices
        """
            sku的商家编码。如果多个，用逗号分隔，并与其他sku信息保持相同顺序
        """
        self._sku_outer_ids = sku_outer_ids
        """
            sku的库存。如果多个，用逗号分隔，并与其他sku信息保持相同顺序
        """
        self._sku_quantitys = sku_quantitys
        """
            sku的属性。如果多个，用逗号分隔，并与其他sku信息保持相同顺序
        """
        self._sku_properties = sku_properties
        """
            sku的经销采购价。如果多个，用逗号分隔，并与其他sku信息保持相同顺序。其中每个值的单位：元。例：“10.56,12.3”。必须在0.01元到10000000元之间。
        """
        self._sku_dealer_cost_prices = sku_dealer_cost_prices
        """
            导入的商品ID
        """
        self._item_id = item_id
        """
            产品spuID，达尔文产品必须要传spuID，否则不能发布。其他非达尔文产品，看情况传
        """
        self._spu_id = spu_id

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int):
            self._category_id = category_id
        else:
            raise TypeError("category_id must be int")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def productcat_id(self):
        return self._productcat_id

    @productcat_id.setter
    def productcat_id(self, productcat_id):
        if isinstance(productcat_id, int):
            self._productcat_id = productcat_id
        else:
            raise TypeError("productcat_id must be int")

    @property
    def standard_price(self):
        return self._standard_price

    @standard_price.setter
    def standard_price(self, standard_price):
        if isinstance(standard_price, str):
            self._standard_price = standard_price
        else:
            raise TypeError("standard_price must be str")

    @property
    def standard_retail_price(self):
        return self._standard_retail_price

    @standard_retail_price.setter
    def standard_retail_price(self, standard_retail_price):
        if isinstance(standard_retail_price, str):
            self._standard_retail_price = standard_retail_price
        else:
            raise TypeError("standard_retail_price must be str")

    @property
    def retail_price_low(self):
        return self._retail_price_low

    @retail_price_low.setter
    def retail_price_low(self, retail_price_low):
        if isinstance(retail_price_low, str):
            self._retail_price_low = retail_price_low
        else:
            raise TypeError("retail_price_low must be str")

    @property
    def retail_price_high(self):
        return self._retail_price_high

    @retail_price_high.setter
    def retail_price_high(self, retail_price_high):
        if isinstance(retail_price_high, str):
            self._retail_price_high = retail_price_high
        else:
            raise TypeError("retail_price_high must be str")

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        if isinstance(cost_price, str):
            self._cost_price = cost_price
        else:
            raise TypeError("cost_price must be str")

    @property
    def dealer_cost_price(self):
        return self._dealer_cost_price

    @dealer_cost_price.setter
    def dealer_cost_price(self, dealer_cost_price):
        if isinstance(dealer_cost_price, str):
            self._dealer_cost_price = dealer_cost_price
        else:
            raise TypeError("dealer_cost_price must be str")

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
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
        else:
            raise TypeError("quantity must be int")

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        if isinstance(desc, str):
            self._desc = desc
        else:
            raise TypeError("desc must be str")

    @property
    def prov(self):
        return self._prov

    @prov.setter
    def prov(self, prov):
        if isinstance(prov, str):
            self._prov = prov
        else:
            raise TypeError("prov must be str")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str):
            self._city = city
        else:
            raise TypeError("city must be str")

    @property
    def postage_type(self):
        return self._postage_type

    @postage_type.setter
    def postage_type(self, postage_type):
        if isinstance(postage_type, str):
            self._postage_type = postage_type
        else:
            raise TypeError("postage_type must be str")

    @property
    def postage_id(self):
        return self._postage_id

    @postage_id.setter
    def postage_id(self, postage_id):
        if isinstance(postage_id, int):
            self._postage_id = postage_id
        else:
            raise TypeError("postage_id must be int")

    @property
    def postage_ordinary(self):
        return self._postage_ordinary

    @postage_ordinary.setter
    def postage_ordinary(self, postage_ordinary):
        if isinstance(postage_ordinary, str):
            self._postage_ordinary = postage_ordinary
        else:
            raise TypeError("postage_ordinary must be str")

    @property
    def postage_fast(self):
        return self._postage_fast

    @postage_fast.setter
    def postage_fast(self, postage_fast):
        if isinstance(postage_fast, str):
            self._postage_fast = postage_fast
        else:
            raise TypeError("postage_fast must be str")

    @property
    def postage_ems(self):
        return self._postage_ems

    @postage_ems.setter
    def postage_ems(self, postage_ems):
        if isinstance(postage_ems, str):
            self._postage_ems = postage_ems
        else:
            raise TypeError("postage_ems must be str")

    @property
    def have_invoice(self):
        return self._have_invoice

    @have_invoice.setter
    def have_invoice(self, have_invoice):
        if isinstance(have_invoice, str):
            self._have_invoice = have_invoice
        else:
            raise TypeError("have_invoice must be str")

    @property
    def have_quarantee(self):
        return self._have_quarantee

    @have_quarantee.setter
    def have_quarantee(self, have_quarantee):
        if isinstance(have_quarantee, str):
            self._have_quarantee = have_quarantee
        else:
            raise TypeError("have_quarantee must be str")

    @property
    def discount_id(self):
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        if isinstance(discount_id, int):
            self._discount_id = discount_id
        else:
            raise TypeError("discount_id must be int")

    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        if isinstance(trade_type, str):
            self._trade_type = trade_type
        else:
            raise TypeError("trade_type must be str")

    @property
    def is_authz(self):
        return self._is_authz

    @is_authz.setter
    def is_authz(self, is_authz):
        if isinstance(is_authz, str):
            self._is_authz = is_authz
        else:
            raise TypeError("is_authz must be str")

    @property
    def pic_path(self):
        return self._pic_path

    @pic_path.setter
    def pic_path(self, pic_path):
        if isinstance(pic_path, str):
            self._pic_path = pic_path
        else:
            raise TypeError("pic_path must be str")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        if isinstance(image, bytes):
            self._image = image
        else:
            raise TypeError("image must be bytes")

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
    def property_alias(self):
        return self._property_alias

    @property_alias.setter
    def property_alias(self, property_alias):
        if isinstance(property_alias, str):
            self._property_alias = property_alias
        else:
            raise TypeError("property_alias must be str")

    @property
    def input_properties(self):
        return self._input_properties

    @input_properties.setter
    def input_properties(self, input_properties):
        if isinstance(input_properties, str):
            self._input_properties = input_properties
        else:
            raise TypeError("input_properties must be str")

    @property
    def sku_standard_prices(self):
        return self._sku_standard_prices

    @sku_standard_prices.setter
    def sku_standard_prices(self, sku_standard_prices):
        if isinstance(sku_standard_prices, str):
            self._sku_standard_prices = sku_standard_prices
        else:
            raise TypeError("sku_standard_prices must be str")

    @property
    def sku_cost_prices(self):
        return self._sku_cost_prices

    @sku_cost_prices.setter
    def sku_cost_prices(self, sku_cost_prices):
        if isinstance(sku_cost_prices, str):
            self._sku_cost_prices = sku_cost_prices
        else:
            raise TypeError("sku_cost_prices must be str")

    @property
    def sku_outer_ids(self):
        return self._sku_outer_ids

    @sku_outer_ids.setter
    def sku_outer_ids(self, sku_outer_ids):
        if isinstance(sku_outer_ids, str):
            self._sku_outer_ids = sku_outer_ids
        else:
            raise TypeError("sku_outer_ids must be str")

    @property
    def sku_quantitys(self):
        return self._sku_quantitys

    @sku_quantitys.setter
    def sku_quantitys(self, sku_quantitys):
        if isinstance(sku_quantitys, str):
            self._sku_quantitys = sku_quantitys
        else:
            raise TypeError("sku_quantitys must be str")

    @property
    def sku_properties(self):
        return self._sku_properties

    @sku_properties.setter
    def sku_properties(self, sku_properties):
        if isinstance(sku_properties, str):
            self._sku_properties = sku_properties
        else:
            raise TypeError("sku_properties must be str")

    @property
    def sku_dealer_cost_prices(self):
        return self._sku_dealer_cost_prices

    @sku_dealer_cost_prices.setter
    def sku_dealer_cost_prices(self, sku_dealer_cost_prices):
        if isinstance(sku_dealer_cost_prices, str):
            self._sku_dealer_cost_prices = sku_dealer_cost_prices
        else:
            raise TypeError("sku_dealer_cost_prices must be str")

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
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, spu_id):
        if isinstance(spu_id, int):
            self._spu_id = spu_id
        else:
            raise TypeError("spu_id must be int")


    def get_api_name(self):
        return "taobao.fenxiao.product.add"

    def to_dict(self):
        request_dict = {}
        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._productcat_id is not None:
            request_dict["productcat_id"] = convert_basic(self._productcat_id)

        if self._standard_price is not None:
            request_dict["standard_price"] = convert_basic(self._standard_price)

        if self._standard_retail_price is not None:
            request_dict["standard_retail_price"] = convert_basic(self._standard_retail_price)

        if self._retail_price_low is not None:
            request_dict["retail_price_low"] = convert_basic(self._retail_price_low)

        if self._retail_price_high is not None:
            request_dict["retail_price_high"] = convert_basic(self._retail_price_high)

        if self._cost_price is not None:
            request_dict["cost_price"] = convert_basic(self._cost_price)

        if self._dealer_cost_price is not None:
            request_dict["dealer_cost_price"] = convert_basic(self._dealer_cost_price)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._quantity is not None:
            request_dict["quantity"] = convert_basic(self._quantity)

        if self._desc is not None:
            request_dict["desc"] = convert_basic(self._desc)

        if self._prov is not None:
            request_dict["prov"] = convert_basic(self._prov)

        if self._city is not None:
            request_dict["city"] = convert_basic(self._city)

        if self._postage_type is not None:
            request_dict["postage_type"] = convert_basic(self._postage_type)

        if self._postage_id is not None:
            request_dict["postage_id"] = convert_basic(self._postage_id)

        if self._postage_ordinary is not None:
            request_dict["postage_ordinary"] = convert_basic(self._postage_ordinary)

        if self._postage_fast is not None:
            request_dict["postage_fast"] = convert_basic(self._postage_fast)

        if self._postage_ems is not None:
            request_dict["postage_ems"] = convert_basic(self._postage_ems)

        if self._have_invoice is not None:
            request_dict["have_invoice"] = convert_basic(self._have_invoice)

        if self._have_quarantee is not None:
            request_dict["have_quarantee"] = convert_basic(self._have_quarantee)

        if self._discount_id is not None:
            request_dict["discount_id"] = convert_basic(self._discount_id)

        if self._trade_type is not None:
            request_dict["trade_type"] = convert_basic(self._trade_type)

        if self._is_authz is not None:
            request_dict["is_authz"] = convert_basic(self._is_authz)

        if self._pic_path is not None:
            request_dict["pic_path"] = convert_basic(self._pic_path)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        if self._property_alias is not None:
            request_dict["property_alias"] = convert_basic(self._property_alias)

        if self._input_properties is not None:
            request_dict["input_properties"] = convert_basic(self._input_properties)

        if self._sku_standard_prices is not None:
            request_dict["sku_standard_prices"] = convert_basic(self._sku_standard_prices)

        if self._sku_cost_prices is not None:
            request_dict["sku_cost_prices"] = convert_basic(self._sku_cost_prices)

        if self._sku_outer_ids is not None:
            request_dict["sku_outer_ids"] = convert_basic(self._sku_outer_ids)

        if self._sku_quantitys is not None:
            request_dict["sku_quantitys"] = convert_basic(self._sku_quantitys)

        if self._sku_properties is not None:
            request_dict["sku_properties"] = convert_basic(self._sku_properties)

        if self._sku_dealer_cost_prices is not None:
            request_dict["sku_dealer_cost_prices"] = convert_basic(self._sku_dealer_cost_prices)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._spu_id is not None:
            request_dict["spu_id"] = convert_basic(self._spu_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


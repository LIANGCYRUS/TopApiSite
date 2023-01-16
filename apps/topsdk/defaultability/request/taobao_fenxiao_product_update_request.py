from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductUpdateRequest(BaseRequest):

    def __init__(
        self,
        pid: int = None,
        name: str = None,
        standard_price: str = None,
        standard_retail_price: str = None,
        retail_price_low: str = None,
        retail_price_high: str = None,
        cost_price: str = None,
        dealer_cost_price: str = None,
        outer_id: str = None,
        quantity: int = None,
        desc: str = None,
        category_id: int = None,
        properties: str = None,
        property_alias: str = None,
        input_properties: str = None,
        pic_path: str = None,
        image: bytes = None,
        prov: str = None,
        city: str = None,
        postage_type: str = None,
        postage_id: int = None,
        postage_ordinary: str = None,
        postage_fast: str = None,
        postage_ems: str = None,
        have_invoice: str = None,
        have_quarantee: str = None,
        status: str = None,
        sku_ids: str = None,
        sku_standard_prices: str = None,
        sku_cost_prices: str = None,
        sku_dealer_cost_prices: str = None,
        sku_quantitys: str = None,
        sku_outer_ids: str = None,
        sku_properties: str = None,
        sku_properties_del: str = None,
        discount_id: int = None,
        is_authz: str = None
    ):
        """
            产品ID
        """
        self._pid = pid
        """
            产品名称，长度不超过60个字节。
        """
        self._name = name
        """
            采购基准价，单位：元。例：“10.56”。必须在0.01元到10000000元之间。
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
            所属类目id，参考Taobao.itemcats.get，不支持成人等类目，输入成人类目id保存提示类目属性错误。
        """
        self._category_id = category_id
        """
            产品属性
        """
        self._properties = properties
        """
            属性别名
        """
        self._property_alias = property_alias
        """
            自定义属性。格式为pid:value;pid:value
        """
        self._input_properties = input_properties
        """
            产品主图图片空间相对路径或绝对路径
        """
        self._pic_path = pic_path
        """
            主图图片，如果pic_path参数不空，则优先使用pic_path，忽略该参数
        """
        self._image = image
        """
            所在地：省，例：“浙江”
        """
        self._prov = prov
        """
            所在地：市，例：“杭州”
        """
        self._city = city
        """
            运费类型，可选值：seller（供应商承担运费）、buyer（分销商承担运费）。
        """
        self._postage_type = postage_type
        """
            运费模板ID，参考taobao.postages.get。更新时必须指定运费类型为 buyer，否则不更新。
        """
        self._postage_id = postage_id
        """
            平邮费用，单位：元。例：“10.56”。大小为0.01元到999999元之间。更新时必须指定运费类型为buyer，否则不更新。
        """
        self._postage_ordinary = postage_ordinary
        """
            快递费用，单位：元。例：“10.56”。大小为0.01元到999999元之间。更新时必须指定运费类型为buyer，否则不更新。
        """
        self._postage_fast = postage_fast
        """
            ems费用，单位：元。例：“10.56”。大小为0.01元到999999元之间。更新时必须指定运费类型为buyer，否则不更新。
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
            发布状态，可选值：up（上架）、down（下架）、delete（删除），输入非法字符则忽略。
        """
        self._status = status
        """
            sku id列表，例：1001,1002,1003。如果传入sku_properties将忽略此参数。
        """
        self._sku_ids = sku_ids
        """
            sku采购基准价，单位元，例："10.50,11.00,20.50"，字段必须和上面的sku_ids或sku_properties保持一致。
        """
        self._sku_standard_prices = sku_standard_prices
        """
            sku采购价格，单位元，例："10.50,11.00,20.50"，字段必须和上面的sku_ids或sku_properties保持一致。
        """
        self._sku_cost_prices = sku_cost_prices
        """
            sku的经销采购价。如果多个，用逗号分隔，并与其他sku信息保持相同顺序。其中每个值的单位：元。例：“10.56,12.3”。必须在0.01元到10000000元之间。
        """
        self._sku_dealer_cost_prices = sku_dealer_cost_prices
        """
            sku库存，单位元，例："10,20,30"，字段必须和sku_ids或sku_properties保持一致。
        """
        self._sku_quantitys = sku_quantitys
        """
            sku商家编码 ，单位元，例："S1000,S1002,S1003"，字段必须和上面的id或sku_properties保持一致，如果没有可以写成",,"
        """
        self._sku_outer_ids = sku_outer_ids
        """
            sku属性。格式:pid:vid;pid:vid,表示一组属性如:1627207:3232483;1630696:3284570,表示一组:机身颜色:军绿色;手机套餐:一电一充。多组之间用逗号“,”区分。(属性的pid调用taobao.itemprops.get取得，属性值的vid用taobao.itempropvalues.get取得vid)
通过此字段可新增和更新sku。若传入此值将忽略sku_ids字段。sku其他字段与此值保持一致。
        """
        self._sku_properties = sku_properties
        """
            根据sku属性删除sku信息。需要按组删除属性。
        """
        self._sku_properties_del = sku_properties_del
        """
            折扣ID
        """
        self._discount_id = discount_id
        """
            产品是否需要授权isAuthz:yes|no 
yes:需要授权 
no:不需要授权
        """
        self._is_authz = is_authz

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, pid):
        if isinstance(pid, int):
            self._pid = pid
        else:
            raise TypeError("pid must be int")

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
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int):
            self._category_id = category_id
        else:
            raise TypeError("category_id must be int")

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
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")

    @property
    def sku_ids(self):
        return self._sku_ids

    @sku_ids.setter
    def sku_ids(self, sku_ids):
        if isinstance(sku_ids, str):
            self._sku_ids = sku_ids
        else:
            raise TypeError("sku_ids must be str")

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
    def sku_dealer_cost_prices(self):
        return self._sku_dealer_cost_prices

    @sku_dealer_cost_prices.setter
    def sku_dealer_cost_prices(self, sku_dealer_cost_prices):
        if isinstance(sku_dealer_cost_prices, str):
            self._sku_dealer_cost_prices = sku_dealer_cost_prices
        else:
            raise TypeError("sku_dealer_cost_prices must be str")

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
    def sku_outer_ids(self):
        return self._sku_outer_ids

    @sku_outer_ids.setter
    def sku_outer_ids(self, sku_outer_ids):
        if isinstance(sku_outer_ids, str):
            self._sku_outer_ids = sku_outer_ids
        else:
            raise TypeError("sku_outer_ids must be str")

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
    def sku_properties_del(self):
        return self._sku_properties_del

    @sku_properties_del.setter
    def sku_properties_del(self, sku_properties_del):
        if isinstance(sku_properties_del, str):
            self._sku_properties_del = sku_properties_del
        else:
            raise TypeError("sku_properties_del must be str")

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
    def is_authz(self):
        return self._is_authz

    @is_authz.setter
    def is_authz(self, is_authz):
        if isinstance(is_authz, str):
            self._is_authz = is_authz
        else:
            raise TypeError("is_authz must be str")


    def get_api_name(self):
        return "taobao.fenxiao.product.update"

    def to_dict(self):
        request_dict = {}
        if self._pid is not None:
            request_dict["pid"] = convert_basic(self._pid)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

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

        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        if self._property_alias is not None:
            request_dict["property_alias"] = convert_basic(self._property_alias)

        if self._input_properties is not None:
            request_dict["input_properties"] = convert_basic(self._input_properties)

        if self._pic_path is not None:
            request_dict["pic_path"] = convert_basic(self._pic_path)

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

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._sku_ids is not None:
            request_dict["sku_ids"] = convert_basic(self._sku_ids)

        if self._sku_standard_prices is not None:
            request_dict["sku_standard_prices"] = convert_basic(self._sku_standard_prices)

        if self._sku_cost_prices is not None:
            request_dict["sku_cost_prices"] = convert_basic(self._sku_cost_prices)

        if self._sku_dealer_cost_prices is not None:
            request_dict["sku_dealer_cost_prices"] = convert_basic(self._sku_dealer_cost_prices)

        if self._sku_quantitys is not None:
            request_dict["sku_quantitys"] = convert_basic(self._sku_quantitys)

        if self._sku_outer_ids is not None:
            request_dict["sku_outer_ids"] = convert_basic(self._sku_outer_ids)

        if self._sku_properties is not None:
            request_dict["sku_properties"] = convert_basic(self._sku_properties)

        if self._sku_properties_del is not None:
            request_dict["sku_properties_del"] = convert_basic(self._sku_properties_del)

        if self._discount_id is not None:
            request_dict["discount_id"] = convert_basic(self._discount_id)

        if self._is_authz is not None:
            request_dict["is_authz"] = convert_basic(self._is_authz)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


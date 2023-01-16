from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoProductAddRequest(BaseRequest):

    def __init__(
        self,
        cid: int = None,
        name: str = None,
        price: str = None,
        image: bytes = None,
        outer_id: str = None,
        props: str = None,
        binds: str = None,
        sale_props: str = None,
        customer_props: str = None,
        desc: str = None,
        major: bool = None,
        native_unkeyprops: str = None,
        vertical_market: int = None,
        market_time: datetime = None,
        property_alias: str = None
    ):
        """
            商品类目ID.调用taobao.itemcats.get获取;注意:必须是叶子类目 id.
        """
        self._cid = cid
        """
            产品名称,最大30个字符.
        """
        self._name = name
        """
            产品市场价.精确到2位小数;单位为元.如：200.07
        """
        self._price = price
        """
            产品主图片.最大1M,目前仅支持GIF,JPG.
        """
        self._image = image
        """
            外部产品ID
        """
        self._outer_id = outer_id
        """
            关键属性 结构:pid:vid;pid:vid.调用taobao.itemprops.get获取pid,调用taobao.itempropvalues.get获取vid;如果碰到用户自定义属性,请用customer_props.
        """
        self._props = props
        """
            非关键属性结构:pid:vid;pid:vid.<br>
非关键属性<font color=red>不包含</font>关键属性、销售属性、用户自定义属性、商品属性;
<br>调用taobao.itemprops.get获取pid,调用taobao.itempropvalues.get获取vid.<br><font color=red>注:支持最大长度为512字节</font>
        """
        self._binds = binds
        """
            销售属性结构:pid:vid;pid:vid.调用taobao.itemprops.get获取is_sale_prop＝true的pid,调用taobao.itempropvalues.get获取vid.
        """
        self._sale_props = sale_props
        """
            用户自定义属性,结构：pid1:value1;pid2:value2，如果有型号，系列等子属性用: 隔开 例如：“20000:优衣库:型号:001;632501:1234”，表示“品牌:优衣库:型号:001;货号:1234”
<br><font color=red>注：包含所有自定义属性的传入</font>
        """
        self._customer_props = customer_props
        """
            产品描述.最大不超过25000个字符
        """
        self._desc = desc
        """
            是不是主图
        """
        self._major = major
        """
            native_unkeyprops
        """
        self._native_unkeyprops = native_unkeyprops
        """
            加入垂直市场，目前只支持以鞋城卖家身份加入名鞋馆(暂时此字段还不起作用，不对外开放)
        """
        self._vertical_market = vertical_market
        """
            上市时间。目前只支持鞋城类目传入此参数
        """
        self._market_time = market_time
        """
            销售属性值别名。格式为pid1:vid1:alias1;pid1:vid2:alia2。只有少数销售属性值支持传入别名，比如颜色和尺寸
        """
        self._property_alias = property_alias

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, cid):
        if isinstance(cid, int):
            self._cid = cid
        else:
            raise TypeError("cid must be int")

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
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, str):
            self._price = price
        else:
            raise TypeError("price must be str")

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
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")

    @property
    def props(self):
        return self._props

    @props.setter
    def props(self, props):
        if isinstance(props, str):
            self._props = props
        else:
            raise TypeError("props must be str")

    @property
    def binds(self):
        return self._binds

    @binds.setter
    def binds(self, binds):
        if isinstance(binds, str):
            self._binds = binds
        else:
            raise TypeError("binds must be str")

    @property
    def sale_props(self):
        return self._sale_props

    @sale_props.setter
    def sale_props(self, sale_props):
        if isinstance(sale_props, str):
            self._sale_props = sale_props
        else:
            raise TypeError("sale_props must be str")

    @property
    def customer_props(self):
        return self._customer_props

    @customer_props.setter
    def customer_props(self, customer_props):
        if isinstance(customer_props, str):
            self._customer_props = customer_props
        else:
            raise TypeError("customer_props must be str")

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
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        if isinstance(major, bool):
            self._major = major
        else:
            raise TypeError("major must be bool")

    @property
    def native_unkeyprops(self):
        return self._native_unkeyprops

    @native_unkeyprops.setter
    def native_unkeyprops(self, native_unkeyprops):
        if isinstance(native_unkeyprops, str):
            self._native_unkeyprops = native_unkeyprops
        else:
            raise TypeError("native_unkeyprops must be str")

    @property
    def vertical_market(self):
        return self._vertical_market

    @vertical_market.setter
    def vertical_market(self, vertical_market):
        if isinstance(vertical_market, int):
            self._vertical_market = vertical_market
        else:
            raise TypeError("vertical_market must be int")

    @property
    def market_time(self):
        return self._market_time

    @market_time.setter
    def market_time(self, market_time):
        if isinstance(market_time, datetime):
            self._market_time = market_time
        else:
            raise TypeError("market_time must be datetime")

    @property
    def property_alias(self):
        return self._property_alias

    @property_alias.setter
    def property_alias(self, property_alias):
        if isinstance(property_alias, str):
            self._property_alias = property_alias
        else:
            raise TypeError("property_alias must be str")


    def get_api_name(self):
        return "taobao.product.add"

    def to_dict(self):
        request_dict = {}
        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._price is not None:
            request_dict["price"] = convert_basic(self._price)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._props is not None:
            request_dict["props"] = convert_basic(self._props)

        if self._binds is not None:
            request_dict["binds"] = convert_basic(self._binds)

        if self._sale_props is not None:
            request_dict["sale_props"] = convert_basic(self._sale_props)

        if self._customer_props is not None:
            request_dict["customer_props"] = convert_basic(self._customer_props)

        if self._desc is not None:
            request_dict["desc"] = convert_basic(self._desc)

        if self._major is not None:
            request_dict["major"] = convert_basic(self._major)

        if self._native_unkeyprops is not None:
            request_dict["native_unkeyprops"] = convert_basic(self._native_unkeyprops)

        if self._vertical_market is not None:
            request_dict["vertical_market"] = convert_basic(self._vertical_market)

        if self._market_time is not None:
            request_dict["market_time"] = convert_basic(self._market_time)

        if self._property_alias is not None:
            request_dict["property_alias"] = convert_basic(self._property_alias)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


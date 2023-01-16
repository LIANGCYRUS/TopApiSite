from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemPriceUpdateRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        approve_status: str = None,
        auto_repost: bool = None,
        cid: int = None,
        desc: str = None,
        valid_thru: int = None,
        post_fee: str = None,
        express_fee: str = None,
        ems_fee: str = None,
        has_warranty: bool = None,
        has_invoice: bool = None,
        increment: str = None,
        props: str = None,
        num: int = None,
        freight_payer: str = None,
        seller_cids: str = None,
        has_showcase: bool = None,
        list_time: datetime = None,
        stuff_status: str = None,
        title: str = None,
        price: str = None,
        has_discount: bool = None,
        outer_id: str = None,
        postage_id: int = None,
        product_id: int = None,
        is_taobao: bool = None,
        is_ex: bool = None,
        is_3D: bool = None,
        auction_point: int = None,
        property_alias: str = None,
        lang: str = None,
        pic_path: str = None,
        is_replace_sku: bool = None,
        image: bytes = None,
        auto_fill: str = None,
        sell_promise: bool = None,
        cod_postage_id: int = None,
        is_lightning_consignment: bool = None,
        weight: int = None,
        shape: str = None,
        is_xinpin: bool = None,
        sub_stock: int = None,
        ignorewarning: str = None,
        input_pids: list = None,
        input_str: list = None,
        sku_properties: str = None,
        sku_quantities: str = None,
        sku_prices: str = None,
        sku_outer_ids: str = None,
        location.state: str = None,
        location.city: str = None
    ):
        """
            商品数字ID，该参数必须
        """
        self._num_iid = num_iid
        """
            商品上传后的状态。可选值:onsale（出售中）,instock（库中），如果同时更新商品状态为出售中及list_time为将来的时间，则商品还是处于定时上架的状态, 此时item.is_timing为true
        """
        self._approve_status = approve_status
        """
            自动重发。可选值:true,false;
        """
        self._auto_repost = auto_repost
        """
            叶子类目id
        """
        self._cid = cid
        """
            商品描述. 字数要大于5个字符，小于25000个字符 ，受违禁词控制
        """
        self._desc = desc
        """
            有效期。可选值:7,14;单位:天;
        """
        self._valid_thru = valid_thru
        """
            平邮费用。取值范围:0.01-999.00;精确到2位小数;单位:元。如:5.07，表示:5元7分, 注:post_fee,express_fee,ems_fee需一起填写
        """
        self._post_fee = post_fee
        """
            快递费用。取值范围:0.01-999.00;精确到2位小数;单位:元。如:15.07，表示:15元7分
        """
        self._express_fee = express_fee
        """
            ems费用。取值范围:0.01-999.00;精确到2位小数;单位:元。如:25.07，表示:25元7分
        """
        self._ems_fee = ems_fee
        """
            是否有保修。可选值:true,false;
        """
        self._has_warranty = has_warranty
        """
            是否有发票。可选值:true,false (商城卖家此字段必须为true)
        """
        self._has_invoice = has_invoice
        """
            加价幅度 如果为0，代表系统代理幅度
        """
        self._increment = increment
        """
            商品属性列表。格式:pid:vid;pid:vid。属性的pid调用taobao.itemprops.get取得，属性值的vid用taobao.itempropvalues.get取得vid。 如果该类目下面没有属性，可以不用填写。如果有属性，必选属性必填，其他非必选属性可以选择不填写.属性不能超过35对。所有属性加起来包括分割符不能超过549字节，单个属性没有限制。 如果有属性是可输入的话，则用字段input_str填入属性的值。
        """
        self._props = props
        """
            商品数量，取值范围:0-999999的整数。且需要等于Sku所有数量的和
        """
        self._num = num
        """
            运费承担方式。运费承担方式。可选值:seller（卖家承担）,buyer(买家承担);
        """
        self._freight_payer = freight_payer
        """
            重新关联商品与店铺类目，结构:",cid1,cid2,...,"，如果店铺类目存在二级类目，必须传入子类目cids。
        """
        self._seller_cids = seller_cids
        """
            橱窗推荐。可选值:true,false;
        """
        self._has_showcase = has_showcase
        """
            上架时间。不论是更新架下的商品还是出售中的商品，如果这个字段小于当前时间则直接上架商品，并且上架的时间为更新商品的时间，此时item.is_timing为false，如果大于当前时间则宝贝会下架进入定时上架的宝贝中。
        """
        self._list_time = list_time
        """
            商品新旧程度。可选值:new（全新）,unused（闲置）,second（二手）。
        """
        self._stuff_status = stuff_status
        """
            宝贝标题. 不能超过60字符,受违禁词控制
        """
        self._title = title
        """
            商品价格。取值范围:0-100000000;精确到2位小数;单位:元。如:200.07，表示:200元7分。需要在正确的价格区间内。
        """
        self._price = price
        """
            支持会员打折。可选值:true,false;
        """
        self._has_discount = has_discount
        """
            商家编码
        """
        self._outer_id = outer_id
        """
            宝贝所属的运费模板ID。取值范围：整数且必须是该卖家的运费模板的ID（可通过taobao.postages.get获得当前会话用户的所有邮费模板）
        """
        self._postage_id = postage_id
        """
            商品所属的产品ID(B商家发布商品需要用)
        """
        self._product_id = product_id
        """
            是否在淘宝上显示
        """
        self._is_taobao = is_taobao
        """
            是否在外店显示
        """
        self._is_ex = is_ex
        """
            是否是3D
        """
        self._is_3D = is_3D
        """
            商品的积分返点比例。如：5 表示返点比例0.5%. 注意：返点比例必须是>0的整数，而且最大是90,即为9%.B商家在发布非虚拟商品时，返点必须是 5的倍数，即0.5%的倍数。其它是1的倍数，即0.1%的倍数。无名良品商家发布商品时，复用该字段记录积分宝返点比例，返点必须是对应类目的返点步长的整数倍，默认是5，即0.5%。注意此时该字段值依旧必须是>0的整数，注意此时该字段值依旧必须是>0的整数，最高值不超过500，即50%
        """
        self._auction_point = auction_point
        """
            属性值别名。如pid:vid:别名;pid1:vid1:别名1， pid:属性id vid:值id。总长度不超过512字节
        """
        self._property_alias = property_alias
        """
            商品文字的版本，繁体传入”zh_HK”，简体传入”zh_CN”
        """
        self._lang = lang
        """
            商品主图需要关联的图片空间的相对url。这个url所对应的图片必须要属于当前用户。pic_path和image只需要传入一个,如果两个都传，默认选择pic_path
        """
        self._pic_path = pic_path
        """
            是否替换sku
        """
        self._is_replace_sku = is_replace_sku
        """
            商品图片。类型:JPG,GIF;最大长度:500k
        """
        self._image = image
        """
            代充商品类型。只有少数类目下的商品可以标记上此字段，具体哪些类目可以上传可以通过taobao.itemcat.features.get获得。在代充商品的类目下，不传表示不标记商品类型（交易搜索中就不能通过标记搜到相关的交易了）。可选类型： 
no_mark(不做类型标记) 
time_card(点卡软件代充) 
fee_card(话费软件代充)
        """
        self._auto_fill = auto_fill
        """
            是否承诺退换货服务!虚拟商品无须设置此项!
        """
        self._sell_promise = sell_promise
        """
            货到付款运费模板ID
        """
        self._cod_postage_id = cod_postage_id
        """
            实物闪电发货。注意：在售的闪电发货产品不允许取消闪电发货，需要先下架商品才能取消闪电发货标记
        """
        self._is_lightning_consignment = is_lightning_consignment
        """
            商品的重量(商超卖家专用字段)
        """
        self._weight = weight
        """
            宝贝形态:
1代表电子券;0或其他代表实物
        """
        self._shape = shape
        """
            商品是否为新品。只有在当前类目开通新品,并且当前用户拥有该类目下发布新品权限时才能设置is_xinpin为true，否则设置true后会返回错误码:isv.invalid-permission:xinpin。同时只有一口价全新的宝贝才能设置为新品，否则会返回错误码：isv.invalid-parameter:xinpin。不设置参数就保持原有值。
        """
        self._is_xinpin = is_xinpin
        """
            商品是否支持拍下减库存:1支持;2取消支持(付款减库存);0(默认)不更改 集市卖家默认拍下减库存; 商城卖家默认付款减库存
        """
        self._sub_stock = sub_stock
        """
            忽略警告提示.
        """
        self._ignorewarning = ignorewarning
        """
            用户自行输入的类目属性ID串，结构："pid1,pid2,pid3"，如："20000"（表示品牌） 注：通常一个类目下用户可输入的关键属性不超过1个。
        """
        self._input_pids = input_pids
        """
            用户自行输入的子属性名和属性值，结构:"父属性值;一级子属性名;一级子属性值;二级子属性名;自定义输入值,....",如：“耐克;耐克系列;科比系列;科比系列;2K5,Nike乔丹鞋;乔丹系列;乔丹鞋系列;乔丹鞋系列;json5”，多个自定义属性用','分割，input_str需要与input_pids一一对应，注：通常一个类目下用户可输入的关键属性不超过1个。所有属性别名加起来不能超过3999字节。此处不可以使用“其他”、“其它”和“其她”这三个词。
        """
        self._input_str = input_str
        """
            更新的Sku的属性串，调用taobao.itemprops.get获取类目属性，如果属性是销售属性，再用taobao.itempropvalues.get取得vid。格式:pid:vid;pid:vid。该字段内的销售属性也需要在props字段填写 。如果更新时有对Sku进行操作，则Sku的properties一定要传入。
        """
        self._sku_properties = sku_properties
        """
            更新的Sku的数量串，结构如：num1,num2,num3 如:2,3,4
        """
        self._sku_quantities = sku_quantities
        """
            更新的Sku的价格串，结构如：10.00,5.00,… 精确到2位小数;单位:元。如:200.07，表示:200元7分
        """
        self._sku_prices = sku_prices
        """
            Sku的外部id串，结构如：1234,1342,… sku_properties, sku_quantities, sku_prices, sku_outer_ids在输入数据时要一一对应，如果没有sku_outer_ids也要写上这个参数，入参是","(这个是两个sku的示列，逗号数应该是sku个数减1)；该参数最大长度是512个字节
        """
        self._sku_outer_ids = sku_outer_ids
        """
            所在地省份。如浙江 具体可以下载http://dl.open.taobao.com/sdk/商品城市列表.rar 取到
        """
        self._location.state = location.state
        """
            所在地城市。如杭州 具体可以下载http://dl.open.taobao.com/sdk/商品城市列表.rar 取到
        """
        self._location.city = location.city

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
    def approve_status(self):
        return self._approve_status

    @approve_status.setter
    def approve_status(self, approve_status):
        if isinstance(approve_status, str):
            self._approve_status = approve_status
        else:
            raise TypeError("approve_status must be str")

    @property
    def auto_repost(self):
        return self._auto_repost

    @auto_repost.setter
    def auto_repost(self, auto_repost):
        if isinstance(auto_repost, bool):
            self._auto_repost = auto_repost
        else:
            raise TypeError("auto_repost must be bool")

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
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        if isinstance(desc, str):
            self._desc = desc
        else:
            raise TypeError("desc must be str")

    @property
    def valid_thru(self):
        return self._valid_thru

    @valid_thru.setter
    def valid_thru(self, valid_thru):
        if isinstance(valid_thru, int):
            self._valid_thru = valid_thru
        else:
            raise TypeError("valid_thru must be int")

    @property
    def post_fee(self):
        return self._post_fee

    @post_fee.setter
    def post_fee(self, post_fee):
        if isinstance(post_fee, str):
            self._post_fee = post_fee
        else:
            raise TypeError("post_fee must be str")

    @property
    def express_fee(self):
        return self._express_fee

    @express_fee.setter
    def express_fee(self, express_fee):
        if isinstance(express_fee, str):
            self._express_fee = express_fee
        else:
            raise TypeError("express_fee must be str")

    @property
    def ems_fee(self):
        return self._ems_fee

    @ems_fee.setter
    def ems_fee(self, ems_fee):
        if isinstance(ems_fee, str):
            self._ems_fee = ems_fee
        else:
            raise TypeError("ems_fee must be str")

    @property
    def has_warranty(self):
        return self._has_warranty

    @has_warranty.setter
    def has_warranty(self, has_warranty):
        if isinstance(has_warranty, bool):
            self._has_warranty = has_warranty
        else:
            raise TypeError("has_warranty must be bool")

    @property
    def has_invoice(self):
        return self._has_invoice

    @has_invoice.setter
    def has_invoice(self, has_invoice):
        if isinstance(has_invoice, bool):
            self._has_invoice = has_invoice
        else:
            raise TypeError("has_invoice must be bool")

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, increment):
        if isinstance(increment, str):
            self._increment = increment
        else:
            raise TypeError("increment must be str")

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
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        if isinstance(num, int):
            self._num = num
        else:
            raise TypeError("num must be int")

    @property
    def freight_payer(self):
        return self._freight_payer

    @freight_payer.setter
    def freight_payer(self, freight_payer):
        if isinstance(freight_payer, str):
            self._freight_payer = freight_payer
        else:
            raise TypeError("freight_payer must be str")

    @property
    def seller_cids(self):
        return self._seller_cids

    @seller_cids.setter
    def seller_cids(self, seller_cids):
        if isinstance(seller_cids, str):
            self._seller_cids = seller_cids
        else:
            raise TypeError("seller_cids must be str")

    @property
    def has_showcase(self):
        return self._has_showcase

    @has_showcase.setter
    def has_showcase(self, has_showcase):
        if isinstance(has_showcase, bool):
            self._has_showcase = has_showcase
        else:
            raise TypeError("has_showcase must be bool")

    @property
    def list_time(self):
        return self._list_time

    @list_time.setter
    def list_time(self, list_time):
        if isinstance(list_time, datetime):
            self._list_time = list_time
        else:
            raise TypeError("list_time must be datetime")

    @property
    def stuff_status(self):
        return self._stuff_status

    @stuff_status.setter
    def stuff_status(self, stuff_status):
        if isinstance(stuff_status, str):
            self._stuff_status = stuff_status
        else:
            raise TypeError("stuff_status must be str")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise TypeError("title must be str")

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
    def has_discount(self):
        return self._has_discount

    @has_discount.setter
    def has_discount(self, has_discount):
        if isinstance(has_discount, bool):
            self._has_discount = has_discount
        else:
            raise TypeError("has_discount must be bool")

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
    def postage_id(self):
        return self._postage_id

    @postage_id.setter
    def postage_id(self, postage_id):
        if isinstance(postage_id, int):
            self._postage_id = postage_id
        else:
            raise TypeError("postage_id must be int")

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self._product_id = product_id
        else:
            raise TypeError("product_id must be int")

    @property
    def is_taobao(self):
        return self._is_taobao

    @is_taobao.setter
    def is_taobao(self, is_taobao):
        if isinstance(is_taobao, bool):
            self._is_taobao = is_taobao
        else:
            raise TypeError("is_taobao must be bool")

    @property
    def is_ex(self):
        return self._is_ex

    @is_ex.setter
    def is_ex(self, is_ex):
        if isinstance(is_ex, bool):
            self._is_ex = is_ex
        else:
            raise TypeError("is_ex must be bool")

    @property
    def is_3D(self):
        return self._is_3D

    @is_3D.setter
    def is_3D(self, is_3D):
        if isinstance(is_3D, bool):
            self._is_3D = is_3D
        else:
            raise TypeError("is_3D must be bool")

    @property
    def auction_point(self):
        return self._auction_point

    @auction_point.setter
    def auction_point(self, auction_point):
        if isinstance(auction_point, int):
            self._auction_point = auction_point
        else:
            raise TypeError("auction_point must be int")

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
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, lang):
        if isinstance(lang, str):
            self._lang = lang
        else:
            raise TypeError("lang must be str")

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
    def is_replace_sku(self):
        return self._is_replace_sku

    @is_replace_sku.setter
    def is_replace_sku(self, is_replace_sku):
        if isinstance(is_replace_sku, bool):
            self._is_replace_sku = is_replace_sku
        else:
            raise TypeError("is_replace_sku must be bool")

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
    def auto_fill(self):
        return self._auto_fill

    @auto_fill.setter
    def auto_fill(self, auto_fill):
        if isinstance(auto_fill, str):
            self._auto_fill = auto_fill
        else:
            raise TypeError("auto_fill must be str")

    @property
    def sell_promise(self):
        return self._sell_promise

    @sell_promise.setter
    def sell_promise(self, sell_promise):
        if isinstance(sell_promise, bool):
            self._sell_promise = sell_promise
        else:
            raise TypeError("sell_promise must be bool")

    @property
    def cod_postage_id(self):
        return self._cod_postage_id

    @cod_postage_id.setter
    def cod_postage_id(self, cod_postage_id):
        if isinstance(cod_postage_id, int):
            self._cod_postage_id = cod_postage_id
        else:
            raise TypeError("cod_postage_id must be int")

    @property
    def is_lightning_consignment(self):
        return self._is_lightning_consignment

    @is_lightning_consignment.setter
    def is_lightning_consignment(self, is_lightning_consignment):
        if isinstance(is_lightning_consignment, bool):
            self._is_lightning_consignment = is_lightning_consignment
        else:
            raise TypeError("is_lightning_consignment must be bool")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = weight
        else:
            raise TypeError("weight must be int")

    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, shape):
        if isinstance(shape, str):
            self._shape = shape
        else:
            raise TypeError("shape must be str")

    @property
    def is_xinpin(self):
        return self._is_xinpin

    @is_xinpin.setter
    def is_xinpin(self, is_xinpin):
        if isinstance(is_xinpin, bool):
            self._is_xinpin = is_xinpin
        else:
            raise TypeError("is_xinpin must be bool")

    @property
    def sub_stock(self):
        return self._sub_stock

    @sub_stock.setter
    def sub_stock(self, sub_stock):
        if isinstance(sub_stock, int):
            self._sub_stock = sub_stock
        else:
            raise TypeError("sub_stock must be int")

    @property
    def ignorewarning(self):
        return self._ignorewarning

    @ignorewarning.setter
    def ignorewarning(self, ignorewarning):
        if isinstance(ignorewarning, str):
            self._ignorewarning = ignorewarning
        else:
            raise TypeError("ignorewarning must be str")

    @property
    def input_pids(self):
        return self._input_pids

    @input_pids.setter
    def input_pids(self, input_pids):
        if isinstance(input_pids, list):
            self._input_pids = input_pids
        else:
            raise TypeError("input_pids must be list")

    @property
    def input_str(self):
        return self._input_str

    @input_str.setter
    def input_str(self, input_str):
        if isinstance(input_str, list):
            self._input_str = input_str
        else:
            raise TypeError("input_str must be list")

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
    def sku_quantities(self):
        return self._sku_quantities

    @sku_quantities.setter
    def sku_quantities(self, sku_quantities):
        if isinstance(sku_quantities, str):
            self._sku_quantities = sku_quantities
        else:
            raise TypeError("sku_quantities must be str")

    @property
    def sku_prices(self):
        return self._sku_prices

    @sku_prices.setter
    def sku_prices(self, sku_prices):
        if isinstance(sku_prices, str):
            self._sku_prices = sku_prices
        else:
            raise TypeError("sku_prices must be str")

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
    def location.state(self):
        return self._location.state

    @location.state.setter
    def location.state(self, location.state):
        if isinstance(location.state, str):
            self._location.state = location.state
        else:
            raise TypeError("location.state must be str")

    @property
    def location.city(self):
        return self._location.city

    @location.city.setter
    def location.city(self, location.city):
        if isinstance(location.city, str):
            self._location.city = location.city
        else:
            raise TypeError("location.city must be str")


    def get_api_name(self):
        return "taobao.item.price.update"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._approve_status is not None:
            request_dict["approve_status"] = convert_basic(self._approve_status)

        if self._auto_repost is not None:
            request_dict["auto_repost"] = convert_basic(self._auto_repost)

        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._desc is not None:
            request_dict["desc"] = convert_basic(self._desc)

        if self._valid_thru is not None:
            request_dict["valid_thru"] = convert_basic(self._valid_thru)

        if self._post_fee is not None:
            request_dict["post_fee"] = convert_basic(self._post_fee)

        if self._express_fee is not None:
            request_dict["express_fee"] = convert_basic(self._express_fee)

        if self._ems_fee is not None:
            request_dict["ems_fee"] = convert_basic(self._ems_fee)

        if self._has_warranty is not None:
            request_dict["has_warranty"] = convert_basic(self._has_warranty)

        if self._has_invoice is not None:
            request_dict["has_invoice"] = convert_basic(self._has_invoice)

        if self._increment is not None:
            request_dict["increment"] = convert_basic(self._increment)

        if self._props is not None:
            request_dict["props"] = convert_basic(self._props)

        if self._num is not None:
            request_dict["num"] = convert_basic(self._num)

        if self._freight_payer is not None:
            request_dict["freight_payer"] = convert_basic(self._freight_payer)

        if self._seller_cids is not None:
            request_dict["seller_cids"] = convert_basic(self._seller_cids)

        if self._has_showcase is not None:
            request_dict["has_showcase"] = convert_basic(self._has_showcase)

        if self._list_time is not None:
            request_dict["list_time"] = convert_basic(self._list_time)

        if self._stuff_status is not None:
            request_dict["stuff_status"] = convert_basic(self._stuff_status)

        if self._title is not None:
            request_dict["title"] = convert_basic(self._title)

        if self._price is not None:
            request_dict["price"] = convert_basic(self._price)

        if self._has_discount is not None:
            request_dict["has_discount"] = convert_basic(self._has_discount)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._postage_id is not None:
            request_dict["postage_id"] = convert_basic(self._postage_id)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._is_taobao is not None:
            request_dict["is_taobao"] = convert_basic(self._is_taobao)

        if self._is_ex is not None:
            request_dict["is_ex"] = convert_basic(self._is_ex)

        if self._is_3D is not None:
            request_dict["is_3D"] = convert_basic(self._is_3D)

        if self._auction_point is not None:
            request_dict["auction_point"] = convert_basic(self._auction_point)

        if self._property_alias is not None:
            request_dict["property_alias"] = convert_basic(self._property_alias)

        if self._lang is not None:
            request_dict["lang"] = convert_basic(self._lang)

        if self._pic_path is not None:
            request_dict["pic_path"] = convert_basic(self._pic_path)

        if self._is_replace_sku is not None:
            request_dict["is_replace_sku"] = convert_basic(self._is_replace_sku)

        if self._auto_fill is not None:
            request_dict["auto_fill"] = convert_basic(self._auto_fill)

        if self._sell_promise is not None:
            request_dict["sell_promise"] = convert_basic(self._sell_promise)

        if self._cod_postage_id is not None:
            request_dict["cod_postage_id"] = convert_basic(self._cod_postage_id)

        if self._is_lightning_consignment is not None:
            request_dict["is_lightning_consignment"] = convert_basic(self._is_lightning_consignment)

        if self._weight is not None:
            request_dict["weight"] = convert_basic(self._weight)

        if self._shape is not None:
            request_dict["shape"] = convert_basic(self._shape)

        if self._is_xinpin is not None:
            request_dict["is_xinpin"] = convert_basic(self._is_xinpin)

        if self._sub_stock is not None:
            request_dict["sub_stock"] = convert_basic(self._sub_stock)

        if self._ignorewarning is not None:
            request_dict["ignorewarning"] = convert_basic(self._ignorewarning)

        if self._input_pids is not None:
            request_dict["input_pids"] = convert_basic_list(self._input_pids)

        if self._input_str is not None:
            request_dict["input_str"] = convert_basic_list(self._input_str)

        if self._sku_properties is not None:
            request_dict["sku_properties"] = convert_basic(self._sku_properties)

        if self._sku_quantities is not None:
            request_dict["sku_quantities"] = convert_basic(self._sku_quantities)

        if self._sku_prices is not None:
            request_dict["sku_prices"] = convert_basic(self._sku_prices)

        if self._sku_outer_ids is not None:
            request_dict["sku_outer_ids"] = convert_basic(self._sku_outer_ids)

        if self._location.state is not None:
            request_dict["location.state"] = convert_basic(self._location.state)

        if self._location.city is not None:
            request_dict["location.city"] = convert_basic(self._location.city)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemAddRequest(BaseRequest):

    def __init__(
        self,
        approve_status: str = None,
        type: str = None,
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
        image: bytes = None,
        auto_fill: str = None,
        sell_promise: bool = None,
        cod_postage_id: int = None,
        is_lightning_consignment: bool = None,
        weight: int = None,
        shape: str = None,
        is_xinpin: bool = None,
        sub_stock: int = None,
        features: str = None,
        scenic_ticket_pay_way: int = None,
        scenic_ticket_book_cost: str = None,
        global_stock_type: str = None,
        global_stock_country: str = None,
        global_stock_delivery_place: str = None,
        global_stock_tax_free_promise: bool = None,
        item_weight: str = None,
        item_size: str = None,
        input_custom_cpv: str = None,
        cpv_memo: str = None,
        support_custom_made: bool = None,
        custom_made_type_id: str = None,
        newprepay: str = None,
        barcode: str = None,
        sell_point: str = None,
        qualification: str = None,
        o2o_bind_service: bool = None,
        ignorewarning: str = None,
        after_sale_id: int = None,
        change_prop: str = None,
        desc_modules: str = None,
        is_offline: str = None,
        wireless_desc: str = None,
        chaoshi_extends_info: str = None,
        spu_confirm: bool = None,
        video_id: int = None,
        interactive_id: int = None,
        lease_extends_info: str = None,
        brokerage: str = None,
        biz_code: str = None,
        image_urls: list = None,
        input_pids: list = None,
        input_str: list = None,
        sku_properties: str = None,
        sku_quantities: str = None,
        sku_prices: str = None,
        sku_outer_ids: str = None,
        sku_barcode: str = None,
        sku_spec_ids: str = None,
        sku_delivery_times: str = None,
        sku_hd_length: str = None,
        sku_hd_height: str = None,
        sku_hd_lamp_quantity: str = None,
        location.state: str = None,
        location.city: str = None,
        food_security.prd_license_no: str = None,
        food_security.design_code: str = None,
        food_security.factory: str = None,
        food_security.factory_site: str = None,
        food_security.contact: str = None,
        food_security.mix: str = None,
        food_security.plan_storage: str = None,
        food_security.period: str = None,
        food_security.food_additive: str = None,
        food_security.supplier: str = None,
        food_security.product_date_start: str = None,
        food_security.product_date_end: str = None,
        food_security.stock_date_start: str = None,
        food_security.stock_date_end: str = None,
        food_security.health_product_no: str = None,
        locality_life.expirydate: str = None,
        locality_life.network_id: str = None,
        locality_life.merchant: str = None,
        locality_life.verification: str = None,
        locality_life.refund_ratio: int = None,
        locality_life.onsale_auto_refund_ratio: int = None,
        locality_life.choose_logis: str = None,
        locality_life.refundmafee: str = None,
        locality_life.obs: str = None,
        locality_life.eticket: str = None,
        locality_life.version: str = None,
        locality_life.packageid: str = None,
        paimai_info.mode: int = None,
        paimai_info.deposit: int = None,
        paimai_info.interval: int = None,
        paimai_info.reserve: str = None,
        paimai_info.valid_hour: int = None,
        paimai_info.valid_minute: int = None,
        ms_payment.reference_price: str = None,
        ms_payment.voucher_price: str = None,
        ms_payment.price: str = None,
        delivery_time.need_delivery_time: str = None,
        delivery_time.delivery_time_type: str = None,
        delivery_time.delivery_time: str = None
    ):
        """
            商品上传后的状态。可选值:onsale(出售中),instock(仓库中);默认值:onsale
        """
        self._approve_status = approve_status
        """
            发布类型。可选值:fixed(一口价),auction(拍卖)。B商家不能发布拍卖商品，而且拍卖商品是没有SKU的。拍卖商品发布时需要附加拍卖商品信息：拍卖类型(paimai_info.mode，拍卖类型包括三种：增价拍[1]，荷兰拍[2]以及降价拍[3])，商品数量(num)，起拍价(price)，价格幅度(increament)，保证金(paimai_info.deposit)。另外拍卖商品支持自定义销售周期，通过paimai_info.valid_hour和paimai_info.valid_minute来指定。对于降价拍来说需要设置降价周期(paimai_info.interval)和拍卖保留价(paimai_info.reserve)。注意：通过taobao.item.get接口获取拍卖信息时，会返回除了valid_hour和valid_minute之外的所有拍卖信息。
        """
        self._type = type
        """
            自动重发。可选值:true,false;默认值:false(不重发)
        """
        self._auto_repost = auto_repost
        """
            叶子类目id
        """
        self._cid = cid
        """
            宝贝描述。字数要大于5个字符，小于25000个字符，受违禁词控制
        """
        self._desc = desc
        """
            有效期。可选值:7,14;单位:天;默认值:14
        """
        self._valid_thru = valid_thru
        """
            平邮费用。取值范围:0.01-999.00;精确到2位小数;单位:元。如:5.07，表示:5元7分. 注:post_fee,express_fee,ems_fee需要一起填写
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
            是否有保修。可选值:true,false;默认值:false(不保修)
        """
        self._has_warranty = has_warranty
        """
            是否有发票。可选值:true,false (商城卖家此字段必须为true);默认值:false(无发票)
        """
        self._has_invoice = has_invoice
        """
            加价(降价)幅度。如果为0，代表系统代理幅度。对于增价拍和荷兰拍来说是加价幅度，对于降价拍来说是降价幅度。
        """
        self._increment = increment
        """
            商品属性列表。格式:pid:vid;pid:vid。属性的pid调用taobao.itemprops.get取得，属性值的vid用taobao.itempropvalues.get取得vid。 如果该类目下面没有属性，可以不用填写。如果有属性，必选属性必填，其他非必选属性可以选择不填写.属性不能超过35对。所有属性加起来包括分割符不能超过549字节，单个属性没有限制。 如果有属性是可输入的话，则用字段input_str填入属性的值
        """
        self._props = props
        """
            商品数量。取值范围:0-900000000的整数。且需要等于Sku所有数量的和。拍卖商品中增加拍只能为1，荷兰拍要在[2,500)范围内。
        """
        self._num = num
        """
            运费承担方式。可选值:seller（卖家承担）,buyer(买家承担);默认值:seller。卖家承担不用设置邮费和postage_id.买家承担的时候，必填邮费和postage_id 如果用户设置了运费模板会优先使用运费模板，否则要同步设置邮费（post_fee,express_fee,ems_fee）
        """
        self._freight_payer = freight_payer
        """
            商品所属的店铺类目列表。按逗号分隔。结构:",cid1,cid2,...,"，如果店铺类目存在二级类目，必须传入子类目cids。
        """
        self._seller_cids = seller_cids
        """
            橱窗推荐。可选值:true,false;默认值:false(不推荐)
        """
        self._has_showcase = has_showcase
        """
            定时上架时间。(时间格式：yyyy-MM-dd HH:mm:ss)
        """
        self._list_time = list_time
        """
            新旧程度。可选值：new(新)，second(二手)。B商家不能发布二手商品。如果是二手商品，特定类目下属性里面必填新旧成色属性
        """
        self._stuff_status = stuff_status
        """
            宝贝标题。不能超过30字符，受违禁词控制。天猫图书管控类目最大允许120字符；
        """
        self._title = title
        """
            商品价格。取值范围:0-100000000;精确到2位小数;单位:元。如:200.07，表示:200元7分。需要在正确的价格区间内。拍卖商品对应的起拍价。
        """
        self._price = price
        """
            支持会员打折。可选值:true,false;默认值:false(不打折)
        """
        self._has_discount = has_discount
        """
            商品外部编码，该字段的最大长度是64个字节
        """
        self._outer_id = outer_id
        """
            宝贝所属的运费模板ID。取值范围：整数且必须是该卖家的运费模板的ID（可通过taobao.delivery.template.get获得当前会话用户的所有邮费模板）
        """
        self._postage_id = postage_id
        """
            商品所属的产品ID(B商家发布商品需要用)
        """
        self._product_id = product_id
        """
            是否在淘宝上显示（如果传FALSE，则在淘宝主站无法显示该商品）
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
            商品的积分返点比例。如:5,表示:返点比例0.5%. 注意：返点比例必须是>0的整数，而且最大是90,即为9%.B商家在发布非虚拟商品时，返点必须是 5的倍数，即0.5%的倍数。其它是1的倍数，即0.1%的倍数。无名良品商家发布商品时，复用该字段记录积分宝返点比例，返点必须是对应类目的返点步长的整数倍，默认是5，即0.5%。注意此时该字段值依旧必须是>0的整数，最高值不超过500，即50%
        """
        self._auction_point = auction_point
        """
            属性值别名。如pid:vid:别名;pid1:vid1:别名1 ，其中：pid是属性id vid是属性值id。总长度不超过800个字符，如"123:333:你好"，引号内的是10个字符。
        """
        self._property_alias = property_alias
        """
            商品文字的字符集。繁体传入"zh_HK"，简体传入"zh_CN"，不传默认为简体
        """
        self._lang = lang
        """
            （推荐）商品主图需要关联的图片空间的相对url。这个url所对应的图片必须要属于当前用户。pic_path和image只需要传入一个,如果两个都传，默认选择pic_path
        """
        self._pic_path = pic_path
        """
            商品主图片。类型:JPG,GIF;最大长度:3M。（推荐使用pic_path字段，先把图片上传到卖家图片空间）
        """
        self._image = image
        """
            代充商品类型。在代充商品的类目下，不传表示不标记商品类型（交易搜索中就不能通过标记搜到相关的交易了）。可选类型： no_mark(不做类型标记) time_card(点卡软件代充) fee_card(话费软件代充)
        """
        self._auto_fill = auto_fill
        """
            是否承诺退换货服务!虚拟商品无须设置此项!
        """
        self._sell_promise = sell_promise
        """
            此为货到付款运费模板的ID，对应的JAVA类型是long,如果COD卖家应用了货到付款运费模板，此值要进行设置。该字段已经废弃
        """
        self._cod_postage_id = cod_postage_id
        """
            实物闪电发货
        """
        self._is_lightning_consignment = is_lightning_consignment
        """
            商品的重量(商超卖家专用字段)
        """
        self._weight = weight
        """
            宝贝形态:1代表电子券;0或其他代表实物
        """
        self._shape = shape
        """
            商品是否为新品。只有在当前类目开通新品,并且当前用户拥有该类目下发布新品权限时才能设置is_xinpin为true，否则设置true后会返回错误码:isv.invalid-permission:add-xinpin。同时只有一口价全新的宝贝才能设置为新品，否则会返回错误码：isv.invalid-parameter:xinpin。不设置该参数值或设置为false效果一致。
        """
        self._is_xinpin = is_xinpin
        """
            商品是否支持拍下减库存:1支持;2取消支持(付款减库存);0(默认)不更改集市卖家默认拍下减库存;商城卖家默认付款减库存
        """
        self._sub_stock = sub_stock
        """
            宝贝特征值，格式为：【key1:value1;key2:value2;key3:value3;】，key和value用【:】分隔，key&value之间用【;】分隔，只有在Top支持的特征值才能保存到宝贝上，目前支持的Key列表为：mysize_tp
        """
        self._features = features
        """
            景区门票类宝贝发布时候，当卖家签订了支付宝代扣协议时候，需要选择支付方式：全额支付和订金支付。当scenic_ticket_pay_way为1时表示全额支付，为2时表示订金支付
        """
        self._scenic_ticket_pay_way = scenic_ticket_pay_way
        """
            景区门票在选择订金支付时候，需要交的预订费。传入的值是1到20之间的数值，小数点后最多可以保留两位（多余的部分将做四舍五入的处理）。这个数值表示的是预订费的比例，最终的预订费为 scenic_ticket_book_cost乘一口价除以100
        """
        self._scenic_ticket_book_cost = scenic_ticket_book_cost
        """
            全球购商品采购地（库存类型），有两种库存类型：现货和代购参数值为1时代表现货，值为2时代表代购。注意：使用时请与 全球购商品采购地（地区/国家）配合使用
        """
        self._global_stock_type = global_stock_type
        """
            全球购商品采购地（地区/国家）,默认值只在全球购商品采购地（库存类型选择情况生效），地区国家值请填写法定的国家名称，类如（美国, 香港, 日本, 英国, 新西兰, 德国, 韩国, 荷兰, 法国, 意大利, 台湾, 澳门, 加拿大, 瑞士, 西班牙, 泰国, 新加坡, 马来西亚, 菲律宾），不要使用其他
        """
        self._global_stock_country = global_stock_country
        """
            全球购商品发货地，发货地现在有两种类型：“国内”和“海外及港澳台”，参数值为1时代表“国内”，值为2时代表“海外及港澳台”，默认为国内。注意：卖家必须已经签署并启用“海外直邮”合约，才能选择发货地为“海外及港澳台”
        """
        self._global_stock_delivery_place = global_stock_delivery_place
        """
            全球购商品卖家包税承诺，当值为true时，代表卖家承诺包税。注意：请与“全球购商品发货地”配合使用，包税承诺必须满足：1、发货地为海外及港澳台 2、卖家已经签署并启用“包税合约”合约
        """
        self._global_stock_tax_free_promise = global_stock_tax_free_promise
        """
            商品的重量，用于按重量计费的运费模板。注意：单位为kg。只能传入数值类型（包含小数），不能带单位，单位默认为kg。
        """
        self._item_weight = item_weight
        """
            表示商品的体积，如果需要使用按体积计费的运费模板，一定要设置这个值。该值的单位为立方米（m3），如果是其他单位，请转换成成立方米。该值支持两种格式的设置：格式1：bulk:3,单位为立方米(m3),表示直接设置为商品的体积。格式2：length:10;breadth:10;height:10，单位为米（m）。体积和长宽高都支持小数类型。在传入体积或长宽高时候，不能带单位。体积的单位默认为立方米（m3），长宽高的单位默认为米(m)该值支持两种格式的设置：格式1：bulk:3,单位为立方米(m3),表示直接设置为商品的体积。格式2：length:10;breadth:10;height:10，单位为米（m）
        """
        self._item_size = item_size
        """
            针对当前商品的自定义属性值，目前是针对销售属性值自定义的，所以调用方需要把自定义属性值对应的虚拟属性值ID（负整数，例如例子中的 -1和-2）像标准属性值值的id一样设置到SKU上，如果自定义属性值有属性值图片，也要设置到属性图片上
        """
        self._input_custom_cpv = input_custom_cpv
        """
            针对当前商品的标准属性值的补充说明，让买家更加了解商品信息减少交易纠纷
        """
        self._cpv_memo = cpv_memo
        """
            是否支持定制市场 true代表支持，false代表支持,如果为空代表与之前保持不变不会修改
        """
        self._support_custom_made = support_custom_made
        """
            定制工具Id如果支持定制市场，这个值不填写，就用之前的定制工具Id，之前的定制工具Id没有值就默认为-1
        """
        self._custom_made_type_id = custom_made_type_id
        """
            该宝贝是否支持【7天无理由退货】，卖家选择的值只是一个因素，最终以类目和选择的属性条件来确定是否支持7天。填入字符0，表示不支持；未填写或填人字符1，表示支持7天无理由退货；
        """
        self._newprepay = newprepay
        """
            商品条形码
        """
        self._barcode = barcode
        """
            商品卖点信息，最长150个字符。天猫商家和集市卖家都可用。
        """
        self._sell_point = sell_point
        """
            商品资质信息
        """
        self._qualification = qualification
        """
            汽车O2O绑定线下服务标记，如不为空，表示关联服务，否则，不关联服务。
        """
        self._o2o_bind_service = o2o_bind_service
        """
            忽略警告提示.
        """
        self._ignorewarning = ignorewarning
        """
            售后说明模板id
        """
        self._after_sale_id = after_sale_id
        """
            基础色数据，淘宝不使用
        """
        self._change_prop = change_prop
        """
            已废弃
        """
        self._desc_modules = desc_modules
        """
            是否是线下商品。1：线上商品（默认值）；2：线上或线下商品；3：线下商品。
        """
        self._is_offline = is_offline
        """
            无线的宝贝描述
        """
        self._wireless_desc = wireless_desc
        """
            天猫超市扩展字段，天猫超市专用。
        """
        self._chaoshi_extends_info = chaoshi_extends_info
        """
            手机类目spu 优化，信息确认字段
        """
        self._spu_confirm = spu_confirm
        """
            主图视频id
        """
        self._video_id = video_id
        """
            主图视频互动信息id，必须填写主图视频id才能有互动信息id
        """
        self._interactive_id = interactive_id
        """
            租赁扩展信息
        """
        self._lease_extends_info = lease_extends_info
        """
            仅淘小铺卖家需要。佣金比例(15.3对应的佣金比例为15.3%).只支持小数点后1位。多余的位数四舍五入(15.32会保存为15.3%
        """
        self._brokerage = brokerage
        """
            业务身份编码。淘小铺编码为"taobao-taoxiaopu"
        """
        self._biz_code = biz_code
        """
            此字段已经废弃，不再使用
        """
        self._image_urls = image_urls
        """
            用户自行输入的类目属性ID串，结构："pid1,pid2,pid3"，如："20000"（表示品牌） 注：通常一个类目下用户可输入的关键属性不超过1个。
        """
        self._input_pids = input_pids
        """
            用户自行输入的子属性名和属性值，结构:"父属性值;一级子属性名;一级子属性值;二级子属性名;自定义输入值,....",如：“耐克;耐克系列;科比系列;科比系列;2K5,Nike乔丹鞋;乔丹系列;乔丹鞋系列;乔丹鞋系列;json5”，多个自定义属性用','分割，input_str需要与input_pids一一对应，注：通常一个类目下用户可输入的关键属性不超过1个。所有属性别名加起来不能超过3999字节。此处不可以使用“其他”、“其它”和“其她”这三个词。
        """
        self._input_str = input_str
        """
            更新的sku的属性串，调用taobao.itemprops.get获取。格式:pid1:vid;pid2:vid,多个sku属性之间用逗号分隔。该字段内的属性需要在props字段同时包含。如果新增商品包含了sku，则此字段一定要传入,字段长度要控制在512个字节以内。
        """
        self._sku_properties = sku_properties
        """
            Sku的数量串，结构如：num1,num2,num3 如：2,3
        """
        self._sku_quantities = sku_quantities
        """
            Sku的价格串，结构如：10.00,5.00,… 精确到2位小数;单位:元。如:200.07，表示:200元7分
        """
        self._sku_prices = sku_prices
        """
            Sku的外部id串，结构如：1234,1342,… sku_properties, sku_quantities, sku_prices, sku_outer_ids在输入数据时要一一对应，如果没有sku_outer_ids也要写上这个参数，入参是","(这个是两个sku的示列，逗号数应该是sku个数减1)；该参数最大长度是512个字节
        """
        self._sku_outer_ids = sku_outer_ids
        """
            sku层面的条形码，多个SKU情况，与SKU价格库存格式类似，用逗号分隔
        """
        self._sku_barcode = sku_barcode
        """
            此参数暂时不起作用
        """
        self._sku_spec_ids = sku_spec_ids
        """
            此参数暂时不起作用
        """
        self._sku_delivery_times = sku_delivery_times
        """
            家装建材类目，商品SKU的长度，正整数，单位为cm，部分类目必选。 数据和SKU一一对应，用,分隔，如：20,30,30
        """
        self._sku_hd_length = sku_hd_length
        """
            家装建材类目，商品SKU的高度，单位为cm，部分类目必选。 天猫和淘宝格式不同。天猫：可选值为："0-15", "15-25", "25-50", "50-60", "60-80", "80-120", "120-160", "160-200"。 数据和SKU一一对应，用,分隔，格式如：15-25,25-50,25-50。 淘宝：正整数，单位为cm,格式如：20,30,30
        """
        self._sku_hd_height = sku_hd_height
        """
            家装建材类目，商品SKU的灯头数量，正整数，大于等于3，部分类目必选。天猫商家专用。 数据和SKU一一对应，用,分隔，如：3,5,7
        """
        self._sku_hd_lamp_quantity = sku_hd_lamp_quantity
        """
            所在地省份。如浙江
        """
        self._location.state = location.state
        """
            所在地城市。如杭州 。
        """
        self._location.city = location.city
        """
            生产许可证号
        """
        self._food_security.prd_license_no = food_security.prd_license_no
        """
            产品标准号
        """
        self._food_security.design_code = food_security.design_code
        """
            厂名
        """
        self._food_security.factory = food_security.factory
        """
            厂址
        """
        self._food_security.factory_site = food_security.factory_site
        """
            厂家联系方式
        """
        self._food_security.contact = food_security.contact
        """
            配料表
        """
        self._food_security.mix = food_security.mix
        """
            储藏方法
        """
        self._food_security.plan_storage = food_security.plan_storage
        """
            保质期，默认有单位，传入数字
        """
        self._food_security.period = food_security.period
        """
            食品添加剂
        """
        self._food_security.food_additive = food_security.food_additive
        """
            供货商
        """
        self._food_security.supplier = food_security.supplier
        """
            生产开始日期，格式必须为yyyy-MM-dd
        """
        self._food_security.product_date_start = food_security.product_date_start
        """
            生产结束日期,格式必须为yyyy-MM-dd
        """
        self._food_security.product_date_end = food_security.product_date_end
        """
            进货开始日期，要在生产日期之后，格式必须为yyyy-MM-dd
        """
        self._food_security.stock_date_start = food_security.stock_date_start
        """
            进货结束日期，要在生产日期之后，格式必须为yyyy-MM-dd
        """
        self._food_security.stock_date_end = food_security.stock_date_end
        """
            健字号，保健品/膳食营养补充剂 这个类目下特有的信息，此类目下无需填写生产许可证编号（QS），如果填写了生产许可证编号（QS）将被忽略不保存；保存宝贝时，标题前会自动加上健字号产品名称一起作为宝贝标题；
        """
        self._food_security.health_product_no = food_security.health_product_no
        """
            本地生活电子交易凭证业务，目前此字段只涉及到的信息为有效期;如果有效期为起止日期类型，此值为2012-08-06,2012-08-16如果有效期为【购买成功日 至】类型则格式为2012-08-16如果有效期为天数类型则格式为15
        """
        self._locality_life.expirydate = locality_life.expirydate
        """
            网点ID
        """
        self._locality_life.network_id = locality_life.network_id
        """
            码商信息，格式为 码商id:nick
        """
        self._locality_life.merchant = locality_life.merchant
        """
            核销打款 1代表核销打款 0代表非核销打款
        """
        self._locality_life.verification = locality_life.verification
        """
            退款比例，百分比%前的数字,1-100的正整数值
        """
        self._locality_life.refund_ratio = locality_life.refund_ratio
        """
            电子凭证售中自动退款比例，百分比%前的数字，介于1-100之间的整数
        """
        self._locality_life.onsale_auto_refund_ratio = locality_life.onsale_auto_refund_ratio
        """
            发布电子凭证宝贝时候表示是否使用邮寄 0: 代表不使用邮寄； 1：代表使用邮寄；如果不设置这个值，代表不使用邮寄
        """
        self._locality_life.choose_logis = locality_life.choose_logis
        """
            退款码费承担方。发布电子凭证宝贝的时候会增加“退款码费承担方”配置项，可选填：(1)s（卖家承担） (2)b(买家承担)
        """
        self._locality_life.refundmafee = locality_life.refundmafee
        """
            预约门店是否支持门店自提,1:是
        """
        self._locality_life.obs = locality_life.obs
        """
            电子凭证业务属性，数据字典是: 1、is_card:1 (暂时不用) 2、consume_way:4 （1 串码 ，4 身份证）3、consume_midmnick ：(核销放行账号:用户id-用户名，支持多个，用逗号分隔,例如 1234-测试账号35,1345-测试账号56）4、market:eticket (电子凭证商品标记) 5、has_pos:1 (1 表示商品配置线下门店，在detail上进行展示 ，没有或者其他值只不展示)格式是: k1:v2;k2:v2;........ 如：has_pos:1;market:eticket;consume_midmnick:901409638-OPPO;consume_way:4
        """
        self._locality_life.eticket = locality_life.eticket
        """
            新版电子凭证字段
        """
        self._locality_life.version = locality_life.version
        """
            新版电子凭证包 id
        """
        self._locality_life.packageid = locality_life.packageid
        """
            拍卖商品选择的拍卖类型，拍卖类型包括三种：增价拍(1)，荷兰拍(2)和降价拍(3)。
        """
        self._paimai_info.mode = paimai_info.mode
        """
            拍卖宝贝的保证金。对于增价拍和荷兰拍来说保证金有两种模式：淘宝默认模式（首次出价金额的10%），自定义固定保证金（固定冻结金额只能输入不超过30万的正整数），并且保证金只冻结1次。对于降价拍来说保证金只有淘宝默认的（竞拍价格的10% * 竞拍数量），并且每次出价都需要冻结保证金。对于拍卖宝贝来说，保证金是必须的，但是默认使用淘宝默认保证金模式，只有用户需要使用自定义固定保证金的时候才需要使用到这个参数，如果该参数不传或传入0则代表使用默认。
        """
        self._paimai_info.deposit = paimai_info.deposit
        """
            降价拍宝贝的降价周期(分钟)。降价拍宝贝的价格每隔paimai_info.interval时间会下降一次increment。
        """
        self._paimai_info.interval = paimai_info.interval
        """
            降价拍宝贝的保留价。对于降价拍来说，paimai_info.reserve必须大于0，且小于price-increment，而且（price-paimai_info.reserve）/increment的计算结果必须为整数
        """
        self._paimai_info.reserve = paimai_info.reserve
        """
            自定义销售周期的小时数。拍卖宝贝可以自定义销售周期，这里指定销售周期的小时数。注意，该参数只作为输入参数，不能通过taobao.item.get接口获取。
        """
        self._paimai_info.valid_hour = paimai_info.valid_hour
        """
            自定义销售周期的分钟数。拍卖宝贝可以自定义销售周期，这里是指定销售周期的分钟数。自定义销售周期的小时数。拍卖宝贝可以自定义销售周期，这里指定销售周期的小时数。注意，该参数只作为输入参数，不能通过taobao.item.get接口获取。
        """
        self._paimai_info.valid_minute = paimai_info.valid_minute
        """
            参考价。该商品订单首次支付价格为 订金 价格，用户可根据 参考价 估算全款。详见说明：http://bangpai.taobao.com/group/thread/15031186-303287205.htm
        """
        self._ms_payment.reference_price = ms_payment.reference_price
        """
            尾款可抵扣金额。详见说明：http://bangpai.taobao.com/group/thread/15031186-303287205.htm
        """
        self._ms_payment.voucher_price = ms_payment.voucher_price
        """
            订金。在“线上付订金线下付尾款”模式中，有订金、尾款可抵扣金额和参考价，三者需要同时填写。该商品订单首次支付价格为 订金 价格，用户可根据 参考价 估算全款。该模式有别于“一口价”付款方式，针对一个商品，只能选择两种付款方式中的一种，其适用于家装、二手车等场景。详见说明：http://bangpai.taobao.com/group/thread/15031186-303287205.htm
        """
        self._ms_payment.price = ms_payment.price
        """
            设置是否使用发货时间，商品级别，sku级别
        """
        self._delivery_time.need_delivery_time = delivery_time.need_delivery_time
        """
            发货时间类型：绝对发货时间或者相对发货时间
        """
        self._delivery_time.delivery_time_type = delivery_time.delivery_time_type
        """
            商品级别设置的发货时间。设置了商品级别的发货时间，相对发货时间，则填写相对发货时间的天数（大于3）；绝对发货时间，则填写yyyy-mm-dd格式，如2013-11-11
        """
        self._delivery_time.delivery_time = delivery_time.delivery_time

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
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")

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
    def features(self):
        return self._features

    @features.setter
    def features(self, features):
        if isinstance(features, str):
            self._features = features
        else:
            raise TypeError("features must be str")

    @property
    def scenic_ticket_pay_way(self):
        return self._scenic_ticket_pay_way

    @scenic_ticket_pay_way.setter
    def scenic_ticket_pay_way(self, scenic_ticket_pay_way):
        if isinstance(scenic_ticket_pay_way, int):
            self._scenic_ticket_pay_way = scenic_ticket_pay_way
        else:
            raise TypeError("scenic_ticket_pay_way must be int")

    @property
    def scenic_ticket_book_cost(self):
        return self._scenic_ticket_book_cost

    @scenic_ticket_book_cost.setter
    def scenic_ticket_book_cost(self, scenic_ticket_book_cost):
        if isinstance(scenic_ticket_book_cost, str):
            self._scenic_ticket_book_cost = scenic_ticket_book_cost
        else:
            raise TypeError("scenic_ticket_book_cost must be str")

    @property
    def global_stock_type(self):
        return self._global_stock_type

    @global_stock_type.setter
    def global_stock_type(self, global_stock_type):
        if isinstance(global_stock_type, str):
            self._global_stock_type = global_stock_type
        else:
            raise TypeError("global_stock_type must be str")

    @property
    def global_stock_country(self):
        return self._global_stock_country

    @global_stock_country.setter
    def global_stock_country(self, global_stock_country):
        if isinstance(global_stock_country, str):
            self._global_stock_country = global_stock_country
        else:
            raise TypeError("global_stock_country must be str")

    @property
    def global_stock_delivery_place(self):
        return self._global_stock_delivery_place

    @global_stock_delivery_place.setter
    def global_stock_delivery_place(self, global_stock_delivery_place):
        if isinstance(global_stock_delivery_place, str):
            self._global_stock_delivery_place = global_stock_delivery_place
        else:
            raise TypeError("global_stock_delivery_place must be str")

    @property
    def global_stock_tax_free_promise(self):
        return self._global_stock_tax_free_promise

    @global_stock_tax_free_promise.setter
    def global_stock_tax_free_promise(self, global_stock_tax_free_promise):
        if isinstance(global_stock_tax_free_promise, bool):
            self._global_stock_tax_free_promise = global_stock_tax_free_promise
        else:
            raise TypeError("global_stock_tax_free_promise must be bool")

    @property
    def item_weight(self):
        return self._item_weight

    @item_weight.setter
    def item_weight(self, item_weight):
        if isinstance(item_weight, str):
            self._item_weight = item_weight
        else:
            raise TypeError("item_weight must be str")

    @property
    def item_size(self):
        return self._item_size

    @item_size.setter
    def item_size(self, item_size):
        if isinstance(item_size, str):
            self._item_size = item_size
        else:
            raise TypeError("item_size must be str")

    @property
    def input_custom_cpv(self):
        return self._input_custom_cpv

    @input_custom_cpv.setter
    def input_custom_cpv(self, input_custom_cpv):
        if isinstance(input_custom_cpv, str):
            self._input_custom_cpv = input_custom_cpv
        else:
            raise TypeError("input_custom_cpv must be str")

    @property
    def cpv_memo(self):
        return self._cpv_memo

    @cpv_memo.setter
    def cpv_memo(self, cpv_memo):
        if isinstance(cpv_memo, str):
            self._cpv_memo = cpv_memo
        else:
            raise TypeError("cpv_memo must be str")

    @property
    def support_custom_made(self):
        return self._support_custom_made

    @support_custom_made.setter
    def support_custom_made(self, support_custom_made):
        if isinstance(support_custom_made, bool):
            self._support_custom_made = support_custom_made
        else:
            raise TypeError("support_custom_made must be bool")

    @property
    def custom_made_type_id(self):
        return self._custom_made_type_id

    @custom_made_type_id.setter
    def custom_made_type_id(self, custom_made_type_id):
        if isinstance(custom_made_type_id, str):
            self._custom_made_type_id = custom_made_type_id
        else:
            raise TypeError("custom_made_type_id must be str")

    @property
    def newprepay(self):
        return self._newprepay

    @newprepay.setter
    def newprepay(self, newprepay):
        if isinstance(newprepay, str):
            self._newprepay = newprepay
        else:
            raise TypeError("newprepay must be str")

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        if isinstance(barcode, str):
            self._barcode = barcode
        else:
            raise TypeError("barcode must be str")

    @property
    def sell_point(self):
        return self._sell_point

    @sell_point.setter
    def sell_point(self, sell_point):
        if isinstance(sell_point, str):
            self._sell_point = sell_point
        else:
            raise TypeError("sell_point must be str")

    @property
    def qualification(self):
        return self._qualification

    @qualification.setter
    def qualification(self, qualification):
        if isinstance(qualification, str):
            self._qualification = qualification
        else:
            raise TypeError("qualification must be str")

    @property
    def o2o_bind_service(self):
        return self._o2o_bind_service

    @o2o_bind_service.setter
    def o2o_bind_service(self, o2o_bind_service):
        if isinstance(o2o_bind_service, bool):
            self._o2o_bind_service = o2o_bind_service
        else:
            raise TypeError("o2o_bind_service must be bool")

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
    def after_sale_id(self):
        return self._after_sale_id

    @after_sale_id.setter
    def after_sale_id(self, after_sale_id):
        if isinstance(after_sale_id, int):
            self._after_sale_id = after_sale_id
        else:
            raise TypeError("after_sale_id must be int")

    @property
    def change_prop(self):
        return self._change_prop

    @change_prop.setter
    def change_prop(self, change_prop):
        if isinstance(change_prop, str):
            self._change_prop = change_prop
        else:
            raise TypeError("change_prop must be str")

    @property
    def desc_modules(self):
        return self._desc_modules

    @desc_modules.setter
    def desc_modules(self, desc_modules):
        if isinstance(desc_modules, str):
            self._desc_modules = desc_modules
        else:
            raise TypeError("desc_modules must be str")

    @property
    def is_offline(self):
        return self._is_offline

    @is_offline.setter
    def is_offline(self, is_offline):
        if isinstance(is_offline, str):
            self._is_offline = is_offline
        else:
            raise TypeError("is_offline must be str")

    @property
    def wireless_desc(self):
        return self._wireless_desc

    @wireless_desc.setter
    def wireless_desc(self, wireless_desc):
        if isinstance(wireless_desc, str):
            self._wireless_desc = wireless_desc
        else:
            raise TypeError("wireless_desc must be str")

    @property
    def chaoshi_extends_info(self):
        return self._chaoshi_extends_info

    @chaoshi_extends_info.setter
    def chaoshi_extends_info(self, chaoshi_extends_info):
        if isinstance(chaoshi_extends_info, str):
            self._chaoshi_extends_info = chaoshi_extends_info
        else:
            raise TypeError("chaoshi_extends_info must be str")

    @property
    def spu_confirm(self):
        return self._spu_confirm

    @spu_confirm.setter
    def spu_confirm(self, spu_confirm):
        if isinstance(spu_confirm, bool):
            self._spu_confirm = spu_confirm
        else:
            raise TypeError("spu_confirm must be bool")

    @property
    def video_id(self):
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        if isinstance(video_id, int):
            self._video_id = video_id
        else:
            raise TypeError("video_id must be int")

    @property
    def interactive_id(self):
        return self._interactive_id

    @interactive_id.setter
    def interactive_id(self, interactive_id):
        if isinstance(interactive_id, int):
            self._interactive_id = interactive_id
        else:
            raise TypeError("interactive_id must be int")

    @property
    def lease_extends_info(self):
        return self._lease_extends_info

    @lease_extends_info.setter
    def lease_extends_info(self, lease_extends_info):
        if isinstance(lease_extends_info, str):
            self._lease_extends_info = lease_extends_info
        else:
            raise TypeError("lease_extends_info must be str")

    @property
    def brokerage(self):
        return self._brokerage

    @brokerage.setter
    def brokerage(self, brokerage):
        if isinstance(brokerage, str):
            self._brokerage = brokerage
        else:
            raise TypeError("brokerage must be str")

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, biz_code):
        if isinstance(biz_code, str):
            self._biz_code = biz_code
        else:
            raise TypeError("biz_code must be str")

    @property
    def image_urls(self):
        return self._image_urls

    @image_urls.setter
    def image_urls(self, image_urls):
        if isinstance(image_urls, list):
            self._image_urls = image_urls
        else:
            raise TypeError("image_urls must be list")

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
    def sku_barcode(self):
        return self._sku_barcode

    @sku_barcode.setter
    def sku_barcode(self, sku_barcode):
        if isinstance(sku_barcode, str):
            self._sku_barcode = sku_barcode
        else:
            raise TypeError("sku_barcode must be str")

    @property
    def sku_spec_ids(self):
        return self._sku_spec_ids

    @sku_spec_ids.setter
    def sku_spec_ids(self, sku_spec_ids):
        if isinstance(sku_spec_ids, str):
            self._sku_spec_ids = sku_spec_ids
        else:
            raise TypeError("sku_spec_ids must be str")

    @property
    def sku_delivery_times(self):
        return self._sku_delivery_times

    @sku_delivery_times.setter
    def sku_delivery_times(self, sku_delivery_times):
        if isinstance(sku_delivery_times, str):
            self._sku_delivery_times = sku_delivery_times
        else:
            raise TypeError("sku_delivery_times must be str")

    @property
    def sku_hd_length(self):
        return self._sku_hd_length

    @sku_hd_length.setter
    def sku_hd_length(self, sku_hd_length):
        if isinstance(sku_hd_length, str):
            self._sku_hd_length = sku_hd_length
        else:
            raise TypeError("sku_hd_length must be str")

    @property
    def sku_hd_height(self):
        return self._sku_hd_height

    @sku_hd_height.setter
    def sku_hd_height(self, sku_hd_height):
        if isinstance(sku_hd_height, str):
            self._sku_hd_height = sku_hd_height
        else:
            raise TypeError("sku_hd_height must be str")

    @property
    def sku_hd_lamp_quantity(self):
        return self._sku_hd_lamp_quantity

    @sku_hd_lamp_quantity.setter
    def sku_hd_lamp_quantity(self, sku_hd_lamp_quantity):
        if isinstance(sku_hd_lamp_quantity, str):
            self._sku_hd_lamp_quantity = sku_hd_lamp_quantity
        else:
            raise TypeError("sku_hd_lamp_quantity must be str")

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

    @property
    def food_security.prd_license_no(self):
        return self._food_security.prd_license_no

    @food_security.prd_license_no.setter
    def food_security.prd_license_no(self, food_security.prd_license_no):
        if isinstance(food_security.prd_license_no, str):
            self._food_security.prd_license_no = food_security.prd_license_no
        else:
            raise TypeError("food_security.prd_license_no must be str")

    @property
    def food_security.design_code(self):
        return self._food_security.design_code

    @food_security.design_code.setter
    def food_security.design_code(self, food_security.design_code):
        if isinstance(food_security.design_code, str):
            self._food_security.design_code = food_security.design_code
        else:
            raise TypeError("food_security.design_code must be str")

    @property
    def food_security.factory(self):
        return self._food_security.factory

    @food_security.factory.setter
    def food_security.factory(self, food_security.factory):
        if isinstance(food_security.factory, str):
            self._food_security.factory = food_security.factory
        else:
            raise TypeError("food_security.factory must be str")

    @property
    def food_security.factory_site(self):
        return self._food_security.factory_site

    @food_security.factory_site.setter
    def food_security.factory_site(self, food_security.factory_site):
        if isinstance(food_security.factory_site, str):
            self._food_security.factory_site = food_security.factory_site
        else:
            raise TypeError("food_security.factory_site must be str")

    @property
    def food_security.contact(self):
        return self._food_security.contact

    @food_security.contact.setter
    def food_security.contact(self, food_security.contact):
        if isinstance(food_security.contact, str):
            self._food_security.contact = food_security.contact
        else:
            raise TypeError("food_security.contact must be str")

    @property
    def food_security.mix(self):
        return self._food_security.mix

    @food_security.mix.setter
    def food_security.mix(self, food_security.mix):
        if isinstance(food_security.mix, str):
            self._food_security.mix = food_security.mix
        else:
            raise TypeError("food_security.mix must be str")

    @property
    def food_security.plan_storage(self):
        return self._food_security.plan_storage

    @food_security.plan_storage.setter
    def food_security.plan_storage(self, food_security.plan_storage):
        if isinstance(food_security.plan_storage, str):
            self._food_security.plan_storage = food_security.plan_storage
        else:
            raise TypeError("food_security.plan_storage must be str")

    @property
    def food_security.period(self):
        return self._food_security.period

    @food_security.period.setter
    def food_security.period(self, food_security.period):
        if isinstance(food_security.period, str):
            self._food_security.period = food_security.period
        else:
            raise TypeError("food_security.period must be str")

    @property
    def food_security.food_additive(self):
        return self._food_security.food_additive

    @food_security.food_additive.setter
    def food_security.food_additive(self, food_security.food_additive):
        if isinstance(food_security.food_additive, str):
            self._food_security.food_additive = food_security.food_additive
        else:
            raise TypeError("food_security.food_additive must be str")

    @property
    def food_security.supplier(self):
        return self._food_security.supplier

    @food_security.supplier.setter
    def food_security.supplier(self, food_security.supplier):
        if isinstance(food_security.supplier, str):
            self._food_security.supplier = food_security.supplier
        else:
            raise TypeError("food_security.supplier must be str")

    @property
    def food_security.product_date_start(self):
        return self._food_security.product_date_start

    @food_security.product_date_start.setter
    def food_security.product_date_start(self, food_security.product_date_start):
        if isinstance(food_security.product_date_start, str):
            self._food_security.product_date_start = food_security.product_date_start
        else:
            raise TypeError("food_security.product_date_start must be str")

    @property
    def food_security.product_date_end(self):
        return self._food_security.product_date_end

    @food_security.product_date_end.setter
    def food_security.product_date_end(self, food_security.product_date_end):
        if isinstance(food_security.product_date_end, str):
            self._food_security.product_date_end = food_security.product_date_end
        else:
            raise TypeError("food_security.product_date_end must be str")

    @property
    def food_security.stock_date_start(self):
        return self._food_security.stock_date_start

    @food_security.stock_date_start.setter
    def food_security.stock_date_start(self, food_security.stock_date_start):
        if isinstance(food_security.stock_date_start, str):
            self._food_security.stock_date_start = food_security.stock_date_start
        else:
            raise TypeError("food_security.stock_date_start must be str")

    @property
    def food_security.stock_date_end(self):
        return self._food_security.stock_date_end

    @food_security.stock_date_end.setter
    def food_security.stock_date_end(self, food_security.stock_date_end):
        if isinstance(food_security.stock_date_end, str):
            self._food_security.stock_date_end = food_security.stock_date_end
        else:
            raise TypeError("food_security.stock_date_end must be str")

    @property
    def food_security.health_product_no(self):
        return self._food_security.health_product_no

    @food_security.health_product_no.setter
    def food_security.health_product_no(self, food_security.health_product_no):
        if isinstance(food_security.health_product_no, str):
            self._food_security.health_product_no = food_security.health_product_no
        else:
            raise TypeError("food_security.health_product_no must be str")

    @property
    def locality_life.expirydate(self):
        return self._locality_life.expirydate

    @locality_life.expirydate.setter
    def locality_life.expirydate(self, locality_life.expirydate):
        if isinstance(locality_life.expirydate, str):
            self._locality_life.expirydate = locality_life.expirydate
        else:
            raise TypeError("locality_life.expirydate must be str")

    @property
    def locality_life.network_id(self):
        return self._locality_life.network_id

    @locality_life.network_id.setter
    def locality_life.network_id(self, locality_life.network_id):
        if isinstance(locality_life.network_id, str):
            self._locality_life.network_id = locality_life.network_id
        else:
            raise TypeError("locality_life.network_id must be str")

    @property
    def locality_life.merchant(self):
        return self._locality_life.merchant

    @locality_life.merchant.setter
    def locality_life.merchant(self, locality_life.merchant):
        if isinstance(locality_life.merchant, str):
            self._locality_life.merchant = locality_life.merchant
        else:
            raise TypeError("locality_life.merchant must be str")

    @property
    def locality_life.verification(self):
        return self._locality_life.verification

    @locality_life.verification.setter
    def locality_life.verification(self, locality_life.verification):
        if isinstance(locality_life.verification, str):
            self._locality_life.verification = locality_life.verification
        else:
            raise TypeError("locality_life.verification must be str")

    @property
    def locality_life.refund_ratio(self):
        return self._locality_life.refund_ratio

    @locality_life.refund_ratio.setter
    def locality_life.refund_ratio(self, locality_life.refund_ratio):
        if isinstance(locality_life.refund_ratio, int):
            self._locality_life.refund_ratio = locality_life.refund_ratio
        else:
            raise TypeError("locality_life.refund_ratio must be int")

    @property
    def locality_life.onsale_auto_refund_ratio(self):
        return self._locality_life.onsale_auto_refund_ratio

    @locality_life.onsale_auto_refund_ratio.setter
    def locality_life.onsale_auto_refund_ratio(self, locality_life.onsale_auto_refund_ratio):
        if isinstance(locality_life.onsale_auto_refund_ratio, int):
            self._locality_life.onsale_auto_refund_ratio = locality_life.onsale_auto_refund_ratio
        else:
            raise TypeError("locality_life.onsale_auto_refund_ratio must be int")

    @property
    def locality_life.choose_logis(self):
        return self._locality_life.choose_logis

    @locality_life.choose_logis.setter
    def locality_life.choose_logis(self, locality_life.choose_logis):
        if isinstance(locality_life.choose_logis, str):
            self._locality_life.choose_logis = locality_life.choose_logis
        else:
            raise TypeError("locality_life.choose_logis must be str")

    @property
    def locality_life.refundmafee(self):
        return self._locality_life.refundmafee

    @locality_life.refundmafee.setter
    def locality_life.refundmafee(self, locality_life.refundmafee):
        if isinstance(locality_life.refundmafee, str):
            self._locality_life.refundmafee = locality_life.refundmafee
        else:
            raise TypeError("locality_life.refundmafee must be str")

    @property
    def locality_life.obs(self):
        return self._locality_life.obs

    @locality_life.obs.setter
    def locality_life.obs(self, locality_life.obs):
        if isinstance(locality_life.obs, str):
            self._locality_life.obs = locality_life.obs
        else:
            raise TypeError("locality_life.obs must be str")

    @property
    def locality_life.eticket(self):
        return self._locality_life.eticket

    @locality_life.eticket.setter
    def locality_life.eticket(self, locality_life.eticket):
        if isinstance(locality_life.eticket, str):
            self._locality_life.eticket = locality_life.eticket
        else:
            raise TypeError("locality_life.eticket must be str")

    @property
    def locality_life.version(self):
        return self._locality_life.version

    @locality_life.version.setter
    def locality_life.version(self, locality_life.version):
        if isinstance(locality_life.version, str):
            self._locality_life.version = locality_life.version
        else:
            raise TypeError("locality_life.version must be str")

    @property
    def locality_life.packageid(self):
        return self._locality_life.packageid

    @locality_life.packageid.setter
    def locality_life.packageid(self, locality_life.packageid):
        if isinstance(locality_life.packageid, str):
            self._locality_life.packageid = locality_life.packageid
        else:
            raise TypeError("locality_life.packageid must be str")

    @property
    def paimai_info.mode(self):
        return self._paimai_info.mode

    @paimai_info.mode.setter
    def paimai_info.mode(self, paimai_info.mode):
        if isinstance(paimai_info.mode, int):
            self._paimai_info.mode = paimai_info.mode
        else:
            raise TypeError("paimai_info.mode must be int")

    @property
    def paimai_info.deposit(self):
        return self._paimai_info.deposit

    @paimai_info.deposit.setter
    def paimai_info.deposit(self, paimai_info.deposit):
        if isinstance(paimai_info.deposit, int):
            self._paimai_info.deposit = paimai_info.deposit
        else:
            raise TypeError("paimai_info.deposit must be int")

    @property
    def paimai_info.interval(self):
        return self._paimai_info.interval

    @paimai_info.interval.setter
    def paimai_info.interval(self, paimai_info.interval):
        if isinstance(paimai_info.interval, int):
            self._paimai_info.interval = paimai_info.interval
        else:
            raise TypeError("paimai_info.interval must be int")

    @property
    def paimai_info.reserve(self):
        return self._paimai_info.reserve

    @paimai_info.reserve.setter
    def paimai_info.reserve(self, paimai_info.reserve):
        if isinstance(paimai_info.reserve, str):
            self._paimai_info.reserve = paimai_info.reserve
        else:
            raise TypeError("paimai_info.reserve must be str")

    @property
    def paimai_info.valid_hour(self):
        return self._paimai_info.valid_hour

    @paimai_info.valid_hour.setter
    def paimai_info.valid_hour(self, paimai_info.valid_hour):
        if isinstance(paimai_info.valid_hour, int):
            self._paimai_info.valid_hour = paimai_info.valid_hour
        else:
            raise TypeError("paimai_info.valid_hour must be int")

    @property
    def paimai_info.valid_minute(self):
        return self._paimai_info.valid_minute

    @paimai_info.valid_minute.setter
    def paimai_info.valid_minute(self, paimai_info.valid_minute):
        if isinstance(paimai_info.valid_minute, int):
            self._paimai_info.valid_minute = paimai_info.valid_minute
        else:
            raise TypeError("paimai_info.valid_minute must be int")

    @property
    def ms_payment.reference_price(self):
        return self._ms_payment.reference_price

    @ms_payment.reference_price.setter
    def ms_payment.reference_price(self, ms_payment.reference_price):
        if isinstance(ms_payment.reference_price, str):
            self._ms_payment.reference_price = ms_payment.reference_price
        else:
            raise TypeError("ms_payment.reference_price must be str")

    @property
    def ms_payment.voucher_price(self):
        return self._ms_payment.voucher_price

    @ms_payment.voucher_price.setter
    def ms_payment.voucher_price(self, ms_payment.voucher_price):
        if isinstance(ms_payment.voucher_price, str):
            self._ms_payment.voucher_price = ms_payment.voucher_price
        else:
            raise TypeError("ms_payment.voucher_price must be str")

    @property
    def ms_payment.price(self):
        return self._ms_payment.price

    @ms_payment.price.setter
    def ms_payment.price(self, ms_payment.price):
        if isinstance(ms_payment.price, str):
            self._ms_payment.price = ms_payment.price
        else:
            raise TypeError("ms_payment.price must be str")

    @property
    def delivery_time.need_delivery_time(self):
        return self._delivery_time.need_delivery_time

    @delivery_time.need_delivery_time.setter
    def delivery_time.need_delivery_time(self, delivery_time.need_delivery_time):
        if isinstance(delivery_time.need_delivery_time, str):
            self._delivery_time.need_delivery_time = delivery_time.need_delivery_time
        else:
            raise TypeError("delivery_time.need_delivery_time must be str")

    @property
    def delivery_time.delivery_time_type(self):
        return self._delivery_time.delivery_time_type

    @delivery_time.delivery_time_type.setter
    def delivery_time.delivery_time_type(self, delivery_time.delivery_time_type):
        if isinstance(delivery_time.delivery_time_type, str):
            self._delivery_time.delivery_time_type = delivery_time.delivery_time_type
        else:
            raise TypeError("delivery_time.delivery_time_type must be str")

    @property
    def delivery_time.delivery_time(self):
        return self._delivery_time.delivery_time

    @delivery_time.delivery_time.setter
    def delivery_time.delivery_time(self, delivery_time.delivery_time):
        if isinstance(delivery_time.delivery_time, str):
            self._delivery_time.delivery_time = delivery_time.delivery_time
        else:
            raise TypeError("delivery_time.delivery_time must be str")


    def get_api_name(self):
        return "taobao.item.add"

    def to_dict(self):
        request_dict = {}
        if self._approve_status is not None:
            request_dict["approve_status"] = convert_basic(self._approve_status)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

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

        if self._features is not None:
            request_dict["features"] = convert_basic(self._features)

        if self._scenic_ticket_pay_way is not None:
            request_dict["scenic_ticket_pay_way"] = convert_basic(self._scenic_ticket_pay_way)

        if self._scenic_ticket_book_cost is not None:
            request_dict["scenic_ticket_book_cost"] = convert_basic(self._scenic_ticket_book_cost)

        if self._global_stock_type is not None:
            request_dict["global_stock_type"] = convert_basic(self._global_stock_type)

        if self._global_stock_country is not None:
            request_dict["global_stock_country"] = convert_basic(self._global_stock_country)

        if self._global_stock_delivery_place is not None:
            request_dict["global_stock_delivery_place"] = convert_basic(self._global_stock_delivery_place)

        if self._global_stock_tax_free_promise is not None:
            request_dict["global_stock_tax_free_promise"] = convert_basic(self._global_stock_tax_free_promise)

        if self._item_weight is not None:
            request_dict["item_weight"] = convert_basic(self._item_weight)

        if self._item_size is not None:
            request_dict["item_size"] = convert_basic(self._item_size)

        if self._input_custom_cpv is not None:
            request_dict["input_custom_cpv"] = convert_basic(self._input_custom_cpv)

        if self._cpv_memo is not None:
            request_dict["cpv_memo"] = convert_basic(self._cpv_memo)

        if self._support_custom_made is not None:
            request_dict["support_custom_made"] = convert_basic(self._support_custom_made)

        if self._custom_made_type_id is not None:
            request_dict["custom_made_type_id"] = convert_basic(self._custom_made_type_id)

        if self._newprepay is not None:
            request_dict["newprepay"] = convert_basic(self._newprepay)

        if self._barcode is not None:
            request_dict["barcode"] = convert_basic(self._barcode)

        if self._sell_point is not None:
            request_dict["sell_point"] = convert_basic(self._sell_point)

        if self._qualification is not None:
            request_dict["qualification"] = convert_basic(self._qualification)

        if self._o2o_bind_service is not None:
            request_dict["o2o_bind_service"] = convert_basic(self._o2o_bind_service)

        if self._ignorewarning is not None:
            request_dict["ignorewarning"] = convert_basic(self._ignorewarning)

        if self._after_sale_id is not None:
            request_dict["after_sale_id"] = convert_basic(self._after_sale_id)

        if self._change_prop is not None:
            request_dict["change_prop"] = convert_basic(self._change_prop)

        if self._desc_modules is not None:
            request_dict["desc_modules"] = convert_basic(self._desc_modules)

        if self._is_offline is not None:
            request_dict["is_offline"] = convert_basic(self._is_offline)

        if self._wireless_desc is not None:
            request_dict["wireless_desc"] = convert_basic(self._wireless_desc)

        if self._chaoshi_extends_info is not None:
            request_dict["chaoshi_extends_info"] = convert_basic(self._chaoshi_extends_info)

        if self._spu_confirm is not None:
            request_dict["spu_confirm"] = convert_basic(self._spu_confirm)

        if self._video_id is not None:
            request_dict["video_id"] = convert_basic(self._video_id)

        if self._interactive_id is not None:
            request_dict["interactive_id"] = convert_basic(self._interactive_id)

        if self._lease_extends_info is not None:
            request_dict["lease_extends_info"] = convert_basic(self._lease_extends_info)

        if self._brokerage is not None:
            request_dict["brokerage"] = convert_basic(self._brokerage)

        if self._biz_code is not None:
            request_dict["biz_code"] = convert_basic(self._biz_code)

        if self._image_urls is not None:
            request_dict["image_urls"] = convert_basic_list(self._image_urls)

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

        if self._sku_barcode is not None:
            request_dict["sku_barcode"] = convert_basic(self._sku_barcode)

        if self._sku_spec_ids is not None:
            request_dict["sku_spec_ids"] = convert_basic(self._sku_spec_ids)

        if self._sku_delivery_times is not None:
            request_dict["sku_delivery_times"] = convert_basic(self._sku_delivery_times)

        if self._sku_hd_length is not None:
            request_dict["sku_hd_length"] = convert_basic(self._sku_hd_length)

        if self._sku_hd_height is not None:
            request_dict["sku_hd_height"] = convert_basic(self._sku_hd_height)

        if self._sku_hd_lamp_quantity is not None:
            request_dict["sku_hd_lamp_quantity"] = convert_basic(self._sku_hd_lamp_quantity)

        if self._location.state is not None:
            request_dict["location.state"] = convert_basic(self._location.state)

        if self._location.city is not None:
            request_dict["location.city"] = convert_basic(self._location.city)

        if self._food_security.prd_license_no is not None:
            request_dict["food_security.prd_license_no"] = convert_basic(self._food_security.prd_license_no)

        if self._food_security.design_code is not None:
            request_dict["food_security.design_code"] = convert_basic(self._food_security.design_code)

        if self._food_security.factory is not None:
            request_dict["food_security.factory"] = convert_basic(self._food_security.factory)

        if self._food_security.factory_site is not None:
            request_dict["food_security.factory_site"] = convert_basic(self._food_security.factory_site)

        if self._food_security.contact is not None:
            request_dict["food_security.contact"] = convert_basic(self._food_security.contact)

        if self._food_security.mix is not None:
            request_dict["food_security.mix"] = convert_basic(self._food_security.mix)

        if self._food_security.plan_storage is not None:
            request_dict["food_security.plan_storage"] = convert_basic(self._food_security.plan_storage)

        if self._food_security.period is not None:
            request_dict["food_security.period"] = convert_basic(self._food_security.period)

        if self._food_security.food_additive is not None:
            request_dict["food_security.food_additive"] = convert_basic(self._food_security.food_additive)

        if self._food_security.supplier is not None:
            request_dict["food_security.supplier"] = convert_basic(self._food_security.supplier)

        if self._food_security.product_date_start is not None:
            request_dict["food_security.product_date_start"] = convert_basic(self._food_security.product_date_start)

        if self._food_security.product_date_end is not None:
            request_dict["food_security.product_date_end"] = convert_basic(self._food_security.product_date_end)

        if self._food_security.stock_date_start is not None:
            request_dict["food_security.stock_date_start"] = convert_basic(self._food_security.stock_date_start)

        if self._food_security.stock_date_end is not None:
            request_dict["food_security.stock_date_end"] = convert_basic(self._food_security.stock_date_end)

        if self._food_security.health_product_no is not None:
            request_dict["food_security.health_product_no"] = convert_basic(self._food_security.health_product_no)

        if self._locality_life.expirydate is not None:
            request_dict["locality_life.expirydate"] = convert_basic(self._locality_life.expirydate)

        if self._locality_life.network_id is not None:
            request_dict["locality_life.network_id"] = convert_basic(self._locality_life.network_id)

        if self._locality_life.merchant is not None:
            request_dict["locality_life.merchant"] = convert_basic(self._locality_life.merchant)

        if self._locality_life.verification is not None:
            request_dict["locality_life.verification"] = convert_basic(self._locality_life.verification)

        if self._locality_life.refund_ratio is not None:
            request_dict["locality_life.refund_ratio"] = convert_basic(self._locality_life.refund_ratio)

        if self._locality_life.onsale_auto_refund_ratio is not None:
            request_dict["locality_life.onsale_auto_refund_ratio"] = convert_basic(self._locality_life.onsale_auto_refund_ratio)

        if self._locality_life.choose_logis is not None:
            request_dict["locality_life.choose_logis"] = convert_basic(self._locality_life.choose_logis)

        if self._locality_life.refundmafee is not None:
            request_dict["locality_life.refundmafee"] = convert_basic(self._locality_life.refundmafee)

        if self._locality_life.obs is not None:
            request_dict["locality_life.obs"] = convert_basic(self._locality_life.obs)

        if self._locality_life.eticket is not None:
            request_dict["locality_life.eticket"] = convert_basic(self._locality_life.eticket)

        if self._locality_life.version is not None:
            request_dict["locality_life.version"] = convert_basic(self._locality_life.version)

        if self._locality_life.packageid is not None:
            request_dict["locality_life.packageid"] = convert_basic(self._locality_life.packageid)

        if self._paimai_info.mode is not None:
            request_dict["paimai_info.mode"] = convert_basic(self._paimai_info.mode)

        if self._paimai_info.deposit is not None:
            request_dict["paimai_info.deposit"] = convert_basic(self._paimai_info.deposit)

        if self._paimai_info.interval is not None:
            request_dict["paimai_info.interval"] = convert_basic(self._paimai_info.interval)

        if self._paimai_info.reserve is not None:
            request_dict["paimai_info.reserve"] = convert_basic(self._paimai_info.reserve)

        if self._paimai_info.valid_hour is not None:
            request_dict["paimai_info.valid_hour"] = convert_basic(self._paimai_info.valid_hour)

        if self._paimai_info.valid_minute is not None:
            request_dict["paimai_info.valid_minute"] = convert_basic(self._paimai_info.valid_minute)

        if self._ms_payment.reference_price is not None:
            request_dict["ms_payment.reference_price"] = convert_basic(self._ms_payment.reference_price)

        if self._ms_payment.voucher_price is not None:
            request_dict["ms_payment.voucher_price"] = convert_basic(self._ms_payment.voucher_price)

        if self._ms_payment.price is not None:
            request_dict["ms_payment.price"] = convert_basic(self._ms_payment.price)

        if self._delivery_time.need_delivery_time is not None:
            request_dict["delivery_time.need_delivery_time"] = convert_basic(self._delivery_time.need_delivery_time)

        if self._delivery_time.delivery_time_type is not None:
            request_dict["delivery_time.delivery_time_type"] = convert_basic(self._delivery_time.delivery_time_type)

        if self._delivery_time.delivery_time is not None:
            request_dict["delivery_time.delivery_time"] = convert_basic(self._delivery_time.delivery_time)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsConsignOrderNotifyRequest(BaseRequest):

    def __init__(
        self,
        extend_fields: str = None,
        order_item_list: list = None,
        invoice_info_list: list = None,
        receiver_info: object = None,
        car_no: str = None,
        sender_info: object = None,
        picker_id: str = None,
        carriers_name: str = None,
        picker_call: str = None,
        picker_name: str = None,
        transport_mode: str = None,
        deliver_requirements: object = None,
        tms_service_name: str = None,
        tms_service_code: str = None,
        postfee: int = None,
        got_amount: int = None,
        ar_amount: int = None,
        discount_amount: int = None,
        order_amount: int = None,
        alipay_no: str = None,
        order_shop_create_time: datetime = None,
        order_examination_time: datetime = None,
        order_pay_time: datetime = None,
        order_create_time: datetime = None,
        order_priority: int = None,
        order_sub_source: str = None,
        order_source: int = None,
        order_flag: str = None,
        order_type: int = None,
        order_code: str = None,
        store_code: str = None,
        remark: str = None,
        prev_order_code: str = None,
        service_fee: int = None
    ):
        """
            拓展属性
        """
        self._extend_fields = extend_fields
        """
            订单商品信息列表
        """
        self._order_item_list = order_item_list
        """
            发票信息列表
        """
        self._invoice_info_list = invoice_info_list
        """
            收件人信息
        """
        self._receiver_info = receiver_info
        """
            废弃，车牌号
        """
        self._car_no = car_no
        """
            发货方信息
        """
        self._sender_info = sender_info
        """
            废弃，取件人身份证
        """
        self._picker_id = picker_id
        """
            废弃，承运商名称
        """
        self._carriers_name = carriers_name
        """
            废弃，取件人电话
        """
        self._picker_call = picker_call
        """
            废弃，取件人姓名
        """
        self._picker_name = picker_name
        """
            废弃，出库方式（自提，快递，销毁）
        """
        self._transport_mode = transport_mode
        """
            配送要求
        """
        self._deliver_requirements = deliver_requirements
        """
            快递公司名称
        """
        self._tms_service_name = tms_service_name
        """
            快递公司编码，此字段为空时，由菜鸟选择快递配送
        """
        self._tms_service_code = tms_service_code
        """
            快递费用，单位分
        """
        self._postfee = postfee
        """
            订单已付金额，消费者已经支付的金额，单位分
        """
        self._got_amount = got_amount
        """
            订单应收金额，消费者还需要付的金额，单位分
        """
        self._ar_amount = ar_amount
        """
            订单优惠金额，整单优惠金额，单位分
        """
        self._discount_amount = discount_amount
        """
            订单总金额,=总商品金额-订单优惠金额+快递费用，单位分
        """
        self._order_amount = order_amount
        """
            废弃，支付宝交易号
        """
        self._alipay_no = alipay_no
        """
            下单时间，订单在交易平台创建时间
        """
        self._order_shop_create_time = order_shop_create_time
        """
            订单审核时间,ERP创建支付时间
        """
        self._order_examination_time = order_examination_time
        """
            订单支付时间
        """
        self._order_pay_time = order_pay_time
        """
            订单创建时间,ERP创建订单时间
        """
        self._order_create_time = order_create_time
        """
            废弃，订单优先级0 -10，根据订单作业优先级设置，数字越大，优先级越高
        """
        self._order_priority = order_priority
        """
            废弃，交易内部来源，文本透传 WAP(手机);HITAO(嗨淘);TOP(TOP平台);TAOBAO(普通淘宝);JHS(聚划算) 一笔订单可能同时有以上多个标记，则以逗号分隔
        """
        self._order_sub_source = order_sub_source
        """
            订单来源（213 天猫，201 淘宝，214 京东，202 1688 阿里中文站 ，203 苏宁在线，204 亚马逊中国，205 当当，208 1号店，207 唯品会，209 国美在线，210 拍拍，206 易贝ebay，211 聚美优品，212 乐蜂网，215 邮乐，216 凡客，217 优购，218 银泰，219 易讯，221 聚尚网，222 蘑菇街，223 POS门店，301 其他）
        """
        self._order_source = order_source
        """
            订单标识 (1: cod –货到付款，4:invoiceinfo-需要发票)
        """
        self._order_flag = order_flag
        """
            单据类型 201 一般交易出库单 202 B2B交易出库单 502 换货出库单 503 补发出库单
        """
        self._order_type = order_type
        """
            ERP订单号
        """
        self._order_code = order_code
        """
            仓库编码，此字段为空时，由菜鸟路由仓库发货
        """
        self._store_code = store_code
        """
            备注
        """
        self._remark = remark
        """
            前物流订单号，订单类型为502 换货出库单 503 补发出库单时，需求传入此内容
        """
        self._prev_order_code = prev_order_code
        """
            COD服务费，单位分
        """
        self._service_fee = service_fee

    @property
    def extend_fields(self):
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, extend_fields):
        if isinstance(extend_fields, str):
            self._extend_fields = extend_fields
        else:
            raise TypeError("extend_fields must be str")

    @property
    def order_item_list(self):
        return self._order_item_list

    @order_item_list.setter
    def order_item_list(self, order_item_list):
        if isinstance(order_item_list, list):
            self._order_item_list = order_item_list
        else:
            raise TypeError("order_item_list must be list")

    @property
    def invoice_info_list(self):
        return self._invoice_info_list

    @invoice_info_list.setter
    def invoice_info_list(self, invoice_info_list):
        if isinstance(invoice_info_list, list):
            self._invoice_info_list = invoice_info_list
        else:
            raise TypeError("invoice_info_list must be list")

    @property
    def receiver_info(self):
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, receiver_info):
        if isinstance(receiver_info, object):
            self._receiver_info = receiver_info
        else:
            raise TypeError("receiver_info must be object")

    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, car_no):
        if isinstance(car_no, str):
            self._car_no = car_no
        else:
            raise TypeError("car_no must be str")

    @property
    def sender_info(self):
        return self._sender_info

    @sender_info.setter
    def sender_info(self, sender_info):
        if isinstance(sender_info, object):
            self._sender_info = sender_info
        else:
            raise TypeError("sender_info must be object")

    @property
    def picker_id(self):
        return self._picker_id

    @picker_id.setter
    def picker_id(self, picker_id):
        if isinstance(picker_id, str):
            self._picker_id = picker_id
        else:
            raise TypeError("picker_id must be str")

    @property
    def carriers_name(self):
        return self._carriers_name

    @carriers_name.setter
    def carriers_name(self, carriers_name):
        if isinstance(carriers_name, str):
            self._carriers_name = carriers_name
        else:
            raise TypeError("carriers_name must be str")

    @property
    def picker_call(self):
        return self._picker_call

    @picker_call.setter
    def picker_call(self, picker_call):
        if isinstance(picker_call, str):
            self._picker_call = picker_call
        else:
            raise TypeError("picker_call must be str")

    @property
    def picker_name(self):
        return self._picker_name

    @picker_name.setter
    def picker_name(self, picker_name):
        if isinstance(picker_name, str):
            self._picker_name = picker_name
        else:
            raise TypeError("picker_name must be str")

    @property
    def transport_mode(self):
        return self._transport_mode

    @transport_mode.setter
    def transport_mode(self, transport_mode):
        if isinstance(transport_mode, str):
            self._transport_mode = transport_mode
        else:
            raise TypeError("transport_mode must be str")

    @property
    def deliver_requirements(self):
        return self._deliver_requirements

    @deliver_requirements.setter
    def deliver_requirements(self, deliver_requirements):
        if isinstance(deliver_requirements, object):
            self._deliver_requirements = deliver_requirements
        else:
            raise TypeError("deliver_requirements must be object")

    @property
    def tms_service_name(self):
        return self._tms_service_name

    @tms_service_name.setter
    def tms_service_name(self, tms_service_name):
        if isinstance(tms_service_name, str):
            self._tms_service_name = tms_service_name
        else:
            raise TypeError("tms_service_name must be str")

    @property
    def tms_service_code(self):
        return self._tms_service_code

    @tms_service_code.setter
    def tms_service_code(self, tms_service_code):
        if isinstance(tms_service_code, str):
            self._tms_service_code = tms_service_code
        else:
            raise TypeError("tms_service_code must be str")

    @property
    def postfee(self):
        return self._postfee

    @postfee.setter
    def postfee(self, postfee):
        if isinstance(postfee, int):
            self._postfee = postfee
        else:
            raise TypeError("postfee must be int")

    @property
    def got_amount(self):
        return self._got_amount

    @got_amount.setter
    def got_amount(self, got_amount):
        if isinstance(got_amount, int):
            self._got_amount = got_amount
        else:
            raise TypeError("got_amount must be int")

    @property
    def ar_amount(self):
        return self._ar_amount

    @ar_amount.setter
    def ar_amount(self, ar_amount):
        if isinstance(ar_amount, int):
            self._ar_amount = ar_amount
        else:
            raise TypeError("ar_amount must be int")

    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        if isinstance(discount_amount, int):
            self._discount_amount = discount_amount
        else:
            raise TypeError("discount_amount must be int")

    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, order_amount):
        if isinstance(order_amount, int):
            self._order_amount = order_amount
        else:
            raise TypeError("order_amount must be int")

    @property
    def alipay_no(self):
        return self._alipay_no

    @alipay_no.setter
    def alipay_no(self, alipay_no):
        if isinstance(alipay_no, str):
            self._alipay_no = alipay_no
        else:
            raise TypeError("alipay_no must be str")

    @property
    def order_shop_create_time(self):
        return self._order_shop_create_time

    @order_shop_create_time.setter
    def order_shop_create_time(self, order_shop_create_time):
        if isinstance(order_shop_create_time, datetime):
            self._order_shop_create_time = order_shop_create_time
        else:
            raise TypeError("order_shop_create_time must be datetime")

    @property
    def order_examination_time(self):
        return self._order_examination_time

    @order_examination_time.setter
    def order_examination_time(self, order_examination_time):
        if isinstance(order_examination_time, datetime):
            self._order_examination_time = order_examination_time
        else:
            raise TypeError("order_examination_time must be datetime")

    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, order_pay_time):
        if isinstance(order_pay_time, datetime):
            self._order_pay_time = order_pay_time
        else:
            raise TypeError("order_pay_time must be datetime")

    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, order_create_time):
        if isinstance(order_create_time, datetime):
            self._order_create_time = order_create_time
        else:
            raise TypeError("order_create_time must be datetime")

    @property
    def order_priority(self):
        return self._order_priority

    @order_priority.setter
    def order_priority(self, order_priority):
        if isinstance(order_priority, int):
            self._order_priority = order_priority
        else:
            raise TypeError("order_priority must be int")

    @property
    def order_sub_source(self):
        return self._order_sub_source

    @order_sub_source.setter
    def order_sub_source(self, order_sub_source):
        if isinstance(order_sub_source, str):
            self._order_sub_source = order_sub_source
        else:
            raise TypeError("order_sub_source must be str")

    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, order_source):
        if isinstance(order_source, int):
            self._order_source = order_source
        else:
            raise TypeError("order_source must be int")

    @property
    def order_flag(self):
        return self._order_flag

    @order_flag.setter
    def order_flag(self, order_flag):
        if isinstance(order_flag, str):
            self._order_flag = order_flag
        else:
            raise TypeError("order_flag must be str")

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, int):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be int")

    @property
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        if isinstance(order_code, str):
            self._order_code = order_code
        else:
            raise TypeError("order_code must be str")

    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, store_code):
        if isinstance(store_code, str):
            self._store_code = store_code
        else:
            raise TypeError("store_code must be str")

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, remark):
        if isinstance(remark, str):
            self._remark = remark
        else:
            raise TypeError("remark must be str")

    @property
    def prev_order_code(self):
        return self._prev_order_code

    @prev_order_code.setter
    def prev_order_code(self, prev_order_code):
        if isinstance(prev_order_code, str):
            self._prev_order_code = prev_order_code
        else:
            raise TypeError("prev_order_code must be str")

    @property
    def service_fee(self):
        return self._service_fee

    @service_fee.setter
    def service_fee(self, service_fee):
        if isinstance(service_fee, int):
            self._service_fee = service_fee
        else:
            raise TypeError("service_fee must be int")


    def get_api_name(self):
        return "taobao.wlb.wms.consign.order.notify"

    def to_dict(self):
        request_dict = {}
        if self._extend_fields is not None:
            request_dict["extend_fields"] = convert_basic(self._extend_fields)

        if self._order_item_list is not None:
            request_dict["order_item_list"] = convert_struct_list(self._order_item_list)

        if self._invoice_info_list is not None:
            request_dict["invoice_info_list"] = convert_struct_list(self._invoice_info_list)

        if self._receiver_info is not None:
            request_dict["receiver_info"] = convert_struct(self._receiver_info)

        if self._car_no is not None:
            request_dict["car_no"] = convert_basic(self._car_no)

        if self._sender_info is not None:
            request_dict["sender_info"] = convert_struct(self._sender_info)

        if self._picker_id is not None:
            request_dict["picker_id"] = convert_basic(self._picker_id)

        if self._carriers_name is not None:
            request_dict["carriers_name"] = convert_basic(self._carriers_name)

        if self._picker_call is not None:
            request_dict["picker_call"] = convert_basic(self._picker_call)

        if self._picker_name is not None:
            request_dict["picker_name"] = convert_basic(self._picker_name)

        if self._transport_mode is not None:
            request_dict["transport_mode"] = convert_basic(self._transport_mode)

        if self._deliver_requirements is not None:
            request_dict["deliver_requirements"] = convert_struct(self._deliver_requirements)

        if self._tms_service_name is not None:
            request_dict["tms_service_name"] = convert_basic(self._tms_service_name)

        if self._tms_service_code is not None:
            request_dict["tms_service_code"] = convert_basic(self._tms_service_code)

        if self._postfee is not None:
            request_dict["postfee"] = convert_basic(self._postfee)

        if self._got_amount is not None:
            request_dict["got_amount"] = convert_basic(self._got_amount)

        if self._ar_amount is not None:
            request_dict["ar_amount"] = convert_basic(self._ar_amount)

        if self._discount_amount is not None:
            request_dict["discount_amount"] = convert_basic(self._discount_amount)

        if self._order_amount is not None:
            request_dict["order_amount"] = convert_basic(self._order_amount)

        if self._alipay_no is not None:
            request_dict["alipay_no"] = convert_basic(self._alipay_no)

        if self._order_shop_create_time is not None:
            request_dict["order_shop_create_time"] = convert_basic(self._order_shop_create_time)

        if self._order_examination_time is not None:
            request_dict["order_examination_time"] = convert_basic(self._order_examination_time)

        if self._order_pay_time is not None:
            request_dict["order_pay_time"] = convert_basic(self._order_pay_time)

        if self._order_create_time is not None:
            request_dict["order_create_time"] = convert_basic(self._order_create_time)

        if self._order_priority is not None:
            request_dict["order_priority"] = convert_basic(self._order_priority)

        if self._order_sub_source is not None:
            request_dict["order_sub_source"] = convert_basic(self._order_sub_source)

        if self._order_source is not None:
            request_dict["order_source"] = convert_basic(self._order_source)

        if self._order_flag is not None:
            request_dict["order_flag"] = convert_basic(self._order_flag)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._remark is not None:
            request_dict["remark"] = convert_basic(self._remark)

        if self._prev_order_code is not None:
            request_dict["prev_order_code"] = convert_basic(self._prev_order_code)

        if self._service_fee is not None:
            request_dict["service_fee"] = convert_basic(self._service_fee)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoWlbWmsConsignOrderNotifyOrderitemwlbwmsconsignordernotify:
    def __init__(
        self,
        discount_amount: int = None,
        item_price: int = None,
        actual_price: int = None,
        extend_fields: str = None,
        item_quantity: int = None,
        inventory_type: int = None,
        item_ext_code: str = None,
        item_id: str = None,
        owner_user_name: str = None,
        owner_user_id: str = None,
        user_name: str = None,
        user_id: str = None,
        sub_source_code: str = None,
        order_source_code: str = None,
        order_item_id: str = None,
        item_name: str = None,
        shop_code: str = None
    ):
        """
            商品优惠金额
        """
        self.discount_amount = discount_amount
        """
            销售价格
        """
        self.item_price = item_price
        """
            商品成交价格=销售价格-优惠金额
        """
        self.actual_price = actual_price
        """
            订单商品拓展属性数据
        """
        self.extend_fields = extend_fields
        """
            商品数量
        """
        self.item_quantity = item_quantity
        """
            库存类型
        """
        self.inventory_type = inventory_type
        """
            交易平台商品编码
        """
        self.item_ext_code = item_ext_code
        """
            ERP商品ID
        """
        self.item_id = item_id
        """
            货主名称
        """
        self.owner_user_name = owner_user_name
        """
            货主ID
        """
        self.owner_user_id = owner_user_id
        """
            店铺名称
        """
        self.user_name = user_name
        """
            店铺ID
        """
        self.user_id = user_id
        """
            平台子交易编码
        """
        self.sub_source_code = sub_source_code
        """
            平台交易订单编码，如果不传入淘系交易订单，子订单系统自动标示此商品为赠品；
        """
        self.order_source_code = order_source_code
        """
            ERP订单明细行号ID，数字类型
        """
        self.order_item_id = order_item_id
        """
            商品名称
        """
        self.item_name = item_name
        """
            ERP店铺编码
        """
        self.shop_code = shop_code

class TaobaoWlbWmsConsignOrderNotifyOrderitemlistwlbwmsconsignordernotify:
    def __init__(
        self,
        order_item: object = None
    ):
        """
            订单商品信息
        """
        self.order_item = order_item

class TaobaoWlbWmsConsignOrderNotifyItemdetailwlbwmsconsignordernotify:
    def __init__(
        self,
        amount: str = None,
        quantity: int = None,
        price: str = None,
        unit: str = None,
        item_name: str = None
    ):
        """
            金额
        """
        self.amount = amount
        """
            商品数量
        """
        self.quantity = quantity
        """
            商品价格
        """
        self.price = price
        """
            单位
        """
        self.unit = unit
        """
            商品名称
        """
        self.item_name = item_name

class TaobaoWlbWmsConsignOrderNotifyDetaillistwlbwmsconsignordernotify:
    def __init__(
        self,
        item_detail: object = None
    ):
        """
            发票信息
        """
        self.item_detail = item_detail

class TaobaoWlbWmsConsignOrderNotifyInvoicewlbwmsconsignordernotify:
    def __init__(
        self,
        bill_account: str = None,
        bill_title: str = None,
        bill_content: str = None,
        bill_id: int = None,
        bill_type: str = None,
        detail_list: list = None
    ):
        """
            发票金额
        """
        self.bill_account = bill_account
        """
            发票抬头
        """
        self.bill_title = bill_title
        """
            发票内容
        """
        self.bill_content = bill_content
        """
            Erp发票ID
        """
        self.bill_id = bill_id
        """
            发票类型(VINVOICE - 增值税普通发票， EVINVOICE - 电子增票，电子发票仓库不打印)
        """
        self.bill_type = bill_type
        """
            发票明细列表
        """
        self.detail_list = detail_list

class TaobaoWlbWmsConsignOrderNotifyInvoicelistwlbwmsconsignordernotify:
    def __init__(
        self,
        invoice_info: object = None
    ):
        """
            发票信息
        """
        self.invoice_info = invoice_info

class TaobaoWlbWmsConsignOrderNotifyReceiverwlbwmsconsignordernotify:
    def __init__(
        self,
        receiver_phone: str = None,
        receiver_mobile: str = None,
        receiver_nick: str = None,
        receiver_name: str = None,
        receiver_address: str = None,
        receiver_town: str = None,
        receiver_area: str = None,
        receiver_city: str = None,
        receiver_province: str = None,
        receiver_zip_code: str = None
    ):
        """
            收件人电话
        """
        self.receiver_phone = receiver_phone
        """
            收件人手机
        """
        self.receiver_mobile = receiver_mobile
        """
            收件人Nick
        """
        self.receiver_nick = receiver_nick
        """
            收件人名称
        """
        self.receiver_name = receiver_name
        """
            收件方地址
        """
        self.receiver_address = receiver_address
        """
            收件方街道
        """
        self.receiver_town = receiver_town
        """
            收件方区县
        """
        self.receiver_area = receiver_area
        """
            收件方城市
        """
        self.receiver_city = receiver_city
        """
            收件方省份
        """
        self.receiver_province = receiver_province
        """
            收件方邮编
        """
        self.receiver_zip_code = receiver_zip_code

class TaobaoWlbWmsConsignOrderNotifySenderwlbwmsconsignordernotify:
    def __init__(
        self,
        sender_phone: str = None,
        sender_mobile: str = None,
        sender_name: str = None,
        sender_address: str = None,
        sender_area: str = None,
        sender_city: str = None,
        sender_province: str = None,
        sender_zip_code: str = None,
        sender_town: str = None
    ):
        """
            发件方电话
        """
        self.sender_phone = sender_phone
        """
            发件方手机
        """
        self.sender_mobile = sender_mobile
        """
            发件方名称
        """
        self.sender_name = sender_name
        """
            发件方地址
        """
        self.sender_address = sender_address
        """
            发件方区县
        """
        self.sender_area = sender_area
        """
            发件方城市
        """
        self.sender_city = sender_city
        """
            发件方省份
        """
        self.sender_province = sender_province
        """
            发件方邮编
        """
        self.sender_zip_code = sender_zip_code
        """
            发件方镇
        """
        self.sender_town = sender_town

class TaobaoWlbWmsConsignOrderNotifyDeliverrequirementswlbwmsconsignordernotify:
    def __init__(
        self,
        schedule_end: str = None,
        schedule_start: str = None,
        schedule_day: str = None,
        schedule_type: int = None,
        delivery_type: str = None
    ):
        """
            送达结束时间
        """
        self.schedule_end = schedule_end
        """
            送达开始时间
        """
        self.schedule_start = schedule_start
        """
            送达日期
        """
        self.schedule_day = schedule_day
        """
            投递时延要求:  1-工作日 2-节假日 101,当日达102次晨达103次日达 111 活动标  104 预约达
        """
        self.schedule_type = schedule_type
        """
            配送类型： PTPS-常温配送 LLPS-冷链配送
        """
        self.delivery_type = delivery_type


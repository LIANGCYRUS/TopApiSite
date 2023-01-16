from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderCreateRequest(BaseRequest):

    def __init__(
        self,
        attributes: str = None,
        order_item_list: str = None,
        order_flag: str = None,
        order_type: str = None,
        order_sub_type: str = None,
        invoince_info: str = None,
        package_count: int = None,
        tms_info: str = None,
        alipay_no: str = None,
        schedule_type: str = None,
        receiver_info: str = None,
        sender_info: str = None,
        store_code: str = None,
        out_biz_code: str = None,
        prev_order_code: str = None,
        tms_service_code: str = None,
        total_amount: int = None,
        payable_amount: int = None,
        remark: str = None,
        buyer_nick: str = None,
        expect_start_time: datetime = None,
        expect_end_time: datetime = None,
        schedule_start: str = None,
        schedule_end: str = None,
        service_fee: int = None,
        order_code: str = None,
        is_finished: bool = None,
        tms_order_code: str = None
    ):
        """
            该字段暂时保留
        """
        self._attributes = attributes
        """
            订单商品列表： {"order_item_list":[{"trade_code":"可选,淘宝交易订单，并且不是赠品，必须要传订单来源编号"," sub_trade_code ":"可选,淘宝子交易号","item_id":"必须,商品Id","item_code":"必须,商家编码","item_name":"可选,物流宝商品名称","item_quantity":"必选,计划数量","item_price":"必选,物品价格,单位为分","owner_user_nick
":"可选,货主nick 代销模式下会存在","flag":"判断是否为赠品0 不是1是","remarks":"可选,备注","batch_remark":"可选，批次描述信息会把这个信息带给WMS，但不会跟物流宝库存相关联"，"inventory_type":"库存类型1 可销售库存 101 类型用来定义残次品 201 冻结类型库存 301 在途库存","picture_url":"图片Url","distributor_user_nick": "分销商NICK",必选"ext_order_item_code":"可选，外部商品的商家编码"]} ======================================== 如果订单中的商品条目数大于50条的时候，我们会校验，不能创建成功，需要你按照50个一批的数量传，需要分批调用该接口，第二次传的时候，需要带上wlb_order_code和is_finished和order_item_list三个字段是必传的，is_finished为true表示传输完毕，为false表示还没完全传完。
        """
        self._order_item_list = order_item_list
        """
            用字符串格式来表示订单标记列表：比如COD^PRESELL^SPLIT^LIMIT 等，中间用“^”来隔开 ---------------------------------------- 订单标记list（所有字母全部大写）： 1: COD –货到付款 2: LIMIT-限时配送 3: PRESELL-预售 5:COMPLAIN-已投诉 7:SPLIT-拆单， 8:EXCHANGE-换货， 9:VISIT-上门 ， 10: MODIFYTRANSPORT-是否可改配送方式，
: 是否可改配送方式  默认可更改
11 CONSIGN 物流宝代理发货,自动更改发货状态
12: SELLER_AFFORD 是否卖家承担运费 默认是，即没 13: SYNC_RETURN_BILL，同时退回发票
        """
        self._order_flag = order_flag
        """
            订单类型:  （1）NORMAL_OUT ：正常出库  （2）NORMAL_IN：正常入库  （3）RETURN_IN：退货入库  （4）EXCHANGE_OUT：换货出库
        """
        self._order_type = order_type
        """
            订单子类型：  （1）OTHER： 其他  （2）TAOBAO_TRADE： 淘宝交易  （3）OTHER_TRADE：其他交易  （4）ALLCOATE： 调拨  （5）PURCHASE:采购
        """
        self._order_sub_type = order_sub_type
        """
            {"invoince_info": [{"bill_type":"发票类型，必选", "bill_title":"发票抬头，必选", "bill_amount":"发票金额(单位是分)，必选","bill_content":"发票内容，可选"}]}
        """
        self._invoince_info = invoince_info
        """
            包裹件数，入库单和出库单中会用到
        """
        self._package_count = package_count
        """
            出库单中可能会用到
运输公司名称^^^运输公司联系人^^^运输公司运单号^^^运输公司电话^^^运输公司联系人身份证号

========================================
如果某一个字段的数据为空时，必须传NA
        """
        self._tms_info = tms_info
        """
            支付宝交易号
        """
        self._alipay_no = alipay_no
        """
            投递时延要求:  （1）INSTANT_ARRIVED： 当日达  （2）TOMMORROY_MORNING_ARRIVED：次晨达  （3）TOMMORROY_ARRIVED：次日达  （4）工作日：WORK_DAY  （5）节假日：WEEKED_DAY
        """
        self._schedule_type = schedule_type
        """
            收货方信息，必须传， 手机和电话必选其一。
收货方信息：
邮编^^^省^^^市^^^区^^^具体地址^^^收件方名称^^^手机^^^电话

如果某一个字段的数据为空时，必须传NA
        """
        self._receiver_info = receiver_info
        """
            发货方信息，发货方信息必须传， 手机和电话必选其一。 发货方信息：
邮编^^^省^^^市^^^区^^^具体地址^^^收件方名称^^^手机^^^电话
如果某一个字段的数据为空时，必须传NA
        """
        self._sender_info = sender_info
        """
            仓库编码
        """
        self._store_code = store_code
        """
            外部订单业务ID，该编号在isv中是唯一编号， 用来控制并发，去重用
        """
        self._out_biz_code = out_biz_code
        """
            源订单编号
        """
        self._prev_order_code = prev_order_code
        """
            物流公司编码
        """
        self._tms_service_code = tms_service_code
        """
            总金额
        """
        self._total_amount = total_amount
        """
            应收金额，cod订单必选
        """
        self._payable_amount = payable_amount
        """
            备注
        """
        self._remark = remark
        """
            买家呢称
        """
        self._buyer_nick = buyer_nick
        """
            计划开始送达时间  在入库单中可能会使用
        """
        self._expect_start_time = expect_start_time
        """
            期望结束时间，在入库单会使用到
        """
        self._expect_end_time = expect_end_time
        """
            投递时间范围要求,格式'13:20'用分号隔开
        """
        self._schedule_start = schedule_start
        """
            投递时间范围要求,格式'15:20'用分号隔开
        """
        self._schedule_end = schedule_end
        """
            cod服务费，只有cod订单的时候，才需要这个字段
        """
        self._service_fee = service_fee
        """
            物流宝订单编号，该接口约定每次最多只能传50条order_item_list，如果一个物流宝订单超过50条商品的时候，需要批量来调用该接口，第一次调用的时候，wlb_order_code为空，如果第一次创建成功，该接口返回wlb_order_code，其后继续再该订单上添加商品条目，需要带上wlb_order_code，out_biz_code，order_item_list,is_finished四个字段。
        """
        self._order_code = order_code
        """
            该物流宝订单是否已完成，如果完成则设置为true，如果为false，则需要等待继续创建订单商品信息。
        """
        self._is_finished = is_finished
        """
            运单编号，退货单时可能会使用
        """
        self._tms_order_code = tms_order_code

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        if isinstance(attributes, str):
            self._attributes = attributes
        else:
            raise TypeError("attributes must be str")

    @property
    def order_item_list(self):
        return self._order_item_list

    @order_item_list.setter
    def order_item_list(self, order_item_list):
        if isinstance(order_item_list, str):
            self._order_item_list = order_item_list
        else:
            raise TypeError("order_item_list must be str")

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
        if isinstance(order_type, str):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be str")

    @property
    def order_sub_type(self):
        return self._order_sub_type

    @order_sub_type.setter
    def order_sub_type(self, order_sub_type):
        if isinstance(order_sub_type, str):
            self._order_sub_type = order_sub_type
        else:
            raise TypeError("order_sub_type must be str")

    @property
    def invoince_info(self):
        return self._invoince_info

    @invoince_info.setter
    def invoince_info(self, invoince_info):
        if isinstance(invoince_info, str):
            self._invoince_info = invoince_info
        else:
            raise TypeError("invoince_info must be str")

    @property
    def package_count(self):
        return self._package_count

    @package_count.setter
    def package_count(self, package_count):
        if isinstance(package_count, int):
            self._package_count = package_count
        else:
            raise TypeError("package_count must be int")

    @property
    def tms_info(self):
        return self._tms_info

    @tms_info.setter
    def tms_info(self, tms_info):
        if isinstance(tms_info, str):
            self._tms_info = tms_info
        else:
            raise TypeError("tms_info must be str")

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
    def schedule_type(self):
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        if isinstance(schedule_type, str):
            self._schedule_type = schedule_type
        else:
            raise TypeError("schedule_type must be str")

    @property
    def receiver_info(self):
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, receiver_info):
        if isinstance(receiver_info, str):
            self._receiver_info = receiver_info
        else:
            raise TypeError("receiver_info must be str")

    @property
    def sender_info(self):
        return self._sender_info

    @sender_info.setter
    def sender_info(self, sender_info):
        if isinstance(sender_info, str):
            self._sender_info = sender_info
        else:
            raise TypeError("sender_info must be str")

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
    def out_biz_code(self):
        return self._out_biz_code

    @out_biz_code.setter
    def out_biz_code(self, out_biz_code):
        if isinstance(out_biz_code, str):
            self._out_biz_code = out_biz_code
        else:
            raise TypeError("out_biz_code must be str")

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
    def tms_service_code(self):
        return self._tms_service_code

    @tms_service_code.setter
    def tms_service_code(self, tms_service_code):
        if isinstance(tms_service_code, str):
            self._tms_service_code = tms_service_code
        else:
            raise TypeError("tms_service_code must be str")

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        if isinstance(total_amount, int):
            self._total_amount = total_amount
        else:
            raise TypeError("total_amount must be int")

    @property
    def payable_amount(self):
        return self._payable_amount

    @payable_amount.setter
    def payable_amount(self, payable_amount):
        if isinstance(payable_amount, int):
            self._payable_amount = payable_amount
        else:
            raise TypeError("payable_amount must be int")

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
    def buyer_nick(self):
        return self._buyer_nick

    @buyer_nick.setter
    def buyer_nick(self, buyer_nick):
        if isinstance(buyer_nick, str):
            self._buyer_nick = buyer_nick
        else:
            raise TypeError("buyer_nick must be str")

    @property
    def expect_start_time(self):
        return self._expect_start_time

    @expect_start_time.setter
    def expect_start_time(self, expect_start_time):
        if isinstance(expect_start_time, datetime):
            self._expect_start_time = expect_start_time
        else:
            raise TypeError("expect_start_time must be datetime")

    @property
    def expect_end_time(self):
        return self._expect_end_time

    @expect_end_time.setter
    def expect_end_time(self, expect_end_time):
        if isinstance(expect_end_time, datetime):
            self._expect_end_time = expect_end_time
        else:
            raise TypeError("expect_end_time must be datetime")

    @property
    def schedule_start(self):
        return self._schedule_start

    @schedule_start.setter
    def schedule_start(self, schedule_start):
        if isinstance(schedule_start, str):
            self._schedule_start = schedule_start
        else:
            raise TypeError("schedule_start must be str")

    @property
    def schedule_end(self):
        return self._schedule_end

    @schedule_end.setter
    def schedule_end(self, schedule_end):
        if isinstance(schedule_end, str):
            self._schedule_end = schedule_end
        else:
            raise TypeError("schedule_end must be str")

    @property
    def service_fee(self):
        return self._service_fee

    @service_fee.setter
    def service_fee(self, service_fee):
        if isinstance(service_fee, int):
            self._service_fee = service_fee
        else:
            raise TypeError("service_fee must be int")

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
    def is_finished(self):
        return self._is_finished

    @is_finished.setter
    def is_finished(self, is_finished):
        if isinstance(is_finished, bool):
            self._is_finished = is_finished
        else:
            raise TypeError("is_finished must be bool")

    @property
    def tms_order_code(self):
        return self._tms_order_code

    @tms_order_code.setter
    def tms_order_code(self, tms_order_code):
        if isinstance(tms_order_code, str):
            self._tms_order_code = tms_order_code
        else:
            raise TypeError("tms_order_code must be str")


    def get_api_name(self):
        return "taobao.wlb.order.create"

    def to_dict(self):
        request_dict = {}
        if self._attributes is not None:
            request_dict["attributes"] = convert_basic(self._attributes)

        if self._order_item_list is not None:
            request_dict["order_item_list"] = convert_basic(self._order_item_list)

        if self._order_flag is not None:
            request_dict["order_flag"] = convert_basic(self._order_flag)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._order_sub_type is not None:
            request_dict["order_sub_type"] = convert_basic(self._order_sub_type)

        if self._invoince_info is not None:
            request_dict["invoince_info"] = convert_basic(self._invoince_info)

        if self._package_count is not None:
            request_dict["package_count"] = convert_basic(self._package_count)

        if self._tms_info is not None:
            request_dict["tms_info"] = convert_basic(self._tms_info)

        if self._alipay_no is not None:
            request_dict["alipay_no"] = convert_basic(self._alipay_no)

        if self._schedule_type is not None:
            request_dict["schedule_type"] = convert_basic(self._schedule_type)

        if self._receiver_info is not None:
            request_dict["receiver_info"] = convert_basic(self._receiver_info)

        if self._sender_info is not None:
            request_dict["sender_info"] = convert_basic(self._sender_info)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._out_biz_code is not None:
            request_dict["out_biz_code"] = convert_basic(self._out_biz_code)

        if self._prev_order_code is not None:
            request_dict["prev_order_code"] = convert_basic(self._prev_order_code)

        if self._tms_service_code is not None:
            request_dict["tms_service_code"] = convert_basic(self._tms_service_code)

        if self._total_amount is not None:
            request_dict["total_amount"] = convert_basic(self._total_amount)

        if self._payable_amount is not None:
            request_dict["payable_amount"] = convert_basic(self._payable_amount)

        if self._remark is not None:
            request_dict["remark"] = convert_basic(self._remark)

        if self._buyer_nick is not None:
            request_dict["buyer_nick"] = convert_basic(self._buyer_nick)

        if self._expect_start_time is not None:
            request_dict["expect_start_time"] = convert_basic(self._expect_start_time)

        if self._expect_end_time is not None:
            request_dict["expect_end_time"] = convert_basic(self._expect_end_time)

        if self._schedule_start is not None:
            request_dict["schedule_start"] = convert_basic(self._schedule_start)

        if self._schedule_end is not None:
            request_dict["schedule_end"] = convert_basic(self._schedule_end)

        if self._service_fee is not None:
            request_dict["service_fee"] = convert_basic(self._service_fee)

        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._is_finished is not None:
            request_dict["is_finished"] = convert_basic(self._is_finished)

        if self._tms_order_code is not None:
            request_dict["tms_order_code"] = convert_basic(self._tms_order_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


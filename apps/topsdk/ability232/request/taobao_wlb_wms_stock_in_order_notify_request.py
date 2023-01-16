from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsStockInOrderNotifyRequest(BaseRequest):

    def __init__(
        self,
        order_code: str = None,
        store_code: str = None,
        order_type: int = None,
        inbound_type_desc: str = None,
        order_flag: str = None,
        order_create_time: datetime = None,
        supplier_code: str = None,
        supplier_name: str = None,
        tms_service_code: str = None,
        tms_service_name: str = None,
        tms_order_code: str = None,
        prev_order_code: str = None,
        return_reason: str = None,
        expect_start_time: str = None,
        expect_end_time: str = None,
        extend_fields: str = None,
        remark: str = None,
        sender_info: object = None,
        receiver_info: object = None,
        order_item_list: list = None
    ):
        """
            入库单据编码
        """
        self._order_code = order_code
        """
            仓库编码
        """
        self._store_code = store_code
        """
            单据类型 601普通入库单、501销退入库单、302 调拨入库单、904其他入库单、306 B2B入库
        """
        self._order_type = order_type
        """
            可选择性文本透传至WMS，比如加工归还、委外归还、借出归还、内部归还等
        """
        self._inbound_type_desc = inbound_type_desc
        """
            订单标记以逗号分隔：  9:上门退货入库 13: 退货时是否收取发票，默认不收取（即没13为多选项，如1,2,8,9）
        """
        self._order_flag = order_flag
        """
            单据创建时间
        """
        self._order_create_time = order_create_time
        """
            供应商编码，往来单位编码
        """
        self._supplier_code = supplier_code
        """
            供应商名称 ，往来单位名称
        """
        self._supplier_name = supplier_name
        """
            配送公司编码，拒收（非妥投）的销退订单，由ERP填充原单配送公司编码
        """
        self._tms_service_code = tms_service_code
        """
            快递公司名称
        """
        self._tms_service_name = tms_service_name
        """
            运单号&托运单号 1)	入库单支持多运单号录入 2)	销退场景下如果是拒收（非妥投运单）由ERP填充原运单号
        """
        self._tms_order_code = tms_order_code
        """
            来源单据号，如销售退货时填充原销售订单号
        """
        self._prev_order_code = prev_order_code
        """
            销退时请提供退货的原因
        """
        self._return_reason = return_reason
        """
            预期送达开始时间
        """
        self._expect_start_time = expect_start_time
        """
            预期送达结束时间
        """
        self._expect_end_time = expect_end_time
        """
            扩展属性, key-value结构，格式要求： 以英文分号“;”分隔每组key-value，以英文冒号“:”分隔key与value。如果value中带有分号，需要转成下划线“_”，如果带有冒号，需要转成中划线“-”
        """
        self._extend_fields = extend_fields
        """
            备注，销退入库订单需要留言备注填充到此字段
        """
        self._remark = remark
        """
            系统自动生成
        """
        self._sender_info = sender_info
        """
            系统自动生成
        """
        self._receiver_info = receiver_info
        """
            系统自动生成
        """
        self._order_item_list = order_item_list

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
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, int):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be int")

    @property
    def inbound_type_desc(self):
        return self._inbound_type_desc

    @inbound_type_desc.setter
    def inbound_type_desc(self, inbound_type_desc):
        if isinstance(inbound_type_desc, str):
            self._inbound_type_desc = inbound_type_desc
        else:
            raise TypeError("inbound_type_desc must be str")

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
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, order_create_time):
        if isinstance(order_create_time, datetime):
            self._order_create_time = order_create_time
        else:
            raise TypeError("order_create_time must be datetime")

    @property
    def supplier_code(self):
        return self._supplier_code

    @supplier_code.setter
    def supplier_code(self, supplier_code):
        if isinstance(supplier_code, str):
            self._supplier_code = supplier_code
        else:
            raise TypeError("supplier_code must be str")

    @property
    def supplier_name(self):
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, supplier_name):
        if isinstance(supplier_name, str):
            self._supplier_name = supplier_name
        else:
            raise TypeError("supplier_name must be str")

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
    def tms_service_name(self):
        return self._tms_service_name

    @tms_service_name.setter
    def tms_service_name(self, tms_service_name):
        if isinstance(tms_service_name, str):
            self._tms_service_name = tms_service_name
        else:
            raise TypeError("tms_service_name must be str")

    @property
    def tms_order_code(self):
        return self._tms_order_code

    @tms_order_code.setter
    def tms_order_code(self, tms_order_code):
        if isinstance(tms_order_code, str):
            self._tms_order_code = tms_order_code
        else:
            raise TypeError("tms_order_code must be str")

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
    def return_reason(self):
        return self._return_reason

    @return_reason.setter
    def return_reason(self, return_reason):
        if isinstance(return_reason, str):
            self._return_reason = return_reason
        else:
            raise TypeError("return_reason must be str")

    @property
    def expect_start_time(self):
        return self._expect_start_time

    @expect_start_time.setter
    def expect_start_time(self, expect_start_time):
        if isinstance(expect_start_time, str):
            self._expect_start_time = expect_start_time
        else:
            raise TypeError("expect_start_time must be str")

    @property
    def expect_end_time(self):
        return self._expect_end_time

    @expect_end_time.setter
    def expect_end_time(self, expect_end_time):
        if isinstance(expect_end_time, str):
            self._expect_end_time = expect_end_time
        else:
            raise TypeError("expect_end_time must be str")

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
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, remark):
        if isinstance(remark, str):
            self._remark = remark
        else:
            raise TypeError("remark must be str")

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
    def receiver_info(self):
        return self._receiver_info

    @receiver_info.setter
    def receiver_info(self, receiver_info):
        if isinstance(receiver_info, object):
            self._receiver_info = receiver_info
        else:
            raise TypeError("receiver_info must be object")

    @property
    def order_item_list(self):
        return self._order_item_list

    @order_item_list.setter
    def order_item_list(self, order_item_list):
        if isinstance(order_item_list, list):
            self._order_item_list = order_item_list
        else:
            raise TypeError("order_item_list must be list")


    def get_api_name(self):
        return "taobao.wlb.wms.stock.in.order.notify"

    def to_dict(self):
        request_dict = {}
        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._inbound_type_desc is not None:
            request_dict["inbound_type_desc"] = convert_basic(self._inbound_type_desc)

        if self._order_flag is not None:
            request_dict["order_flag"] = convert_basic(self._order_flag)

        if self._order_create_time is not None:
            request_dict["order_create_time"] = convert_basic(self._order_create_time)

        if self._supplier_code is not None:
            request_dict["supplier_code"] = convert_basic(self._supplier_code)

        if self._supplier_name is not None:
            request_dict["supplier_name"] = convert_basic(self._supplier_name)

        if self._tms_service_code is not None:
            request_dict["tms_service_code"] = convert_basic(self._tms_service_code)

        if self._tms_service_name is not None:
            request_dict["tms_service_name"] = convert_basic(self._tms_service_name)

        if self._tms_order_code is not None:
            request_dict["tms_order_code"] = convert_basic(self._tms_order_code)

        if self._prev_order_code is not None:
            request_dict["prev_order_code"] = convert_basic(self._prev_order_code)

        if self._return_reason is not None:
            request_dict["return_reason"] = convert_basic(self._return_reason)

        if self._expect_start_time is not None:
            request_dict["expect_start_time"] = convert_basic(self._expect_start_time)

        if self._expect_end_time is not None:
            request_dict["expect_end_time"] = convert_basic(self._expect_end_time)

        if self._extend_fields is not None:
            request_dict["extend_fields"] = convert_basic(self._extend_fields)

        if self._remark is not None:
            request_dict["remark"] = convert_basic(self._remark)

        if self._sender_info is not None:
            request_dict["sender_info"] = convert_struct(self._sender_info)

        if self._receiver_info is not None:
            request_dict["receiver_info"] = convert_struct(self._receiver_info)

        if self._order_item_list is not None:
            request_dict["order_item_list"] = convert_struct_list(self._order_item_list)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoWlbWmsStockInOrderNotifySenderinfowlbwmsstockinordernotifywl:
    def __init__(
        self,
        sender_phone: str = None,
        sender_mobile: str = None,
        sender_name: str = None,
        sender_code: str = None,
        sender_address: str = None,
        sender_town: str = None,
        sender_area: str = None,
        sender_city: str = None,
        sender_province: str = None,
        sender_zip_code: str = None
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
            发件方名称，销退场景下填写买家名称； 调拨场景下填写调拨出仓库名称；
        """
        self.sender_name = sender_name
        """
            发件方编码，销退场景下填写买家nick，旺旺号等； 调拨场景下填写调拨出仓库编码；
        """
        self.sender_code = sender_code
        """
            发件方地址
        """
        self.sender_address = sender_address
        """
            发件方镇
        """
        self.sender_town = sender_town
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

class TaobaoWlbWmsStockInOrderNotifyReceiverinfowlbwmsstockinordernotifywl:
    def __init__(
        self,
        receiver_phone: str = None,
        receiver_mobile: str = None,
        receiver_name: str = None,
        receiver_address: str = None,
        receiver_area: str = None,
        receiver_city: str = None,
        receiver_province: str = None,
        receiver_zip_code: str = None,
        receiver_town: str = None
    ):
        """
            收件人手机
        """
        self.receiver_phone = receiver_phone
        """
            收件人手机
        """
        self.receiver_mobile = receiver_mobile
        """
            收件人名称
        """
        self.receiver_name = receiver_name
        """
            收件方地址
        """
        self.receiver_address = receiver_address
        """
            收件人区县
        """
        self.receiver_area = receiver_area
        """
            收件人城市
        """
        self.receiver_city = receiver_city
        """
            收件人省份
        """
        self.receiver_province = receiver_province
        """
            收件人邮编
        """
        self.receiver_zip_code = receiver_zip_code
        """
            收件人镇
        """
        self.receiver_town = receiver_town

class TaobaoWlbWmsStockInOrderNotifyOrderitemwlbwmsstockinordernotifywl:
    def __init__(
        self,
        extend_fields: str = None,
        produce_code: str = None,
        due_date: datetime = None,
        produce_date: datetime = None,
        batch_code: str = None,
        purchase_price: int = None,
        item_quantity: int = None,
        inventory_type: int = None,
        item_id: str = None,
        order_item_id: str = None
    ):
        """
            订单商品拓展属性
        """
        self.extend_fields = extend_fields
        """
            生产批号
        """
        self.produce_code = produce_code
        """
            失效日期
        """
        self.due_date = due_date
        """
            生产日期
        """
        self.produce_date = produce_date
        """
            批次编号
        """
        self.batch_code = batch_code
        """
            采购价格
        """
        self.purchase_price = purchase_price
        """
            商品数量
        """
        self.item_quantity = item_quantity
        """
            库存类型 1 正品 101 残次 102 机损 103 箱损 201 冻结库存 301 在途库存
        """
        self.inventory_type = inventory_type
        """
            后端商品ID
        """
        self.item_id = item_id
        """
            ERP单据明细ID
        """
        self.order_item_id = order_item_id

class TaobaoWlbWmsStockInOrderNotifyOrderitemlistwlbwmsstockinordernotifywl:
    def __init__(
        self,
        order_item: object = None
    ):
        """
            系统自动生成
        """
        self.order_item = order_item


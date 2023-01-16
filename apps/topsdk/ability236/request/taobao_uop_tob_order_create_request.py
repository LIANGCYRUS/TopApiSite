from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoUopTobOrderCreateRequest(BaseRequest):

    def __init__(
        self,
        delivery_order: object = None
    ):
        """
            ERP出库对象
        """
        self._delivery_order = delivery_order

    @property
    def delivery_order(self):
        return self._delivery_order

    @delivery_order.setter
    def delivery_order(self, delivery_order):
        if isinstance(delivery_order, object):
            self._delivery_order = delivery_order
        else:
            raise TypeError("delivery_order must be object")


    def get_api_name(self):
        return "taobao.uop.tob.order.create"

    def to_dict(self):
        request_dict = {}
        if self._delivery_order is not None:
            request_dict["delivery_order"] = convert_struct(self._delivery_order)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoUopTobOrderCreateReceiverInfo:
    def __init__(
        self,
        mobile: str = None,
        name: str = None,
        detail_address: str = None,
        town: str = None,
        area: str = None,
        city: str = None,
        province: str = None
    ):
        """
            收货人移动电话
        """
        self.mobile = mobile
        """
            收货人姓名
        """
        self.name = name
        """
            收货人详细地址
        """
        self.detail_address = detail_address
        """
            收货人镇
        """
        self.town = town
        """
            收货人区
        """
        self.area = area
        """
            收货人市
        """
        self.city = city
        """
            收货人省
        """
        self.province = province

class TaobaoUopTobOrderCreateOrderLine:
    def __init__(
        self,
        inventory_type: str = None,
        source_order_code: str = None,
        sub_source_order_code: str = None,
        batch_code: str = None,
        product_date: datetime = None,
        expire_date: datetime = None,
        produce_code: str = None,
        item_quantity: int = None,
        item_code: str = None,
        item_name: str = None,
        item_id: str = None,
        order_line_no: str = None
    ):
        """
            库存类型，ZP=正品、CC=残次
        """
        self.inventory_type = inventory_type
        """
            原交易单，供销平台交易单号、分销平台单号
        """
        self.source_order_code = source_order_code
        """
            子交易单号
        """
        self.sub_source_order_code = sub_source_order_code
        """
            批次编码
        """
        self.batch_code = batch_code
        """
            生产日期，生产日期(YYYY-MM-DD)
        """
        self.product_date = product_date
        """
            过期日期，生产日期(YYYY-MM-DD)
        """
        self.expire_date = expire_date
        """
            生产批号
        """
        self.produce_code = produce_code
        """
            商品数量
        """
        self.item_quantity = item_quantity
        """
            商品编码
        """
        self.item_code = item_code
        """
            商品名称
        """
        self.item_name = item_name
        """
            商品ID
        """
        self.item_id = item_id
        """
            订单行号
        """
        self.order_line_no = order_line_no

class TaobaoUopTobOrderCreateDeliveryOrder:
    def __init__(
        self,
        delivery_order_code: str = None,
        rel_in_bound_order_code: str = None,
        warehouse_code: str = None,
        order_type: str = None,
        arrive_channel_type: str = None,
        create_time: datetime = None,
        receiver_info: object = None,
        logistics_code: str = None,
        logistics_name: str = None,
        last_arrive_date: datetime = None,
        order_line: list = None,
        extend_props: str = None,
        sign_time: str = None,
        is_self_lifting: str = None,
        transport_mode: str = None
    ):
        """
            ERP出库单号,ERP系统内本次出库的唯一标示
        """
        self.delivery_order_code = delivery_order_code
        """
            交接入库单号,例如唯品会入库单号或者门店收货单号、商家仓入库单号等
        """
        self.rel_in_bound_order_code = rel_in_bound_order_code
        """
            发货仓库
        """
        self.warehouse_code = warehouse_code
        """
            单据类型,出库单类型(JYCK=一般交易出库单;HHCK=换货出库单;BFCK=补发出库单;QTCK=其他出库单;TOBCK=TOB出库;BIGTOBCK=大B2B发货)
        """
        self.order_type = order_type
        """
            到货渠道类型，VIP＝1、门店＝2、经销商＝3、大润发=4、猫超=5、零售通=6、AE=7、京东=8、亚马逊=9、经销=10、代理=11、商超=12、其他=99
        """
        self.arrive_channel_type = arrive_channel_type
        """
            发货单创建时间
        """
        self.create_time = create_time
        """
            收货人信息
        """
        self.receiver_info = receiver_info
        """
            物流公司编码
        """
        self.logistics_code = logistics_code
        """
            物流公司名称
        """
        self.logistics_name = logistics_name
        """
            最晚到货时间
        """
        self.last_arrive_date = last_arrive_date
        """
            订单信息
        """
        self.order_line = order_line
        """
            扩展信息
        """
        self.extend_props = extend_props
        """
            收货时间区间
        """
        self.sign_time = sign_time
        """
            是否自提
        """
        self.is_self_lifting = is_self_lifting
        """
            配送方式，1=整车直送、2=拼车直送、3=零担、4=快递、5=自提
        """
        self.transport_mode = transport_mode


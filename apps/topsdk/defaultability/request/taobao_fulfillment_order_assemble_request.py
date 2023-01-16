from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFulfillmentOrderAssembleRequest(BaseRequest):

    def __init__(
        self,
        assemble_orders: list = None,
        type: str = None
    ):
        """
            批量回传集合,一次接口最多40
        """
        self._assemble_orders = assemble_orders
        """
            操作类型，支持参数为MERGE、CANCEL_MERGE。当进行CANCEL_MERGE操作时，只需要传入groupId即可，order_list可以为空
        """
        self._type = type

    @property
    def assemble_orders(self):
        return self._assemble_orders

    @assemble_orders.setter
    def assemble_orders(self, assemble_orders):
        if isinstance(assemble_orders, list):
            self._assemble_orders = assemble_orders
        else:
            raise TypeError("assemble_orders must be list")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")


    def get_api_name(self):
        return "taobao.fulfillment.order.assemble"

    def to_dict(self):
        request_dict = {}
        if self._assemble_orders is not None:
            request_dict["assemble_orders"] = convert_struct_list(self._assemble_orders)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoFulfillmentOrderAssembleOrderGroup:
    def __init__(
        self,
        taobao_sub_order_id: str = None,
        order_type: int = None,
        item_type: int = None,
        order_id: str = None,
        erp_order_id: str = None,
        taobao_parent_order_id: str = None
    ):
        """
            淘宝交易子订单id
        """
        self.taobao_sub_order_id = taobao_sub_order_id
        """
            order_id的类型，0:淘宝交易订单,1: 换货单,2:分销单，3:补货单，4:代发单
        """
        self.order_type = order_type
        """
            商品类型, 0:下单货品，1:赠品，2:其他
        """
        self.item_type = item_type
        """
            淘宝单号可以是交易订单、换货单、补货单、代发单或分销单等，当 order_type=0时，order_id =  taobao_parent_order_id。
        """
        self.order_id = order_id
        """
            erp系统内的订单id
        """
        self.erp_order_id = erp_order_id
        """
            淘宝交易主订单id
        """
        self.taobao_parent_order_id = taobao_parent_order_id

class TaobaoFulfillmentOrderAssembleAssembleOrder:
    def __init__(
        self,
        group_id: str = None,
        order_list: list = None
    ):
        """
            组合id，服务商内部的合单操作id，取消合单会根据group_id进行删除操作。
        """
        self.group_id = group_id
        """
            合单订单列表，一个列表最多200
        """
        self.order_list = order_list


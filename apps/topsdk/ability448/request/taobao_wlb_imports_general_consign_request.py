from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportsGeneralConsignRequest(BaseRequest):

    def __init__(
        self,
        trade_order_id: int = None,
        resource_id: int = None,
        store_code: str = None,
        first_logistics: str = None,
        first_waybillno: str = None,
        sender_id: int = None,
        cancel_id: int = None,
        vas_code: str = None
    ):
        """
            交易订单id
        """
        self._trade_order_id = trade_order_id
        """
            物流资源ID
        """
        self._resource_id = resource_id
        """
            仓库编码
        """
        self._store_code = store_code
        """
            第1段物流承运商
        """
        self._first_logistics = first_logistics
        """
            第1段物流运单号
        """
        self._first_waybillno = first_waybillno
        """
            卖家发货地址库ID；不填的话取默认发货地址；如果填写的senderId对应多个地址，取第一个
        """
        self._sender_id = sender_id
        """
            卖家退货地址库ID；不填写的话取默认退货地址；如果填写的cancelId对应多个地址，取第一个
        """
        self._cancel_id = cancel_id
        """
            增值服务编码.多个以逗号分隔
        """
        self._vas_code = vas_code

    @property
    def trade_order_id(self):
        return self._trade_order_id

    @trade_order_id.setter
    def trade_order_id(self, trade_order_id):
        if isinstance(trade_order_id, int):
            self._trade_order_id = trade_order_id
        else:
            raise TypeError("trade_order_id must be int")

    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        if isinstance(resource_id, int):
            self._resource_id = resource_id
        else:
            raise TypeError("resource_id must be int")

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
    def first_logistics(self):
        return self._first_logistics

    @first_logistics.setter
    def first_logistics(self, first_logistics):
        if isinstance(first_logistics, str):
            self._first_logistics = first_logistics
        else:
            raise TypeError("first_logistics must be str")

    @property
    def first_waybillno(self):
        return self._first_waybillno

    @first_waybillno.setter
    def first_waybillno(self, first_waybillno):
        if isinstance(first_waybillno, str):
            self._first_waybillno = first_waybillno
        else:
            raise TypeError("first_waybillno must be str")

    @property
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        if isinstance(sender_id, int):
            self._sender_id = sender_id
        else:
            raise TypeError("sender_id must be int")

    @property
    def cancel_id(self):
        return self._cancel_id

    @cancel_id.setter
    def cancel_id(self, cancel_id):
        if isinstance(cancel_id, int):
            self._cancel_id = cancel_id
        else:
            raise TypeError("cancel_id must be int")

    @property
    def vas_code(self):
        return self._vas_code

    @vas_code.setter
    def vas_code(self, vas_code):
        if isinstance(vas_code, str):
            self._vas_code = vas_code
        else:
            raise TypeError("vas_code must be str")


    def get_api_name(self):
        return "taobao.wlb.imports.general.consign"

    def to_dict(self):
        request_dict = {}
        if self._trade_order_id is not None:
            request_dict["trade_order_id"] = convert_basic(self._trade_order_id)

        if self._resource_id is not None:
            request_dict["resource_id"] = convert_basic(self._resource_id)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._first_logistics is not None:
            request_dict["first_logistics"] = convert_basic(self._first_logistics)

        if self._first_waybillno is not None:
            request_dict["first_waybillno"] = convert_basic(self._first_waybillno)

        if self._sender_id is not None:
            request_dict["sender_id"] = convert_basic(self._sender_id)

        if self._cancel_id is not None:
            request_dict["cancel_id"] = convert_basic(self._cancel_id)

        if self._vas_code is not None:
            request_dict["vas_code"] = convert_basic(self._vas_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


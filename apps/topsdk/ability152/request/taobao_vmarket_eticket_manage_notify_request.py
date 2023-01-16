from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketManageNotifyRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        notify_method: str = None,
        codemerchant_id: int = None
    ):
        """
            订单编号
        """
        self._order_id = order_id
        """
            需要调用的通知方法，目前仅支持是send（发码）或resend（重新发码）
        """
        self._notify_method = notify_method
        """
            码商ID，如果是码商，必须传，如果是信任卖家，不需要传
        """
        self._codemerchant_id = codemerchant_id

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        if isinstance(order_id, int):
            self._order_id = order_id
        else:
            raise TypeError("order_id must be int")

    @property
    def notify_method(self):
        return self._notify_method

    @notify_method.setter
    def notify_method(self, notify_method):
        if isinstance(notify_method, str):
            self._notify_method = notify_method
        else:
            raise TypeError("notify_method must be str")

    @property
    def codemerchant_id(self):
        return self._codemerchant_id

    @codemerchant_id.setter
    def codemerchant_id(self, codemerchant_id):
        if isinstance(codemerchant_id, int):
            self._codemerchant_id = codemerchant_id
        else:
            raise TypeError("codemerchant_id must be int")


    def get_api_name(self):
        return "taobao.vmarket.eticket.manage.notify"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._notify_method is not None:
            request_dict["notify_method"] = convert_basic(self._notify_method)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


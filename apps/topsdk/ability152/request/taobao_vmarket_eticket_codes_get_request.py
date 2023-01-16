from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketCodesGetRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        codemerchant_id: int = None
    ):
        """
            订单号
        """
        self._order_id = order_id
        """
            码商ID
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
    def codemerchant_id(self):
        return self._codemerchant_id

    @codemerchant_id.setter
    def codemerchant_id(self, codemerchant_id):
        if isinstance(codemerchant_id, int):
            self._codemerchant_id = codemerchant_id
        else:
            raise TypeError("codemerchant_id must be int")


    def get_api_name(self):
        return "taobao.vmarket.eticket.codes.get"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


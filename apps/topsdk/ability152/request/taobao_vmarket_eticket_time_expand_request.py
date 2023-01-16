from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketTimeExpandRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        expand_days: int = None
    ):
        """
            订单ID
        """
        self._order_id = order_id
        """
            延长天数，延长时间=当前过期时间+延长天数
        """
        self._expand_days = expand_days

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
    def expand_days(self):
        return self._expand_days

    @expand_days.setter
    def expand_days(self, expand_days):
        if isinstance(expand_days, int):
            self._expand_days = expand_days
        else:
            raise TypeError("expand_days must be int")


    def get_api_name(self):
        return "taobao.vmarket.eticket.time.expand"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._expand_days is not None:
            request_dict["expand_days"] = convert_basic(self._expand_days)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


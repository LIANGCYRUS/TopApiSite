from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDealerRequisitionorderAgreeRequest(BaseRequest):

    def __init__(
        self,
        dealer_order_id: int = None
    ):
        """
            采购申请/经销采购单编号
        """
        self._dealer_order_id = dealer_order_id

    @property
    def dealer_order_id(self):
        return self._dealer_order_id

    @dealer_order_id.setter
    def dealer_order_id(self, dealer_order_id):
        if isinstance(dealer_order_id, int):
            self._dealer_order_id = dealer_order_id
        else:
            raise TypeError("dealer_order_id must be int")


    def get_api_name(self):
        return "taobao.fenxiao.dealer.requisitionorder.agree"

    def to_dict(self):
        request_dict = {}
        if self._dealer_order_id is not None:
            request_dict["dealer_order_id"] = convert_basic(self._dealer_order_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


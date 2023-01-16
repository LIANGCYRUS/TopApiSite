from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaAscpLogisticsSellerWriteoffRequest(BaseRequest):

    def __init__(
        self,
        lp_order_id: int = None,
        receive_code: str = None
    ):
        """
            所要核销的核销物流单ID，在alibaba.ascp.logistics.seller.orders.get中获取。
        """
        self._lp_order_id = lp_order_id
        """
            核销码
        """
        self._receive_code = receive_code

    @property
    def lp_order_id(self):
        return self._lp_order_id

    @lp_order_id.setter
    def lp_order_id(self, lp_order_id):
        if isinstance(lp_order_id, int):
            self._lp_order_id = lp_order_id
        else:
            raise TypeError("lp_order_id must be int")

    @property
    def receive_code(self):
        return self._receive_code

    @receive_code.setter
    def receive_code(self, receive_code):
        if isinstance(receive_code, str):
            self._receive_code = receive_code
        else:
            raise TypeError("receive_code must be str")


    def get_api_name(self):
        return "alibaba.ascp.logistics.seller.writeoff"

    def to_dict(self):
        request_dict = {}
        if self._lp_order_id is not None:
            request_dict["lp_order_id"] = convert_basic(self._lp_order_id)

        if self._receive_code is not None:
            request_dict["receive_code"] = convert_basic(self._receive_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


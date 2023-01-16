from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoRefundGetRequest(BaseRequest):

    def __init__(
        self,
        sub_order_id: int = None,
        query_seller_refund: bool = None,
        refund_id: int = None
    ):
        """
            要查询的退款对应的分销子订单号
        """
        self._sub_order_id = sub_order_id
        """
            是否查询下游消费者订单对应退款信息
        """
        self._query_seller_refund = query_seller_refund
        """
            退款单id（分销子订单号和退款单id，两者至少必填一个，都填的情况下，以退款单id为准）
        """
        self._refund_id = refund_id

    @property
    def sub_order_id(self):
        return self._sub_order_id

    @sub_order_id.setter
    def sub_order_id(self, sub_order_id):
        if isinstance(sub_order_id, int):
            self._sub_order_id = sub_order_id
        else:
            raise TypeError("sub_order_id must be int")

    @property
    def query_seller_refund(self):
        return self._query_seller_refund

    @query_seller_refund.setter
    def query_seller_refund(self, query_seller_refund):
        if isinstance(query_seller_refund, bool):
            self._query_seller_refund = query_seller_refund
        else:
            raise TypeError("query_seller_refund must be bool")

    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        if isinstance(refund_id, int):
            self._refund_id = refund_id
        else:
            raise TypeError("refund_id must be int")


    def get_api_name(self):
        return "taobao.fenxiao.refund.get"

    def to_dict(self):
        request_dict = {}
        if self._sub_order_id is not None:
            request_dict["sub_order_id"] = convert_basic(self._sub_order_id)

        if self._query_seller_refund is not None:
            request_dict["query_seller_refund"] = convert_basic(self._query_seller_refund)

        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDealerRequisitionorderQueryRequest(BaseRequest):

    def __init__(
        self,
        dealer_order_ids: list = None,
        fields: str = None
    ):
        """
            经销采购单编号。
多个编号用英文符号的逗号隔开。最多支持50个经销采购单编号的查询。
        """
        self._dealer_order_ids = dealer_order_ids
        """
            多个字段用","分隔。 fields 如果为空：返回所有经销采购单对象(dealer_orders)字段。 如果不为空：返回指定采购单对象(dealer_orders)字段。 例1： dealer_order_details.product_id 表示只返回product_id 例2： dealer_order_details 表示只返回明细列表
        """
        self._fields = fields

    @property
    def dealer_order_ids(self):
        return self._dealer_order_ids

    @dealer_order_ids.setter
    def dealer_order_ids(self, dealer_order_ids):
        if isinstance(dealer_order_ids, list):
            self._dealer_order_ids = dealer_order_ids
        else:
            raise TypeError("dealer_order_ids must be list")

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, str):
            self._fields = fields
        else:
            raise TypeError("fields must be str")


    def get_api_name(self):
        return "taobao.fenxiao.dealer.requisitionorder.query"

    def to_dict(self):
        request_dict = {}
        if self._dealer_order_ids is not None:
            request_dict["dealer_order_ids"] = convert_basic_list(self._dealer_order_ids)

        if self._fields is not None:
            request_dict["fields"] = convert_basic(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


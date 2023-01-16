from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradeAmountGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        tid: int = None
    ):
        """
            订单帐务详情需要返回的字段信息，可选值如下：1. TradeAmount中可指定的fields：tid,alipay_no,created,pay_time,end_time,total_fee,payment,post_fee,cod_fee,commission_fee,buyer_obtain_point_fee2. OrderAmount中可指定的fields：order_amounts.oid,order_amounts.title,order_amounts.num_iid,order_amounts.sku_properties_name,order_amounts.sku_id,order_amounts.num,order_amounts.price,order_amounts.discount_fee,order_amounts.adjust_fee,order_amounts.payment,order_amounts.promotion_name3. order_amounts(返回OrderAmount的所有内容)4. promotion_details(指定该值会返回主订单的promotion_details中除id之外的所有字段)
        """
        self._fields = fields
        """
            交易编号
        """
        self._tid = tid

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")

    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, int):
            self._tid = tid
        else:
            raise TypeError("tid must be int")


    def get_api_name(self):
        return "taobao.trade.amount.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


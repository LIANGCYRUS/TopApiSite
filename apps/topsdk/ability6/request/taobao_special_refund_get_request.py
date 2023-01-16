from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSpecialRefundGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        refund_id: int = None
    ):
        """
            需要返回的字段。目前支持有：refund_id, alipay_no, tid, oid, buyer_nick, seller_nick, total_fee, status, created, refund_fee, good_status, has_good_return, payment, reason, desc, num_iid, title, price, num, good_return_time, company_name, sid, address, shipping_type, refund_remind_timeout, refund_phase, refund_version, operation_contraint, attribute, outer_id, sku
        """
        self._fields = fields
        """
            退款单号
        """
        self._refund_id = refund_id

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
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        if isinstance(refund_id, int):
            self._refund_id = refund_id
        else:
            raise TypeError("refund_id must be int")


    def get_api_name(self):
        return "taobao.special.refund.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


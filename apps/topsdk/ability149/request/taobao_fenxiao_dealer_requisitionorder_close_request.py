from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDealerRequisitionorderCloseRequest(BaseRequest):

    def __init__(
        self,
        dealer_order_id: int = None,
        reason: int = None,
        reason_detail: str = None
    ):
        """
            经销采购单编号
        """
        self._dealer_order_id = dealer_order_id
        """
            关闭原因：
1：长时间无法联系到分销商，取消交易。
2：分销商错误提交申请，取消交易。
3：缺货，近段时间都无法发货。
4：分销商恶意提交申请单。
5：其他原因。
        """
        self._reason = reason
        """
            关闭详细原因，字数5-200字
        """
        self._reason_detail = reason_detail

    @property
    def dealer_order_id(self):
        return self._dealer_order_id

    @dealer_order_id.setter
    def dealer_order_id(self, dealer_order_id):
        if isinstance(dealer_order_id, int):
            self._dealer_order_id = dealer_order_id
        else:
            raise TypeError("dealer_order_id must be int")

    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, reason):
        if isinstance(reason, int):
            self._reason = reason
        else:
            raise TypeError("reason must be int")

    @property
    def reason_detail(self):
        return self._reason_detail

    @reason_detail.setter
    def reason_detail(self, reason_detail):
        if isinstance(reason_detail, str):
            self._reason_detail = reason_detail
        else:
            raise TypeError("reason_detail must be str")


    def get_api_name(self):
        return "taobao.fenxiao.dealer.requisitionorder.close"

    def to_dict(self):
        request_dict = {}
        if self._dealer_order_id is not None:
            request_dict["dealer_order_id"] = convert_basic(self._dealer_order_id)

        if self._reason is not None:
            request_dict["reason"] = convert_basic(self._reason)

        if self._reason_detail is not None:
            request_dict["reason_detail"] = convert_basic(self._reason_detail)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoOrderConfirmPaidRequest(BaseRequest):

    def __init__(
        self,
        purchase_order_id: int = None,
        confirm_remark: str = None
    ):
        """
            采购单编号。
        """
        self._purchase_order_id = purchase_order_id
        """
            确认支付信息（字数小于100）
        """
        self._confirm_remark = confirm_remark

    @property
    def purchase_order_id(self):
        return self._purchase_order_id

    @purchase_order_id.setter
    def purchase_order_id(self, purchase_order_id):
        if isinstance(purchase_order_id, int):
            self._purchase_order_id = purchase_order_id
        else:
            raise TypeError("purchase_order_id must be int")

    @property
    def confirm_remark(self):
        return self._confirm_remark

    @confirm_remark.setter
    def confirm_remark(self, confirm_remark):
        if isinstance(confirm_remark, str):
            self._confirm_remark = confirm_remark
        else:
            raise TypeError("confirm_remark must be str")


    def get_api_name(self):
        return "taobao.fenxiao.order.confirm.paid"

    def to_dict(self):
        request_dict = {}
        if self._purchase_order_id is not None:
            request_dict["purchase_order_id"] = convert_basic(self._purchase_order_id)

        if self._confirm_remark is not None:
            request_dict["confirm_remark"] = convert_basic(self._confirm_remark)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


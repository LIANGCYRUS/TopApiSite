from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDealerRequisitionorderRemarkUpdateRequest(BaseRequest):

    def __init__(
        self,
        dealer_order_id: int = None,
        supplier_memo: str = None,
        supplier_memo_flag: int = None
    ):
        """
            经销采购单ID
        """
        self._dealer_order_id = dealer_order_id
        """
            备注留言，可为空
        """
        self._supplier_memo = supplier_memo
        """
            旗子的标记，必选。
1-5之间的数字。
非1-5之间，都采用1作为默认。
1:红色
2:黄色
3:绿色
4:蓝色
5:粉红色
        """
        self._supplier_memo_flag = supplier_memo_flag

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
    def supplier_memo(self):
        return self._supplier_memo

    @supplier_memo.setter
    def supplier_memo(self, supplier_memo):
        if isinstance(supplier_memo, str):
            self._supplier_memo = supplier_memo
        else:
            raise TypeError("supplier_memo must be str")

    @property
    def supplier_memo_flag(self):
        return self._supplier_memo_flag

    @supplier_memo_flag.setter
    def supplier_memo_flag(self, supplier_memo_flag):
        if isinstance(supplier_memo_flag, int):
            self._supplier_memo_flag = supplier_memo_flag
        else:
            raise TypeError("supplier_memo_flag must be int")


    def get_api_name(self):
        return "taobao.fenxiao.dealer.requisitionorder.remark.update"

    def to_dict(self):
        request_dict = {}
        if self._dealer_order_id is not None:
            request_dict["dealer_order_id"] = convert_basic(self._dealer_order_id)

        if self._supplier_memo is not None:
            request_dict["supplier_memo"] = convert_basic(self._supplier_memo)

        if self._supplier_memo_flag is not None:
            request_dict["supplier_memo_flag"] = convert_basic(self._supplier_memo_flag)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


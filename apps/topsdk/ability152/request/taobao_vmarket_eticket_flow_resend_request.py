from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketFlowResendRequest(BaseRequest):

    def __init__(
        self,
        outer_id: str = None,
        biz_type: int = None
    ):
        """
            业务单号
        """
        self._outer_id = outer_id
        """
            业务类型值，可联系淘宝业务运营取得具体值
        """
        self._biz_type = biz_type

    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, int):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be int")


    def get_api_name(self):
        return "taobao.vmarket.eticket.flow.resend"

    def to_dict(self):
        request_dict = {}
        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


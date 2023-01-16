from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketFlowConsumeRequest(BaseRequest):

    def __init__(
        self,
        outer_id: str = None,
        code: str = None,
        biz_type: int = None,
        operator: str = None
    ):
        """
            业务单号
        """
        self._outer_id = outer_id
        """
            凭证码
        """
        self._code = code
        """
            淘宝业务提供的业务类型值，请联系相关业务运营取得
        """
        self._biz_type = biz_type
        """
            核销操作人
        """
        self._operator = operator

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
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if isinstance(code, str):
            self._code = code
        else:
            raise TypeError("code must be str")

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, int):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be int")

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        if isinstance(operator, str):
            self._operator = operator
        else:
            raise TypeError("operator must be str")


    def get_api_name(self):
        return "taobao.vmarket.eticket.flow.consume"

    def to_dict(self):
        request_dict = {}
        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._code is not None:
            request_dict["code"] = convert_basic(self._code)

        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._operator is not None:
            request_dict["operator"] = convert_basic(self._operator)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


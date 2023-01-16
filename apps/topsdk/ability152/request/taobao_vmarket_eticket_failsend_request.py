from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketFailsendRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        token: str = None,
        error_code: int = None,
        error_msg: str = None
    ):
        """
            订单号
        """
        self._order_id = order_id
        """
            发码通知时的token
        """
        self._token = token
        """
            错误码
        """
        self._error_code = error_code
        """
            错误信息
        """
        self._error_msg = error_msg

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        if isinstance(order_id, int):
            self._order_id = order_id
        else:
            raise TypeError("order_id must be int")

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        if isinstance(token, str):
            self._token = token
        else:
            raise TypeError("token must be str")

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        if isinstance(error_code, int):
            self._error_code = error_code
        else:
            raise TypeError("error_code must be int")

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        if isinstance(error_msg, str):
            self._error_msg = error_msg
        else:
            raise TypeError("error_msg must be str")


    def get_api_name(self):
        return "taobao.vmarket.eticket.failsend"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        if self._error_code is not None:
            request_dict["error_code"] = convert_basic(self._error_code)

        if self._error_msg is not None:
            request_dict["error_msg"] = convert_basic(self._error_msg)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


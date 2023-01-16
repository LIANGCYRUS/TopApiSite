from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoEticketMerchantMaFailsendRequest(BaseRequest):

    def __init__(
        self,
        biz_type: int = None,
        outer_id: str = None,
        sub_err_code: str = None,
        sub_err_msg: str = None,
        token: str = None
    ):
        """
            业务类型
        """
        self._biz_type = biz_type
        """
            业务id（订单号）
        """
        self._outer_id = outer_id
        """
            错误原因码
        """
        self._sub_err_code = sub_err_code
        """
            错误码描述
        """
        self._sub_err_msg = sub_err_msg
        """
            需要与发码通知获取的值一致
        """
        self._token = token

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
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")

    @property
    def sub_err_code(self):
        return self._sub_err_code

    @sub_err_code.setter
    def sub_err_code(self, sub_err_code):
        if isinstance(sub_err_code, str):
            self._sub_err_code = sub_err_code
        else:
            raise TypeError("sub_err_code must be str")

    @property
    def sub_err_msg(self):
        return self._sub_err_msg

    @sub_err_msg.setter
    def sub_err_msg(self, sub_err_msg):
        if isinstance(sub_err_msg, str):
            self._sub_err_msg = sub_err_msg
        else:
            raise TypeError("sub_err_msg must be str")

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        if isinstance(token, str):
            self._token = token
        else:
            raise TypeError("token must be str")


    def get_api_name(self):
        return "taobao.eticket.merchant.ma.failsend"

    def to_dict(self):
        request_dict = {}
        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._sub_err_code is not None:
            request_dict["sub_err_code"] = convert_basic(self._sub_err_code)

        if self._sub_err_msg is not None:
            request_dict["sub_err_msg"] = convert_basic(self._sub_err_msg)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


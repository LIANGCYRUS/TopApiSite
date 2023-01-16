from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoEticketMerchantMaReverseRequest(BaseRequest):

    def __init__(
        self,
        biz_type: int = None,
        code: str = None,
        outer_id: str = None,
        pos_id: str = None,
        reverse_num: int = None,
        serial_num: str = None,
        token: str = None
    ):
        """
            业务类型
        """
        self._biz_type = biz_type
        """
            码值
        """
        self._code = code
        """
            业务id（订单号）
        """
        self._outer_id = outer_id
        """
            机具编号，如果核销时有则必传
        """
        self._pos_id = pos_id
        """
            冲正份数，需要与核销份数一致
        """
        self._reverse_num = reverse_num
        """
            需要冲正的核销序列号
        """
        self._serial_num = serial_num
        """
            需要跟发码通知获取到的参数一致
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
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if isinstance(code, str):
            self._code = code
        else:
            raise TypeError("code must be str")

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
    def pos_id(self):
        return self._pos_id

    @pos_id.setter
    def pos_id(self, pos_id):
        if isinstance(pos_id, str):
            self._pos_id = pos_id
        else:
            raise TypeError("pos_id must be str")

    @property
    def reverse_num(self):
        return self._reverse_num

    @reverse_num.setter
    def reverse_num(self, reverse_num):
        if isinstance(reverse_num, int):
            self._reverse_num = reverse_num
        else:
            raise TypeError("reverse_num must be int")

    @property
    def serial_num(self):
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        if isinstance(serial_num, str):
            self._serial_num = serial_num
        else:
            raise TypeError("serial_num must be str")

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
        return "taobao.eticket.merchant.ma.reverse"

    def to_dict(self):
        request_dict = {}
        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._code is not None:
            request_dict["code"] = convert_basic(self._code)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._pos_id is not None:
            request_dict["pos_id"] = convert_basic(self._pos_id)

        if self._reverse_num is not None:
            request_dict["reverse_num"] = convert_basic(self._reverse_num)

        if self._serial_num is not None:
            request_dict["serial_num"] = convert_basic(self._serial_num)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


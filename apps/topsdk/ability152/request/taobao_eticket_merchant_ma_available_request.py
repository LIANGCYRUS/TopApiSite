from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoEticketMerchantMaAvailableRequest(BaseRequest):

    def __init__(
        self,
        biz_type: int = None,
        code: str = None,
        consume_num: int = None,
        outer_id: str = None,
        pos_id: str = None,
        serial_num: str = None,
        token: str = None
    ):
        """
            业务类型
        """
        self._biz_type = biz_type
        """
            需要被核销的码
        """
        self._code = code
        """
            核销份数
        """
        self._consume_num = consume_num
        """
            业务id（订单号）
        """
        self._outer_id = outer_id
        """
            机具编号
        """
        self._pos_id = pos_id
        """
            核销序列号，需要保证唯一
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
    def consume_num(self):
        return self._consume_num

    @consume_num.setter
    def consume_num(self, consume_num):
        if isinstance(consume_num, int):
            self._consume_num = consume_num
        else:
            raise TypeError("consume_num must be int")

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
        return "taobao.eticket.merchant.ma.available"

    def to_dict(self):
        request_dict = {}
        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._code is not None:
            request_dict["code"] = convert_basic(self._code)

        if self._consume_num is not None:
            request_dict["consume_num"] = convert_basic(self._consume_num)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._pos_id is not None:
            request_dict["pos_id"] = convert_basic(self._pos_id)

        if self._serial_num is not None:
            request_dict["serial_num"] = convert_basic(self._serial_num)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


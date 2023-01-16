from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketBeforeconsumeRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        verify_code: str = None,
        token: str = None,
        codemerchant_id: int = None,
        posid: str = None,
        mobile: str = None
    ):
        """
            需要验码的电子凭证订单ID
        """
        self._order_id = order_id
        """
            需要验的码
        """
        self._verify_code = verify_code
        """
            安全验证token，需要和发码通知中的token一致
        """
        self._token = token
        """
            码商ID,是码商的话必须传递,如果是信任卖家不需要传
        """
        self._codemerchant_id = codemerchant_id
        """
            操作员身份ID，如果是码商必须传,如果是信任卖家不需要传
        """
        self._posid = posid
        """
            手机号码后四位,没有特殊说明请不要传
        """
        self._mobile = mobile

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
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        if isinstance(verify_code, str):
            self._verify_code = verify_code
        else:
            raise TypeError("verify_code must be str")

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
    def codemerchant_id(self):
        return self._codemerchant_id

    @codemerchant_id.setter
    def codemerchant_id(self, codemerchant_id):
        if isinstance(codemerchant_id, int):
            self._codemerchant_id = codemerchant_id
        else:
            raise TypeError("codemerchant_id must be int")

    @property
    def posid(self):
        return self._posid

    @posid.setter
    def posid(self, posid):
        if isinstance(posid, str):
            self._posid = posid
        else:
            raise TypeError("posid must be str")

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        if isinstance(mobile, str):
            self._mobile = mobile
        else:
            raise TypeError("mobile must be str")


    def get_api_name(self):
        return "taobao.vmarket.eticket.beforeconsume"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._verify_code is not None:
            request_dict["verify_code"] = convert_basic(self._verify_code)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        if self._posid is not None:
            request_dict["posid"] = convert_basic(self._posid)

        if self._mobile is not None:
            request_dict["mobile"] = convert_basic(self._mobile)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


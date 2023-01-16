from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTopOnceTokenGetRequest(BaseRequest):

    def __init__(
        self,
        sec_token: str = None
    ):
        """
            sec_token
        """
        self._sec_token = sec_token

    @property
    def sec_token(self):
        return self._sec_token

    @sec_token.setter
    def sec_token(self, sec_token):
        if isinstance(sec_token, str):
            self._sec_token = sec_token
        else:
            raise TypeError("sec_token must be str")


    def get_api_name(self):
        return "taobao.top.once.token.get"

    def to_dict(self):
        request_dict = {}
        if self._sec_token is not None:
            request_dict["sec_token"] = convert_basic(self._sec_token)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


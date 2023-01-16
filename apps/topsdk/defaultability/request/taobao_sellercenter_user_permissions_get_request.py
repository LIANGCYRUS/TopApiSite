from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSellercenterUserPermissionsGetRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None
    ):
        """
            用户标识，次入参必须为子账号比如zhangsan:cool。如果只输入主账号zhangsan，将报错。
        """
        self._nick = nick

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, nick):
        if isinstance(nick, str):
            self._nick = nick
        else:
            raise TypeError("nick must be str")


    def get_api_name(self):
        return "taobao.sellercenter.user.permissions.get"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


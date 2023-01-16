from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSellercenterSubuserPermissionsRolesGetRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None
    ):
        """
            子账号昵称(子账号标识)
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
        return "taobao.sellercenter.subuser.permissions.roles.get"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


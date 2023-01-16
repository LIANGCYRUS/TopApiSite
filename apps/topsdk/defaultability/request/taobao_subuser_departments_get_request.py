from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSubuserDepartmentsGetRequest(BaseRequest):

    def __init__(
        self,
        user_nick: str = None
    ):
        """
            主账号用户名
        """
        self._user_nick = user_nick

    @property
    def user_nick(self):
        return self._user_nick

    @user_nick.setter
    def user_nick(self, user_nick):
        if isinstance(user_nick, str):
            self._user_nick = user_nick
        else:
            raise TypeError("user_nick must be str")


    def get_api_name(self):
        return "taobao.subuser.departments.get"

    def to_dict(self):
        request_dict = {}
        if self._user_nick is not None:
            request_dict["user_nick"] = convert_basic(self._user_nick)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


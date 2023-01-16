from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoJushitaJdpUserDeleteRequest(BaseRequest):

    def __init__(
        self,
        user_id: int = None,
        nick: str = None
    ):
        """
            需要删除的用户编号
        """
        self._user_id = user_id
        """
            要删除用户的昵称
        """
        self._nick = nick

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int):
            self._user_id = user_id
        else:
            raise TypeError("user_id must be int")

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
        return "taobao.jushita.jdp.user.delete"

    def to_dict(self):
        request_dict = {}
        if self._user_id is not None:
            request_dict["user_id"] = convert_basic(self._user_id)

        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


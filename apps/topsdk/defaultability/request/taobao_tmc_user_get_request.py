from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcUserGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        nick: str = None,
        user_platform: str = None
    ):
        """
            需返回的字段列表，多个字段以半角逗号分隔。可选值：TmcUser结构体中的所有字段，一定要返回topic。
        """
        self._fields = fields
        """
            用户昵称
        """
        self._nick = nick
        """
            用户所属的平台类型，tbUIC:淘宝用户; icbu: icbu用户;ae:ae用户
        """
        self._user_platform = user_platform

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, nick):
        if isinstance(nick, str):
            self._nick = nick
        else:
            raise TypeError("nick must be str")

    @property
    def user_platform(self):
        return self._user_platform

    @user_platform.setter
    def user_platform(self, user_platform):
        if isinstance(user_platform, str):
            self._user_platform = user_platform
        else:
            raise TypeError("user_platform must be str")


    def get_api_name(self):
        return "taobao.tmc.user.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        if self._user_platform is not None:
            request_dict["user_platform"] = convert_basic(self._user_platform)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


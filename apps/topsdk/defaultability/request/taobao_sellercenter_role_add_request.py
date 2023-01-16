from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSellercenterRoleAddRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None,
        name: str = None,
        description: str = None,
        permission_codes: list = None
    ):
        """
            表示卖家昵称
        """
        self._nick = nick
        """
            角色名
        """
        self._name = name
        """
            角色描述
        """
        self._description = description
        """
            需要授权的权限点permission_code列表,以","分割.其code值可以通过调用taobao.sellercenter.user.permissions.get返回，其中permission.is_authorize=1的权限点可以通过本接口授权给对应角色。
        """
        self._permission_codes = permission_codes

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise TypeError("description must be str")

    @property
    def permission_codes(self):
        return self._permission_codes

    @permission_codes.setter
    def permission_codes(self, permission_codes):
        if isinstance(permission_codes, list):
            self._permission_codes = permission_codes
        else:
            raise TypeError("permission_codes must be list")


    def get_api_name(self):
        return "taobao.sellercenter.role.add"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._description is not None:
            request_dict["description"] = convert_basic(self._description)

        if self._permission_codes is not None:
            request_dict["permission_codes"] = convert_basic_list(self._permission_codes)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


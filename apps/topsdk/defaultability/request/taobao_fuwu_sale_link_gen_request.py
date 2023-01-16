from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFuwuSaleLinkGenRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None,
        param_str: str = None
    ):
        """
            用户需要营销的目标人群中的用户nick
        """
        self._nick = nick
        """
            从服务商后台，营销链接功能中生成的参数串直接复制使用。不要修改，否则抛错。
        """
        self._param_str = param_str

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
    def param_str(self):
        return self._param_str

    @param_str.setter
    def param_str(self, param_str):
        if isinstance(param_str, str):
            self._param_str = param_str
        else:
            raise TypeError("param_str must be str")


    def get_api_name(self):
        return "taobao.fuwu.sale.link.gen"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        if self._param_str is not None:
            request_dict["param_str"] = convert_basic(self._param_str)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


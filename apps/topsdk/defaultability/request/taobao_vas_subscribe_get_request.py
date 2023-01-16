from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVasSubscribeGetRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None,
        article_code: str = None
    ):
        """
            淘宝会员名
        """
        self._nick = nick
        """
            商品编码，从合作伙伴后台（my.open.taobao.com）-收费管理-收费项目列表 能够获得该应用的商品代码
        """
        self._article_code = article_code

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
    def article_code(self):
        return self._article_code

    @article_code.setter
    def article_code(self, article_code):
        if isinstance(article_code, str):
            self._article_code = article_code
        else:
            raise TypeError("article_code must be str")


    def get_api_name(self):
        return "taobao.vas.subscribe.get"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        if self._article_code is not None:
            request_dict["article_code"] = convert_basic(self._article_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


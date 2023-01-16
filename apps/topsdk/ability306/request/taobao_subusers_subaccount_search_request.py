from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSubusersSubaccountSearchRequest(BaseRequest):

    def __init__(
        self,
        main_nick: str = None,
        filter_key: str = None,
        page_size: int = None,
        page_num: int = None
    ):
        """
            主账号登录名
        """
        self._main_nick = main_nick
        """
            根据子账号冒号后缀的搜索词，支持中文单字、英文单词 分词规则搜索。该搜索词必传。如果不需要模糊搜索仅需要分页获取子账号列表，请使用taobao.sellercenter.subusers.page接口
        """
        self._filter_key = filter_key
        """
            页大小，大于1小于200
        """
        self._page_size = page_size
        """
            页码，大于等于1
        """
        self._page_num = page_num

    @property
    def main_nick(self):
        return self._main_nick

    @main_nick.setter
    def main_nick(self, main_nick):
        if isinstance(main_nick, str):
            self._main_nick = main_nick
        else:
            raise TypeError("main_nick must be str")

    @property
    def filter_key(self):
        return self._filter_key

    @filter_key.setter
    def filter_key(self, filter_key):
        if isinstance(filter_key, str):
            self._filter_key = filter_key
        else:
            raise TypeError("filter_key must be str")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        if isinstance(page_num, int):
            self._page_num = page_num
        else:
            raise TypeError("page_num must be int")


    def get_api_name(self):
        return "taobao.subusers.subaccount.search"

    def to_dict(self):
        request_dict = {}
        if self._main_nick is not None:
            request_dict["main_nick"] = convert_basic(self._main_nick)

        if self._filter_key is not None:
            request_dict["filter_key"] = convert_basic(self._filter_key)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_num is not None:
            request_dict["page_num"] = convert_basic(self._page_num)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


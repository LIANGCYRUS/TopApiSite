from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSubusersPageRequest(BaseRequest):

    def __init__(
        self,
        user_nick: str = None,
        account_status: int = None,
        page_size: int = None,
        page_num: int = None
    ):
        """
            主账号用户名
        """
        self._user_nick = user_nick
        """
            可以不传，不传的话和老接口返回数据一样。如果传则根据子账号当前状态筛选 1正常   2冻结  3处罚，如果不传默认都返回
        """
        self._account_status = account_status
        """
            页大小，大于1小于200
        """
        self._page_size = page_size
        """
            页码，大于等于1
        """
        self._page_num = page_num

    @property
    def user_nick(self):
        return self._user_nick

    @user_nick.setter
    def user_nick(self, user_nick):
        if isinstance(user_nick, str):
            self._user_nick = user_nick
        else:
            raise TypeError("user_nick must be str")

    @property
    def account_status(self):
        return self._account_status

    @account_status.setter
    def account_status(self, account_status):
        if isinstance(account_status, int):
            self._account_status = account_status
        else:
            raise TypeError("account_status must be int")

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
        return "taobao.subusers.page"

    def to_dict(self):
        request_dict = {}
        if self._user_nick is not None:
            request_dict["user_nick"] = convert_basic(self._user_nick)

        if self._account_status is not None:
            request_dict["account_status"] = convert_basic(self._account_status)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_num is not None:
            request_dict["page_num"] = convert_basic(self._page_num)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


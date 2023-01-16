from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVasSubscSearchRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None,
        article_code: str = None,
        item_code: str = None,
        start_deadline: datetime = None,
        end_deadline: datetime = None,
        status: int = None,
        autosub: bool = None,
        expire_notice: bool = None,
        page_size: int = None,
        page_no: int = None
    ):
        """
            淘宝会员名
        """
        self._nick = nick
        """
            应用收费代码，从合作伙伴后台（my.open.taobao.com）-收费管理-收费项目列表 能够获得该应用的收费代码
        """
        self._article_code = article_code
        """
            收费项目代码，从合作伙伴后台（my.open.taobao.com）-收费管理-收费项目列表 能够获得收费项目代码
        """
        self._item_code = item_code
        """
            到期时间起始值（当start_deadline和end_deadline都不填写时，默认返回最近90天的数据）
        """
        self._start_deadline = start_deadline
        """
            到期时间结束值
        """
        self._end_deadline = end_deadline
        """
            订购记录状态，1=有效 2=过期 空=全部
        """
        self._status = status
        """
            是否自动续费，true=自动续费 false=非自动续费 空=全部
        """
        self._autosub = autosub
        """
            是否到期提醒，true=到期提醒 false=非到期提醒 空=全部
        """
        self._expire_notice = expire_notice
        """
            一页包含的记录数
        """
        self._page_size = page_size
        """
            页码
        """
        self._page_no = page_no

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

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        if isinstance(item_code, str):
            self._item_code = item_code
        else:
            raise TypeError("item_code must be str")

    @property
    def start_deadline(self):
        return self._start_deadline

    @start_deadline.setter
    def start_deadline(self, start_deadline):
        if isinstance(start_deadline, datetime):
            self._start_deadline = start_deadline
        else:
            raise TypeError("start_deadline must be datetime")

    @property
    def end_deadline(self):
        return self._end_deadline

    @end_deadline.setter
    def end_deadline(self, end_deadline):
        if isinstance(end_deadline, datetime):
            self._end_deadline = end_deadline
        else:
            raise TypeError("end_deadline must be datetime")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, int):
            self._status = status
        else:
            raise TypeError("status must be int")

    @property
    def autosub(self):
        return self._autosub

    @autosub.setter
    def autosub(self, autosub):
        if isinstance(autosub, bool):
            self._autosub = autosub
        else:
            raise TypeError("autosub must be bool")

    @property
    def expire_notice(self):
        return self._expire_notice

    @expire_notice.setter
    def expire_notice(self, expire_notice):
        if isinstance(expire_notice, bool):
            self._expire_notice = expire_notice
        else:
            raise TypeError("expire_notice must be bool")

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")


    def get_api_name(self):
        return "taobao.vas.subsc.search"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        if self._article_code is not None:
            request_dict["article_code"] = convert_basic(self._article_code)

        if self._item_code is not None:
            request_dict["item_code"] = convert_basic(self._item_code)

        if self._start_deadline is not None:
            request_dict["start_deadline"] = convert_basic(self._start_deadline)

        if self._end_deadline is not None:
            request_dict["end_deadline"] = convert_basic(self._end_deadline)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._autosub is not None:
            request_dict["autosub"] = convert_basic(self._autosub)

        if self._expire_notice is not None:
            request_dict["expire_notice"] = convert_basic(self._expire_notice)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


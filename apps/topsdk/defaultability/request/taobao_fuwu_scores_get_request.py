from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFuwuScoresGetRequest(BaseRequest):

    def __init__(
        self,
        date: datetime = None,
        page_size: int = None,
        current_page: int = None
    ):
        """
            评价日期，查询某一天的评价
        """
        self._date = date
        """
            每页获取条数。默认值40，最小值1，最大值100。
        """
        self._page_size = page_size
        """
            当前页
        """
        self._current_page = current_page

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, datetime):
            self._date = date
        else:
            raise TypeError("date must be datetime")

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
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        if isinstance(current_page, int):
            self._current_page = current_page
        else:
            raise TypeError("current_page must be int")


    def get_api_name(self):
        return "taobao.fuwu.scores.get"

    def to_dict(self):
        request_dict = {}
        if self._date is not None:
            request_dict["date"] = convert_basic(self._date)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._current_page is not None:
            request_dict["current_page"] = convert_basic(self._current_page)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


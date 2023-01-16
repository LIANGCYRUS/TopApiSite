from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcGroupsGetRequest(BaseRequest):

    def __init__(
        self,
        group_names: list = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            要查询分组的名称，多个分组用半角逗号分隔，不传代表查询所有分组信息，但不会返回组下面的用户信息。如果应用没有设置分组则返回空。组名不能以default开头，default开头是系统默认的组。
        """
        self._group_names = group_names
        """
            页码
        """
        self._page_no = page_no
        """
            每页返回多少个分组
        """
        self._page_size = page_size

    @property
    def group_names(self):
        return self._group_names

    @group_names.setter
    def group_names(self, group_names):
        if isinstance(group_names, list):
            self._group_names = group_names
        else:
            raise TypeError("group_names must be list")

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")


    def get_api_name(self):
        return "taobao.tmc.groups.get"

    def to_dict(self):
        request_dict = {}
        if self._group_names is not None:
            request_dict["group_names"] = convert_basic_list(self._group_names)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


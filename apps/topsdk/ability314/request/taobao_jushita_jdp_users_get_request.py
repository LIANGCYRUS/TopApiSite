from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoJushitaJdpUsersGetRequest(BaseRequest):

    def __init__(
        self,
        target_appkey: str = None,
        start_modified: datetime = None,
        end_modified: datetime = None,
        page_size: int = None,
        page_no: int = None,
        user_id: int = None
    ):
        """
            普通isv不能传入此参数
        """
        self._target_appkey = target_appkey
        """
            此参数一般不用传，用于查询最后更改时间在某个时间段内的用户
        """
        self._start_modified = start_modified
        """
            此参数一般不用传，用于查询最后更改时间在某个时间段内的用户
        """
        self._end_modified = end_modified
        """
            每页记录数，默认200
        """
        self._page_size = page_size
        """
            当前页数
        """
        self._page_no = page_no
        """
            如果传了user_id表示单条查询
        """
        self._user_id = user_id

    @property
    def target_appkey(self):
        return self._target_appkey

    @target_appkey.setter
    def target_appkey(self, target_appkey):
        if isinstance(target_appkey, str):
            self._target_appkey = target_appkey
        else:
            raise TypeError("target_appkey must be str")

    @property
    def start_modified(self):
        return self._start_modified

    @start_modified.setter
    def start_modified(self, start_modified):
        if isinstance(start_modified, datetime):
            self._start_modified = start_modified
        else:
            raise TypeError("start_modified must be datetime")

    @property
    def end_modified(self):
        return self._end_modified

    @end_modified.setter
    def end_modified(self, end_modified):
        if isinstance(end_modified, datetime):
            self._end_modified = end_modified
        else:
            raise TypeError("end_modified must be datetime")

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

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int):
            self._user_id = user_id
        else:
            raise TypeError("user_id must be int")


    def get_api_name(self):
        return "taobao.jushita.jdp.users.get"

    def to_dict(self):
        request_dict = {}
        if self._target_appkey is not None:
            request_dict["target_appkey"] = convert_basic(self._target_appkey)

        if self._start_modified is not None:
            request_dict["start_modified"] = convert_basic(self._start_modified)

        if self._end_modified is not None:
            request_dict["end_modified"] = convert_basic(self._end_modified)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._user_id is not None:
            request_dict["user_id"] = convert_basic(self._user_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


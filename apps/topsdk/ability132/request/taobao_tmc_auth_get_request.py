from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcAuthGetRequest(BaseRequest):

    def __init__(
        self,
        group: str = None
    ):
        """
            tmc组名
        """
        self._group = group

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        if isinstance(group, str):
            self._group = group
        else:
            raise TypeError("group must be str")


    def get_api_name(self):
        return "taobao.tmc.auth.get"

    def to_dict(self):
        request_dict = {}
        if self._group is not None:
            request_dict["group"] = convert_basic(self._group)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


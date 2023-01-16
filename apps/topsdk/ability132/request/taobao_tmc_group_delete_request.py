from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcGroupDeleteRequest(BaseRequest):

    def __init__(
        self,
        group_name: str = None,
        nicks: list = None,
        user_platform: str = None
    ):
        """
            分组名称，分组删除后，用户的消息将会存储于默认分组中。警告：由于分组已经删除，用户之前未消费的消息将无法再获取。不能以default开头，default开头为系统默认组。
        """
        self._group_name = group_name
        """
            用户列表，不传表示删除整个分组，如果用户全部删除后，也会自动删除整个分组
        """
        self._nicks = nicks
        """
            用户所属于的平台类型，tbUIC:淘宝用户; icbu: icbu用户;ae:ae用户
        """
        self._user_platform = user_platform

    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        if isinstance(group_name, str):
            self._group_name = group_name
        else:
            raise TypeError("group_name must be str")

    @property
    def nicks(self):
        return self._nicks

    @nicks.setter
    def nicks(self, nicks):
        if isinstance(nicks, list):
            self._nicks = nicks
        else:
            raise TypeError("nicks must be list")

    @property
    def user_platform(self):
        return self._user_platform

    @user_platform.setter
    def user_platform(self, user_platform):
        if isinstance(user_platform, str):
            self._user_platform = user_platform
        else:
            raise TypeError("user_platform must be str")


    def get_api_name(self):
        return "taobao.tmc.group.delete"

    def to_dict(self):
        request_dict = {}
        if self._group_name is not None:
            request_dict["group_name"] = convert_basic(self._group_name)

        if self._nicks is not None:
            request_dict["nicks"] = convert_basic_list(self._nicks)

        if self._user_platform is not None:
            request_dict["user_platform"] = convert_basic(self._user_platform)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


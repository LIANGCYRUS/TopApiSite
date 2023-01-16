from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcMessagesConfirmRequest(BaseRequest):

    def __init__(
        self,
        group_name: str = None,
        s_message_ids: list = None,
        f_message_ids: list = None
    ):
        """
            分组名称，不传代表默认分组
        """
        self._group_name = group_name
        """
            处理成功的消息ID列表 最大 200个ID
        """
        self._s_message_ids = s_message_ids
        """
            处理失败的消息ID列表--已废弃，无需传此字段
        """
        self._f_message_ids = f_message_ids

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
    def s_message_ids(self):
        return self._s_message_ids

    @s_message_ids.setter
    def s_message_ids(self, s_message_ids):
        if isinstance(s_message_ids, list):
            self._s_message_ids = s_message_ids
        else:
            raise TypeError("s_message_ids must be list")

    @property
    def f_message_ids(self):
        return self._f_message_ids

    @f_message_ids.setter
    def f_message_ids(self, f_message_ids):
        if isinstance(f_message_ids, list):
            self._f_message_ids = f_message_ids
        else:
            raise TypeError("f_message_ids must be list")


    def get_api_name(self):
        return "taobao.tmc.messages.confirm"

    def to_dict(self):
        request_dict = {}
        if self._group_name is not None:
            request_dict["group_name"] = convert_basic(self._group_name)

        if self._s_message_ids is not None:
            request_dict["s_message_ids"] = convert_basic_list(self._s_message_ids)

        if self._f_message_ids is not None:
            request_dict["f_message_ids"] = convert_basic_list(self._f_message_ids)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


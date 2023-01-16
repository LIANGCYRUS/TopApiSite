from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcTopicGroupAddRequest(BaseRequest):

    def __init__(
        self,
        group_name: str = None,
        topics: list = None
    ):
        """
            消息分组名，如果不存在，会自动创建
        """
        self._group_name = group_name
        """
            消息topic名称，多个以逗号(,)分割
        """
        self._topics = topics

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
    def topics(self):
        return self._topics

    @topics.setter
    def topics(self, topics):
        if isinstance(topics, list):
            self._topics = topics
        else:
            raise TypeError("topics must be list")


    def get_api_name(self):
        return "taobao.tmc.topic.group.add"

    def to_dict(self):
        request_dict = {}
        if self._group_name is not None:
            request_dict["group_name"] = convert_basic(self._group_name)

        if self._topics is not None:
            request_dict["topics"] = convert_basic_list(self._topics)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


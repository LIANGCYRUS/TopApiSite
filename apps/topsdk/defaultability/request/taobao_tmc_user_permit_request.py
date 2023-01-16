from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcUserPermitRequest(BaseRequest):

    def __init__(
        self,
        topics: list = None
    ):
        """
            消息主题列表，用半角逗号分隔。当用户订阅的topic是应用订阅的子集时才需要设置，不设置表示继承应用所订阅的所有topic，一般情况建议不要设置。
        """
        self._topics = topics

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
        return "taobao.tmc.user.permit"

    def to_dict(self):
        request_dict = {}
        if self._topics is not None:
            request_dict["topics"] = convert_basic_list(self._topics)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


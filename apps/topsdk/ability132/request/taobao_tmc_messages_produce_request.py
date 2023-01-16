from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcMessagesProduceRequest(BaseRequest):

    def __init__(
        self,
        messages: list = None
    ):
        """
            tmc消息列表, 最多50条，元素结构与taobao.tmc.message.produce一致，用json表示的消息列表。例如：[{"content": "{\"tid\":1234554321,\"status\":\"X_LOGISTICS_PRINTED\",\"action_time\":\"2014-08-08 18:24:00\",\"seller_nick\": \"向阳aa\",\"operator\":\"小张\"}","topic": "taobao_jds_TradeTrace"},{"content": "{\"tid\":1234554321,\"status\":\"X_LOGISTICS_PRINTED\",\"action_time\":\"2014-08-08 18:24:00\",\"seller_nick\": \"向阳aa\",\"operator\":\"小张\"}","topic": "taobao_jds_TradeTrace"}]
        """
        self._messages = messages

    @property
    def messages(self):
        return self._messages

    @messages.setter
    def messages(self, messages):
        if isinstance(messages, list):
            self._messages = messages
        else:
            raise TypeError("messages must be list")


    def get_api_name(self):
        return "taobao.tmc.messages.produce"

    def to_dict(self):
        request_dict = {}
        if self._messages is not None:
            request_dict["messages"] = convert_struct_list(self._messages)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoTmcMessagesProduceTmcPublishMessage:
    def __init__(
        self,
        content: str = None,
        json_ex_content: str = None,
        target_app_key: str = None,
        target_group: str = None,
        topic: str = None
    ):
        """
            消息内容的JSON表述，必须按照topic的定义来填充
        """
        self.content = content
        """
            消息的扩增属性，用json格式表示
        """
        self.json_ex_content = json_ex_content
        """
            直发消息需要传入目标appkey
        """
        self.target_app_key = target_app_key
        """
            目标分组
        """
        self.target_group = target_group
        """
            消息类型
        """
        self.topic = topic


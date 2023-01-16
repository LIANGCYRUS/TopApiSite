from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcMessageProduceRequest(BaseRequest):

    def __init__(
        self,
        content: str = None,
        ex_content: str = None,
        target_appkey: str = None,
        target_group: str = None,
        topic: str = None,
        media_content: bytes = None,
        media_content2: bytes = None,
        media_content3: bytes = None,
        media_content5: bytes = None,
        media_content4: bytes = None,
        delay_millis: int = None,
        expires_millis: int = None
    ):
        """
            消息内容的JSON表述，必须按照topic的定义来填充
        """
        self._content = content
        """
            消息的扩增属性，用json格式表示
        """
        self._ex_content = ex_content
        """
            直发消息需要传入目标appkey
        """
        self._target_appkey = target_appkey
        """
            目标分组，一般为default
        """
        self._target_group = target_group
        """
            消息类型
        """
        self._topic = topic
        """
            回传的文件内容，目前仅支持jpg,png,bmp,gif,pdf类型的文件，文件最大1M。只有消息中有byte[]类型的数据时，才需要传此字段; 否则不需要传此字段。
        """
        self._media_content = media_content
        """
            回传的文件内容，目前仅支持jpg,png,bmp,gif,pdf类型的文件，文件最大1M。只有消息中有byte[]类型的数据时，才需要传此字段; 否则不需要传此字段。具体对应到沙体中的什么值，请参考消息字段说明。
        """
        self._media_content2 = media_content2
        """
            回传的文件内容，目前仅支持jpg,png,bmp,gif,pdf类型的文件，文件最大1M。只有消息中有byte[]类型的数据时，才需要传此字段; 否则不需要传此字段。具体对应到沙体中的什么值，请参考消息字段说明。
        """
        self._media_content3 = media_content3
        """
            回传的文件内容，目前仅支持jpg,png,bmp,gif,pdf类型的文件，文件最大1M。只有消息中有byte[]类型的数据时，才需要传此字段; 否则不需要传此字段。具体对应到沙体中的什么值，请参考消息字段说明。
        """
        self._media_content5 = media_content5
        """
            回传的文件内容，目前仅支持jpg,png,bmp,gif,pdf类型的文件，文件最大1M。只有消息中有byte[]类型的数据时，才需要传此字段; 否则不需要传此字段。具体对应到沙体中的什么值，请参考消息字段说明。
        """
        self._media_content4 = media_content4
        """
            延时参数 时间戳 预期发送时间
        """
        self._delay_millis = delay_millis
        """
            提前过期 相对时间差 毫秒
        """
        self._expires_millis = expires_millis

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if isinstance(content, str):
            self._content = content
        else:
            raise TypeError("content must be str")

    @property
    def ex_content(self):
        return self._ex_content

    @ex_content.setter
    def ex_content(self, ex_content):
        if isinstance(ex_content, str):
            self._ex_content = ex_content
        else:
            raise TypeError("ex_content must be str")

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
    def target_group(self):
        return self._target_group

    @target_group.setter
    def target_group(self, target_group):
        if isinstance(target_group, str):
            self._target_group = target_group
        else:
            raise TypeError("target_group must be str")

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, topic):
        if isinstance(topic, str):
            self._topic = topic
        else:
            raise TypeError("topic must be str")

    @property
    def media_content(self):
        return self._media_content

    @media_content.setter
    def media_content(self, media_content):
        if isinstance(media_content, bytes):
            self._media_content = media_content
        else:
            raise TypeError("media_content must be bytes")

    @property
    def media_content2(self):
        return self._media_content2

    @media_content2.setter
    def media_content2(self, media_content2):
        if isinstance(media_content2, bytes):
            self._media_content2 = media_content2
        else:
            raise TypeError("media_content2 must be bytes")

    @property
    def media_content3(self):
        return self._media_content3

    @media_content3.setter
    def media_content3(self, media_content3):
        if isinstance(media_content3, bytes):
            self._media_content3 = media_content3
        else:
            raise TypeError("media_content3 must be bytes")

    @property
    def media_content5(self):
        return self._media_content5

    @media_content5.setter
    def media_content5(self, media_content5):
        if isinstance(media_content5, bytes):
            self._media_content5 = media_content5
        else:
            raise TypeError("media_content5 must be bytes")

    @property
    def media_content4(self):
        return self._media_content4

    @media_content4.setter
    def media_content4(self, media_content4):
        if isinstance(media_content4, bytes):
            self._media_content4 = media_content4
        else:
            raise TypeError("media_content4 must be bytes")

    @property
    def delay_millis(self):
        return self._delay_millis

    @delay_millis.setter
    def delay_millis(self, delay_millis):
        if isinstance(delay_millis, int):
            self._delay_millis = delay_millis
        else:
            raise TypeError("delay_millis must be int")

    @property
    def expires_millis(self):
        return self._expires_millis

    @expires_millis.setter
    def expires_millis(self, expires_millis):
        if isinstance(expires_millis, int):
            self._expires_millis = expires_millis
        else:
            raise TypeError("expires_millis must be int")


    def get_api_name(self):
        return "taobao.tmc.message.produce"

    def to_dict(self):
        request_dict = {}
        if self._content is not None:
            request_dict["content"] = convert_basic(self._content)

        if self._ex_content is not None:
            request_dict["ex_content"] = convert_basic(self._ex_content)

        if self._target_appkey is not None:
            request_dict["target_appkey"] = convert_basic(self._target_appkey)

        if self._target_group is not None:
            request_dict["target_group"] = convert_basic(self._target_group)

        if self._topic is not None:
            request_dict["topic"] = convert_basic(self._topic)

        if self._delay_millis is not None:
            request_dict["delay_millis"] = convert_basic(self._delay_millis)

        if self._expires_millis is not None:
            request_dict["expires_millis"] = convert_basic(self._expires_millis)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._media_content is not None:
            file_param_dict["media_content"] = convert_basic(self._media_content)
        if self._media_content2 is not None:
            file_param_dict["media_content2"] = convert_basic(self._media_content2)
        if self._media_content3 is not None:
            file_param_dict["media_content3"] = convert_basic(self._media_content3)
        if self._media_content5 is not None:
            file_param_dict["media_content5"] = convert_basic(self._media_content5)
        if self._media_content4 is not None:
            file_param_dict["media_content4"] = convert_basic(self._media_content4)
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoAppstoreSubscribeGetRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None,
        lease_id: int = None
    ):
        """
            用户昵称
        """
        self._nick = nick
        """
            插件实例ID
        """
        self._lease_id = lease_id

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, nick):
        if isinstance(nick, str):
            self._nick = nick
        else:
            raise TypeError("nick must be str")

    @property
    def lease_id(self):
        return self._lease_id

    @lease_id.setter
    def lease_id(self, lease_id):
        if isinstance(lease_id, int):
            self._lease_id = lease_id
        else:
            raise TypeError("lease_id must be int")


    def get_api_name(self):
        return "taobao.appstore.subscribe.get"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        if self._lease_id is not None:
            request_dict["lease_id"] = convert_basic(self._lease_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


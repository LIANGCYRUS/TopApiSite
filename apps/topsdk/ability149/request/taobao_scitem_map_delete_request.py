from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoScitemMapDeleteRequest(BaseRequest):

    def __init__(
        self,
        sc_item_id: int = None,
        user_nick: str = None
    ):
        """
            后台商品ID
        """
        self._sc_item_id = sc_item_id
        """
            店铺用户nick。 如果该参数为空则删除后端商品与当前调用人的商品映射关系;如果不为空则删除指定用户与后端商品的映射关系
        """
        self._user_nick = user_nick

    @property
    def sc_item_id(self):
        return self._sc_item_id

    @sc_item_id.setter
    def sc_item_id(self, sc_item_id):
        if isinstance(sc_item_id, int):
            self._sc_item_id = sc_item_id
        else:
            raise TypeError("sc_item_id must be int")

    @property
    def user_nick(self):
        return self._user_nick

    @user_nick.setter
    def user_nick(self, user_nick):
        if isinstance(user_nick, str):
            self._user_nick = user_nick
        else:
            raise TypeError("user_nick must be str")


    def get_api_name(self):
        return "taobao.scitem.map.delete"

    def to_dict(self):
        request_dict = {}
        if self._sc_item_id is not None:
            request_dict["sc_item_id"] = convert_basic(self._sc_item_id)

        if self._user_nick is not None:
            request_dict["user_nick"] = convert_basic(self._user_nick)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


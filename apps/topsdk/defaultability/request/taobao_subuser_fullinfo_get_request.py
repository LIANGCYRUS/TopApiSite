from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSubuserFullinfoGetRequest(BaseRequest):

    def __init__(
        self,
        sub_nick: str = None,
        sub_id: int = None,
        fields: list = None
    ):
        """
            子账号用户名（传参中sub_id和sub_nick至少需要其中一个，若sub_id与sub_nick同时传入并且合法，那么sub_nick优先，以sub_nick查询子账号）
        """
        self._sub_nick = sub_nick
        """
            子账号ID（传参中sub_id和sub_nick至少需要其中一个，若sub_id与sub_nick同时传入并且合法，那么sub_nick优先，以sub_nick查询子账号）
        """
        self._sub_id = sub_id
        """
            传入所需要的参数信息（若不需要获取子账号或主账号的企业邮箱地址，则无需传入该参数；若需要获取子账号或主账号的企业邮箱地址，则需要传入fields；可选参数值为subuser_email和user_email，传入其他参数值均无效；两个参数都需要则以逗号隔开传入即可，例如：subuser_email,user_email）
        """
        self._fields = fields

    @property
    def sub_nick(self):
        return self._sub_nick

    @sub_nick.setter
    def sub_nick(self, sub_nick):
        if isinstance(sub_nick, str):
            self._sub_nick = sub_nick
        else:
            raise TypeError("sub_nick must be str")

    @property
    def sub_id(self):
        return self._sub_id

    @sub_id.setter
    def sub_id(self, sub_id):
        if isinstance(sub_id, int):
            self._sub_id = sub_id
        else:
            raise TypeError("sub_id must be int")

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")


    def get_api_name(self):
        return "taobao.subuser.fullinfo.get"

    def to_dict(self):
        request_dict = {}
        if self._sub_nick is not None:
            request_dict["sub_nick"] = convert_basic(self._sub_nick)

        if self._sub_id is not None:
            request_dict["sub_id"] = convert_basic(self._sub_id)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


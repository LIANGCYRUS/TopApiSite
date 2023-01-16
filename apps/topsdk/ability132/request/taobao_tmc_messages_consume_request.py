from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTmcMessagesConsumeRequest(BaseRequest):

    def __init__(
        self,
        group_name: str = None,
        quantity: int = None
    ):
        """
            用户分组名称，不传表示消费默认分组，如果应用没有设置用户分组，传入分组名称将会返回错误
        """
        self._group_name = group_name
        """
            每次批量消费消息的条数，最小值：10；最大值：200
        """
        self._quantity = quantity

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
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
        else:
            raise TypeError("quantity must be int")


    def get_api_name(self):
        return "taobao.tmc.messages.consume"

    def to_dict(self):
        request_dict = {}
        if self._group_name is not None:
            request_dict["group_name"] = convert_basic(self._group_name)

        if self._quantity is not None:
            request_dict["quantity"] = convert_basic(self._quantity)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


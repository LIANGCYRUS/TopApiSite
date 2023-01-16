from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbStoresBaseinfoGetRequest(BaseRequest):

    def __init__(
        self,
        type: int = None
    ):
        """
            0.商家仓库.1.菜鸟仓库.2全部被划分的仓库
        """
        self._type = type

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")


    def get_api_name(self):
        return "taobao.wlb.stores.baseinfo.get"

    def to_dict(self):
        request_dict = {}
        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


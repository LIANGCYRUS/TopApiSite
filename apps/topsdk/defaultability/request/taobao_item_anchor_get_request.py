from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemAnchorGetRequest(BaseRequest):

    def __init__(
        self,
        type: int = None,
        cat_id: int = None
    ):
        """
            宝贝模板类型是人工打标还是自动打标：人工打标为1，自动打标为0.人工和自动打标为-1.(最小值：-1，最大值：1)
        """
        self._type = type
        """
            对应类目编号
        """
        self._cat_id = cat_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")

    @property
    def cat_id(self):
        return self._cat_id

    @cat_id.setter
    def cat_id(self, cat_id):
        if isinstance(cat_id, int):
            self._cat_id = cat_id
        else:
            raise TypeError("cat_id must be int")


    def get_api_name(self):
        return "taobao.item.anchor.get"

    def to_dict(self):
        request_dict = {}
        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._cat_id is not None:
            request_dict["cat_id"] = convert_basic(self._cat_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


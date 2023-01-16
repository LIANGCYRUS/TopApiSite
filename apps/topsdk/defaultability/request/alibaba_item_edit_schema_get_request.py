from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaItemEditSchemaGetRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        biz_type: str = None,
        fields: list = None
    ):
        """
            商品ID
        """
        self._item_id = item_id
        """
            业务扩展参数，需与平台约定好
        """
        self._biz_type = biz_type
        """
            制定返回schema中field字段列表，可用于裁剪返回的schema信息。不填则为全部field
        """
        self._fields = fields

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, int):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be int")

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, str):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be str")

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
        return "alibaba.item.edit.schema.get"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


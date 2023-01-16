from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemSimpleschemaUpdateRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        schema_xml_fields: str = None
    ):
        """
            商品id
        """
        self._item_id = item_id
        """
            编辑商品时提交的xml信息
        """
        self._schema_xml_fields = schema_xml_fields

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
    def schema_xml_fields(self):
        return self._schema_xml_fields

    @schema_xml_fields.setter
    def schema_xml_fields(self, schema_xml_fields):
        if isinstance(schema_xml_fields, str):
            self._schema_xml_fields = schema_xml_fields
        else:
            raise TypeError("schema_xml_fields must be str")


    def get_api_name(self):
        return "tmall.item.simpleschema.update"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._schema_xml_fields is not None:
            request_dict["schema_xml_fields"] = convert_basic(self._schema_xml_fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


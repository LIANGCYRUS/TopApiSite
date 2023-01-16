from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemSimpleschemaAddRequest(BaseRequest):

    def __init__(
        self,
        schema_xml_fields: str = None
    ):
        """
            根据tmall.item.add.simpleschema.get生成的商品发布规则入参数据
        """
        self._schema_xml_fields = schema_xml_fields

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
        return "tmall.item.simpleschema.add"

    def to_dict(self):
        request_dict = {}
        if self._schema_xml_fields is not None:
            request_dict["schema_xml_fields"] = convert_basic(self._schema_xml_fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


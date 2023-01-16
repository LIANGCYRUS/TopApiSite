from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaGpuSchemaUpdateRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        schema_xml_fields: str = None,
        provider_id: int = None
    ):
        """
            产品ID
        """
        self._product_id = product_id
        """
            更新产品提交的schema数据
        """
        self._schema_xml_fields = schema_xml_fields
        """
            当前用户所在渠道如0代表天猫，8代表淘宝
        """
        self._provider_id = provider_id

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self._product_id = product_id
        else:
            raise TypeError("product_id must be int")

    @property
    def schema_xml_fields(self):
        return self._schema_xml_fields

    @schema_xml_fields.setter
    def schema_xml_fields(self, schema_xml_fields):
        if isinstance(schema_xml_fields, str):
            self._schema_xml_fields = schema_xml_fields
        else:
            raise TypeError("schema_xml_fields must be str")

    @property
    def provider_id(self):
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        if isinstance(provider_id, int):
            self._provider_id = provider_id
        else:
            raise TypeError("provider_id must be int")


    def get_api_name(self):
        return "alibaba.gpu.schema.update"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._schema_xml_fields is not None:
            request_dict["schema_xml_fields"] = convert_basic(self._schema_xml_fields)

        if self._provider_id is not None:
            request_dict["provider_id"] = convert_basic(self._provider_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


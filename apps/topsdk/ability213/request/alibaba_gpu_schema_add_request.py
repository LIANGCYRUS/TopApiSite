from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaGpuSchemaAddRequest(BaseRequest):

    def __init__(
        self,
        leaf_cat_id: int = None,
        brand_id: int = None,
        schema_xml_fields: str = None,
        provider_id: int = None
    ):
        """
            叶子类目ID
        """
        self._leaf_cat_id = leaf_cat_id
        """
            品牌ID
        """
        self._brand_id = brand_id
        """
            根据alibaba.gpu.add.schema.get获取的规则提交上来的schema
        """
        self._schema_xml_fields = schema_xml_fields
        """
            当前用户所在渠道如0代表天猫，8代表淘宝
        """
        self._provider_id = provider_id

    @property
    def leaf_cat_id(self):
        return self._leaf_cat_id

    @leaf_cat_id.setter
    def leaf_cat_id(self, leaf_cat_id):
        if isinstance(leaf_cat_id, int):
            self._leaf_cat_id = leaf_cat_id
        else:
            raise TypeError("leaf_cat_id must be int")

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        if isinstance(brand_id, int):
            self._brand_id = brand_id
        else:
            raise TypeError("brand_id must be int")

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
        return "alibaba.gpu.schema.add"

    def to_dict(self):
        request_dict = {}
        if self._leaf_cat_id is not None:
            request_dict["leaf_cat_id"] = convert_basic(self._leaf_cat_id)

        if self._brand_id is not None:
            request_dict["brand_id"] = convert_basic(self._brand_id)

        if self._schema_xml_fields is not None:
            request_dict["schema_xml_fields"] = convert_basic(self._schema_xml_fields)

        if self._provider_id is not None:
            request_dict["provider_id"] = convert_basic(self._provider_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


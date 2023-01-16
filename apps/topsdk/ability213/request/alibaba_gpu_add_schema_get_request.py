from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaGpuAddSchemaGetRequest(BaseRequest):

    def __init__(
        self,
        leaf_cat_id: int = None,
        brand_id: int = None,
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
    def provider_id(self):
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        if isinstance(provider_id, int):
            self._provider_id = provider_id
        else:
            raise TypeError("provider_id must be int")


    def get_api_name(self):
        return "alibaba.gpu.add.schema.get"

    def to_dict(self):
        request_dict = {}
        if self._leaf_cat_id is not None:
            request_dict["leaf_cat_id"] = convert_basic(self._leaf_cat_id)

        if self._brand_id is not None:
            request_dict["brand_id"] = convert_basic(self._brand_id)

        if self._provider_id is not None:
            request_dict["provider_id"] = convert_basic(self._provider_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


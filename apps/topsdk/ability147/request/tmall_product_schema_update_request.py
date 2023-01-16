from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallProductSchemaUpdateRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        xml_data: str = None
    ):
        """
            产品编号
        """
        self._product_id = product_id
        """
            根据tmall.product.update.schema.get生成的产品更新规则入参数据
        """
        self._xml_data = xml_data

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
    def xml_data(self):
        return self._xml_data

    @xml_data.setter
    def xml_data(self, xml_data):
        if isinstance(xml_data, str):
            self._xml_data = xml_data
        else:
            raise TypeError("xml_data must be str")


    def get_api_name(self):
        return "tmall.product.schema.update"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._xml_data is not None:
            request_dict["xml_data"] = convert_basic(self._xml_data)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


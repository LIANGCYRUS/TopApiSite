from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductSkuDeleteRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        properties: str = None
    ):
        """
            产品id
        """
        self._product_id = product_id
        """
            sku属性
        """
        self._properties = properties

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
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        if isinstance(properties, str):
            self._properties = properties
        else:
            raise TypeError("properties must be str")


    def get_api_name(self):
        return "taobao.fenxiao.product.sku.delete"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemSchemaAddRequest(BaseRequest):

    def __init__(
        self,
        category_id: int = None,
        product_id: int = None,
        xml_data: str = None
    ):
        """
            商品发布的目标类目，必须是叶子类目
        """
        self._category_id = category_id
        """
            发布商品的productId，如果tmall.product.match.schema.get获取到得字段为空，这个参数传入0，否则需要通过tmall.product.schema.match查询到得可用productId
        """
        self._product_id = product_id
        """
            根据tmall.item.add.schema.get生成的商品发布规则入参数据
        """
        self._xml_data = xml_data

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int):
            self._category_id = category_id
        else:
            raise TypeError("category_id must be int")

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
        return "tmall.item.schema.add"

    def to_dict(self):
        request_dict = {}
        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._xml_data is not None:
            request_dict["xml_data"] = convert_basic(self._xml_data)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


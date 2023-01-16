from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallProductSchemaMatchRequest(BaseRequest):

    def __init__(
        self,
        category_id: int = None,
        propvalues: str = None
    ):
        """
            商品发布的目标类目，必须是叶子类目
        """
        self._category_id = category_id
        """
            根据tmall.product.match.schema.get获取到的模板，ISV将需要的字段填充好相应的值结果XML。
        """
        self._propvalues = propvalues

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
    def propvalues(self):
        return self._propvalues

    @propvalues.setter
    def propvalues(self, propvalues):
        if isinstance(propvalues, str):
            self._propvalues = propvalues
        else:
            raise TypeError("propvalues must be str")


    def get_api_name(self):
        return "tmall.product.schema.match"

    def to_dict(self):
        request_dict = {}
        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._propvalues is not None:
            request_dict["propvalues"] = convert_basic(self._propvalues)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


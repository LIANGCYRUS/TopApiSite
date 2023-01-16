from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureCategoryUpdateRequest(BaseRequest):

    def __init__(
        self,
        category_id: int = None,
        category_name: str = None,
        parent_id: int = None
    ):
        """
            要更新的图片分类的id
        """
        self._category_id = category_id
        """
            图片分类的新名字，最大长度20字符，不能为空
        """
        self._category_name = category_name
        """
            图片分类的新父分类id
        """
        self._parent_id = parent_id

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
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        if isinstance(category_name, str):
            self._category_name = category_name
        else:
            raise TypeError("category_name must be str")

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        if isinstance(parent_id, int):
            self._parent_id = parent_id
        else:
            raise TypeError("parent_id must be int")


    def get_api_name(self):
        return "taobao.picture.category.update"

    def to_dict(self):
        request_dict = {}
        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._category_name is not None:
            request_dict["category_name"] = convert_basic(self._category_name)

        if self._parent_id is not None:
            request_dict["parent_id"] = convert_basic(self._parent_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


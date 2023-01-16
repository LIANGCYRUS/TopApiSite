from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureCategoryAddRequest(BaseRequest):

    def __init__(
        self,
        picture_category_name: str = None,
        parent_id: int = None
    ):
        """
            图片分类名称，最大长度20字符，中文字符算2个字符，不能为空
        """
        self._picture_category_name = picture_category_name
        """
            图片分类的父分类,一级分类的parent_id为0,二级分类的则为其父分类的picture_category_id
        """
        self._parent_id = parent_id

    @property
    def picture_category_name(self):
        return self._picture_category_name

    @picture_category_name.setter
    def picture_category_name(self, picture_category_name):
        if isinstance(picture_category_name, str):
            self._picture_category_name = picture_category_name
        else:
            raise TypeError("picture_category_name must be str")

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
        return "taobao.picture.category.add"

    def to_dict(self):
        request_dict = {}
        if self._picture_category_name is not None:
            request_dict["picture_category_name"] = convert_basic(self._picture_category_name)

        if self._parent_id is not None:
            request_dict["parent_id"] = convert_basic(self._parent_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


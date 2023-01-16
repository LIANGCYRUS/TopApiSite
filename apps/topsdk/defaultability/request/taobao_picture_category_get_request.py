from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureCategoryGetRequest(BaseRequest):

    def __init__(
        self,
        picture_category_id: int = None,
        picture_category_name: str = None,
        type: str = None,
        parent_id: int = None,
        modified_time: datetime = None
    ):
        """
            图片分类ID
        """
        self._picture_category_id = picture_category_id
        """
            图片分类名，不支持模糊查询
        """
        self._picture_category_name = picture_category_name
        """
            1
        """
        self._type = type
        """
            取二级分类时设置为对应父分类id
取一级分类时父分类id设为0
取全部分类的时候不设或设为-1
        """
        self._parent_id = parent_id
        """
            图片分类的修改时间点，格式:yyyy-MM-dd HH:mm:ss。查询此修改时间点之后到目前的图片分类。
        """
        self._modified_time = modified_time

    @property
    def picture_category_id(self):
        return self._picture_category_id

    @picture_category_id.setter
    def picture_category_id(self, picture_category_id):
        if isinstance(picture_category_id, int):
            self._picture_category_id = picture_category_id
        else:
            raise TypeError("picture_category_id must be int")

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
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        if isinstance(parent_id, int):
            self._parent_id = parent_id
        else:
            raise TypeError("parent_id must be int")

    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        if isinstance(modified_time, datetime):
            self._modified_time = modified_time
        else:
            raise TypeError("modified_time must be datetime")


    def get_api_name(self):
        return "taobao.picture.category.get"

    def to_dict(self):
        request_dict = {}
        if self._picture_category_id is not None:
            request_dict["picture_category_id"] = convert_basic(self._picture_category_id)

        if self._picture_category_name is not None:
            request_dict["picture_category_name"] = convert_basic(self._picture_category_name)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._parent_id is not None:
            request_dict["parent_id"] = convert_basic(self._parent_id)

        if self._modified_time is not None:
            request_dict["modified_time"] = convert_basic(self._modified_time)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


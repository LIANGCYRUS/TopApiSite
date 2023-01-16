from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureUpdateRequest(BaseRequest):

    def __init__(
        self,
        picture_id: int = None,
        new_name: str = None
    ):
        """
            要更改名字的图片的id
        """
        self._picture_id = picture_id
        """
            新的图片名，最大长度50字符，不能为空
        """
        self._new_name = new_name

    @property
    def picture_id(self):
        return self._picture_id

    @picture_id.setter
    def picture_id(self, picture_id):
        if isinstance(picture_id, int):
            self._picture_id = picture_id
        else:
            raise TypeError("picture_id must be int")

    @property
    def new_name(self):
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        if isinstance(new_name, str):
            self._new_name = new_name
        else:
            raise TypeError("new_name must be str")


    def get_api_name(self):
        return "taobao.picture.update"

    def to_dict(self):
        request_dict = {}
        if self._picture_id is not None:
            request_dict["picture_id"] = convert_basic(self._picture_id)

        if self._new_name is not None:
            request_dict["new_name"] = convert_basic(self._new_name)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


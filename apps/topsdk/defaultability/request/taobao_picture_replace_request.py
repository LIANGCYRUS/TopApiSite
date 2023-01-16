from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureReplaceRequest(BaseRequest):

    def __init__(
        self,
        picture_id: int = None,
        image_data: bytes = None
    ):
        """
            要替换的图片的id，必须大于0
        """
        self._picture_id = picture_id
        """
            图片二进制文件流,不能为空,允许png、jpg、gif图片格式
        """
        self._image_data = image_data

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
    def image_data(self):
        return self._image_data

    @image_data.setter
    def image_data(self, image_data):
        if isinstance(image_data, bytes):
            self._image_data = image_data
        else:
            raise TypeError("image_data must be bytes")


    def get_api_name(self):
        return "taobao.picture.replace"

    def to_dict(self):
        request_dict = {}
        if self._picture_id is not None:
            request_dict["picture_id"] = convert_basic(self._picture_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image_data is not None:
            file_param_dict["image_data"] = convert_basic(self._image_data)
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureIsreferencedGetRequest(BaseRequest):

    def __init__(
        self,
        picture_id: int = None
    ):
        """
            图片id
        """
        self._picture_id = picture_id

    @property
    def picture_id(self):
        return self._picture_id

    @picture_id.setter
    def picture_id(self, picture_id):
        if isinstance(picture_id, int):
            self._picture_id = picture_id
        else:
            raise TypeError("picture_id must be int")


    def get_api_name(self):
        return "taobao.picture.isreferenced.get"

    def to_dict(self):
        request_dict = {}
        if self._picture_id is not None:
            request_dict["picture_id"] = convert_basic(self._picture_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class CainiaoCloudprintCustomareaUpdateRequest(BaseRequest):

    def __init__(
        self,
        custom_area_id: int = None,
        custom_area_name: str = None,
        custom_area_content: str = None
    ):
        """
            自定义区id（不可修改）
        """
        self._custom_area_id = custom_area_id
        """
            自定义区名称（可修改）
        """
        self._custom_area_name = custom_area_name
        """
            自定义区内容（可修改）
        """
        self._custom_area_content = custom_area_content

    @property
    def custom_area_id(self):
        return self._custom_area_id

    @custom_area_id.setter
    def custom_area_id(self, custom_area_id):
        if isinstance(custom_area_id, int):
            self._custom_area_id = custom_area_id
        else:
            raise TypeError("custom_area_id must be int")

    @property
    def custom_area_name(self):
        return self._custom_area_name

    @custom_area_name.setter
    def custom_area_name(self, custom_area_name):
        if isinstance(custom_area_name, str):
            self._custom_area_name = custom_area_name
        else:
            raise TypeError("custom_area_name must be str")

    @property
    def custom_area_content(self):
        return self._custom_area_content

    @custom_area_content.setter
    def custom_area_content(self, custom_area_content):
        if isinstance(custom_area_content, str):
            self._custom_area_content = custom_area_content
        else:
            raise TypeError("custom_area_content must be str")


    def get_api_name(self):
        return "cainiao.cloudprint.customarea.update"

    def to_dict(self):
        request_dict = {}
        if self._custom_area_id is not None:
            request_dict["custom_area_id"] = convert_basic(self._custom_area_id)

        if self._custom_area_name is not None:
            request_dict["custom_area_name"] = convert_basic(self._custom_area_name)

        if self._custom_area_content is not None:
            request_dict["custom_area_content"] = convert_basic(self._custom_area_content)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


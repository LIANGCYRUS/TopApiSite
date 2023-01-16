from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemSizemappingTemplateDeleteRequest(BaseRequest):

    def __init__(
        self,
        template_id: int = None
    ):
        """
            尺码表模板ID
        """
        self._template_id = template_id

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        if isinstance(template_id, int):
            self._template_id = template_id
        else:
            raise TypeError("template_id must be int")


    def get_api_name(self):
        return "tmall.item.sizemapping.template.delete"

    def to_dict(self):
        request_dict = {}
        if self._template_id is not None:
            request_dict["template_id"] = convert_basic(self._template_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


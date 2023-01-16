from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemSizemappingTemplateCreateRequest(BaseRequest):

    def __init__(
        self,
        template_name: str = None,
        template_content: str = None
    ):
        """
            尺码表模板名称
        """
        self._template_name = template_name
        """
            尺码表模板内容，格式为"尺码值:维度名称:数值,尺码值:维度名称:数值"。其中，数值的单位，长度单位为厘米（cm），体重单位为公斤（kg）。尺码值，维度数据不能包含数字，特殊字符。数值为0-999.9的数字，且最多一位小数。
        """
        self._template_content = template_content

    @property
    def template_name(self):
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        if isinstance(template_name, str):
            self._template_name = template_name
        else:
            raise TypeError("template_name must be str")

    @property
    def template_content(self):
        return self._template_content

    @template_content.setter
    def template_content(self, template_content):
        if isinstance(template_content, str):
            self._template_content = template_content
        else:
            raise TypeError("template_content must be str")


    def get_api_name(self):
        return "tmall.item.sizemapping.template.create"

    def to_dict(self):
        request_dict = {}
        if self._template_name is not None:
            request_dict["template_name"] = convert_basic(self._template_name)

        if self._template_content is not None:
            request_dict["template_content"] = convert_basic(self._template_content)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


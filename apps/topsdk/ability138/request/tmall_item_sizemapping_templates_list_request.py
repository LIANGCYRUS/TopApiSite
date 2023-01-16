from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemSizemappingTemplatesListRequest(BaseRequest):

    def __init__(
        self
    ):


    def get_api_name(self):
        return "tmall.item.sizemapping.templates.list"

    def to_dict(self):
        request_dict = {}
        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemHscodeDetailGetRequest(BaseRequest):

    def __init__(
        self,
        hscode: str = None
    ):
        """
            hscode
        """
        self._hscode = hscode

    @property
    def hscode(self):
        return self._hscode

    @hscode.setter
    def hscode(self, hscode):
        if isinstance(hscode, str):
            self._hscode = hscode
        else:
            raise TypeError("hscode must be str")


    def get_api_name(self):
        return "tmall.item.hscode.detail.get"

    def to_dict(self):
        request_dict = {}
        if self._hscode is not None:
            request_dict["hscode"] = convert_basic(self._hscode)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSubusersInfoQueryRequest(BaseRequest):

    def __init__(
        self,
        site: int = None
    ):
        """
            站点信息，淘宝天猫传0，1688传3
        """
        self._site = site

    @property
    def site(self):
        return self._site

    @site.setter
    def site(self, site):
        if isinstance(site, int):
            self._site = site
        else:
            raise TypeError("site must be int")


    def get_api_name(self):
        return "taobao.subusers.info.query"

    def to_dict(self):
        request_dict = {}
        if self._site is not None:
            request_dict["site"] = convert_basic(self._site)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


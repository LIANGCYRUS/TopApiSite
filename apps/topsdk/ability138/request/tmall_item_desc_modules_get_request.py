from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemDescModulesGetRequest(BaseRequest):

    def __init__(
        self,
        cat_id: int = None,
        usr_id: str = None
    ):
        """
            淘宝后台发布商品的叶子类目id，可通过taobao.itemcats.get查到。api 访问地址http://api.taobao.com/apidoc/api.htm?spm=0.0.0.0.CFhhk4&path=cid:3-apiId:122
        """
        self._cat_id = cat_id
        """
            商家主帐号id
        """
        self._usr_id = usr_id

    @property
    def cat_id(self):
        return self._cat_id

    @cat_id.setter
    def cat_id(self, cat_id):
        if isinstance(cat_id, int):
            self._cat_id = cat_id
        else:
            raise TypeError("cat_id must be int")

    @property
    def usr_id(self):
        return self._usr_id

    @usr_id.setter
    def usr_id(self, usr_id):
        if isinstance(usr_id, str):
            self._usr_id = usr_id
        else:
            raise TypeError("usr_id must be str")


    def get_api_name(self):
        return "tmall.item.desc.modules.get"

    def to_dict(self):
        request_dict = {}
        if self._cat_id is not None:
            request_dict["cat_id"] = convert_basic(self._cat_id)

        if self._usr_id is not None:
            request_dict["usr_id"] = convert_basic(self._usr_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


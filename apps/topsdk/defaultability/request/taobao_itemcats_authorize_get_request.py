from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemcatsAuthorizeGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None
    ):
        """
            需要返回的字段。目前支持有：brand.vid, brand.name, item_cat.cid, item_cat.name, item_cat.status,item_cat.sort_order,item_cat.parent_cid,item_cat.is_parent,xinpin_item_cat.cid, xinpin_item_cat.name, xinpin_item_cat.status,xinpin_item_cat.sort_order,xinpin_item_cat.parent_cid,xinpin_item_cat.is_parent
        """
        self._fields = fields

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")


    def get_api_name(self):
        return "taobao.itemcats.authorize.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


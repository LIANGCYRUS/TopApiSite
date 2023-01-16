from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsItemCombinationGetRequest(BaseRequest):

    def __init__(
        self,
        itemid: int = None
    ):
        """
            货品Id
        """
        self._itemid = itemid

    @property
    def itemid(self):
        return self._itemid

    @itemid.setter
    def itemid(self, itemid):
        if isinstance(itemid, int):
            self._itemid = itemid
        else:
            raise TypeError("itemid must be int")


    def get_api_name(self):
        return "taobao.wlb.wms.item.combination.get"

    def to_dict(self):
        request_dict = {}
        if self._itemid is not None:
            request_dict["itemid"] = convert_basic(self._itemid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


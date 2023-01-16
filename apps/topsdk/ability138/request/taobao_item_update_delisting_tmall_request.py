from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemUpdateDelistingTmallRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None
    ):
        """
            商品数字ID，该参数必须
        """
        self._num_iid = num_iid

    @property
    def num_iid(self):
        return self._num_iid

    @num_iid.setter
    def num_iid(self, num_iid):
        if isinstance(num_iid, int):
            self._num_iid = num_iid
        else:
            raise TypeError("num_iid must be int")


    def get_api_name(self):
        return "taobao.item.update.delisting.tmall"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


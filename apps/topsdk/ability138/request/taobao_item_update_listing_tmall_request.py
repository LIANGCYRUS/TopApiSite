from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemUpdateListingTmallRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        num: int = None
    ):
        """
            商品数字ID，该参数必须
        """
        self._num_iid = num_iid
        """
            需要上架的商品的数量。取值范围:大于零的整数。如果商品有sku，则上架数量默认为所有sku数量总和，不可修改。否则商品数量根据设置数量调整为num
        """
        self._num = num

    @property
    def num_iid(self):
        return self._num_iid

    @num_iid.setter
    def num_iid(self, num_iid):
        if isinstance(num_iid, int):
            self._num_iid = num_iid
        else:
            raise TypeError("num_iid must be int")

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        if isinstance(num, int):
            self._num = num
        else:
            raise TypeError("num must be int")


    def get_api_name(self):
        return "taobao.item.update.listing.tmall"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._num is not None:
            request_dict["num"] = convert_basic(self._num)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


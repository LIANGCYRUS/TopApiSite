from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsAddressSearchRequest(BaseRequest):

    def __init__(
        self,
        rdef: str = None
    ):
        """
            可选，参数列表如下：<br><font color='red'>no_def:查询非默认地址<br>get_def:查询默认取货地址，也即对应卖家后台地址库中发货地址（send_def暂不起作用）<br>cancel_def:查询默认退货地址<br>缺省此参数时，查询所有当前用户的地址库</font>
        """
        self._rdef = rdef

    @property
    def rdef(self):
        return self._rdef

    @rdef.setter
    def rdef(self, rdef):
        if isinstance(rdef, str):
            self._rdef = rdef
        else:
            raise TypeError("rdef must be str")


    def get_api_name(self):
        return "taobao.logistics.address.search"

    def to_dict(self):
        request_dict = {}
        if self._rdef is not None:
            request_dict["rdef"] = convert_basic(self._rdef)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


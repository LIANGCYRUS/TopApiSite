from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportsResourceGetRequest(BaseRequest):

    def __init__(
        self,
        from_id: int = None,
        to_address: object = None
    ):
        """
            卖家发货地区域ID
        """
        self._from_id = from_id
        """
            买家收货地信息
        """
        self._to_address = to_address

    @property
    def from_id(self):
        return self._from_id

    @from_id.setter
    def from_id(self, from_id):
        if isinstance(from_id, int):
            self._from_id = from_id
        else:
            raise TypeError("from_id must be int")

    @property
    def to_address(self):
        return self._to_address

    @to_address.setter
    def to_address(self, to_address):
        if isinstance(to_address, object):
            self._to_address = to_address
        else:
            raise TypeError("to_address must be object")


    def get_api_name(self):
        return "taobao.wlb.imports.resource.get"

    def to_dict(self):
        request_dict = {}
        if self._from_id is not None:
            request_dict["from_id"] = convert_basic(self._from_id)

        if self._to_address is not None:
            request_dict["to_address"] = convert_struct(self._to_address)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoWlbImportsResourceGetReciverAddressDo:
    def __init__(
        self,
        detail_address: str = None,
        street: str = None,
        district: str = None,
        city: str = None,
        province: str = None,
        country: str = None
    ):
        """
            详细地址，只需填写买家具体的收货地址
        """
        self.detail_address = detail_address
        """
            街道信息
        """
        self.street = street
        """
            区县地址信息，city和district不能同时为空
        """
        self.district = district
        """
            市地址信息，city和district不能同时为空
        """
        self.city = city
        """
            省地址信息
        """
        self.province = province
        """
            国家地址信息
        """
        self.country = country


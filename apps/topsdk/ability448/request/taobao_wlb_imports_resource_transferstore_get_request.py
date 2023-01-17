from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportsResourceTransferstoreGetRequest(BaseRequest):

    def __init__(
        self,
        resource_id: int = None,
        from_id: int = None,
        to_address: object = None,
        cids: list = None
    ):
        """
            通过taobao.wlb.imports.resource.get接口查询出来的资源ID
        """
        self._resource_id = resource_id
        """
            卖家发货地址的区域ID，如果不填则为默认发货地址ID
        """
        self._from_id = from_id
        """
            买家收货地信息
        """
        self._to_address = to_address
        """
            商品前台叶子类目ID
        """
        self._cids = cids

    @property
    def resource_id(self):
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        if isinstance(resource_id, int):
            self._resource_id = resource_id
        else:
            raise TypeError("resource_id must be int")

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

    @property
    def cids(self):
        return self._cids

    @cids.setter
    def cids(self, cids):
        if isinstance(cids, list):
            self._cids = cids
        else:
            raise TypeError("cids must be list")


    def get_api_name(self):
        return "taobao.wlb.imports.resource.transferstore.get"

    def to_dict(self):
        request_dict = {}
        if self._resource_id is not None:
            request_dict["resource_id"] = convert_basic(self._resource_id)

        if self._from_id is not None:
            request_dict["from_id"] = convert_basic(self._from_id)

        if self._to_address is not None:
            request_dict["to_address"] = convert_struct(self._to_address)

        if self._cids is not None:
            request_dict["cids"] = convert_basic_list(self._cids)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoWlbImportsResourceTransferstoreGetReciverAddressDo:
    def __init__(
        self,
        street: str = None,
        district: str = None,
        city: str = None,
        province: str = None,
        country: str = None,
        detail_address: str = None
    ):
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
        """
            详细地址，只需填写买家具体的收货地址
        """
        self.detail_address = detail_address


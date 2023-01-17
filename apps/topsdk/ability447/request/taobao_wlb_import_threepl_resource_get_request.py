from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportThreeplResourceGetRequest(BaseRequest):

    def __init__(
        self,
        type: str = None,
        from_id: int = None,
        to_address: object = None
    ):
        """
            ONLINE或者OFFLINE
        """
        self._type = type
        """
            发货地区域id
        """
        self._from_id = from_id
        """
            收件人地址
        """
        self._to_address = to_address

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")

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
        return "taobao.wlb.import.threepl.resource.get"

    def to_dict(self):
        request_dict = {}
        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._from_id is not None:
            request_dict["from_id"] = convert_basic(self._from_id)

        if self._to_address is not None:
            request_dict["to_address"] = convert_struct(self._to_address)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoWlbImportThreeplResourceGetAddressDto:
    def __init__(
        self,
        county: str = None,
        province: str = None,
        town: str = None,
        detail_address: str = None,
        city: str = None,
        country: str = None
    ):
        """
            区级地址
        """
        self.county = county
        """
            省级地址
        """
        self.province = province
        """
            街道地址
        """
        self.town = town
        """
            详细地址
        """
        self.detail_address = detail_address
        """
            市级地址
        """
        self.city = city
        """
            国家地址
        """
        self.country = country


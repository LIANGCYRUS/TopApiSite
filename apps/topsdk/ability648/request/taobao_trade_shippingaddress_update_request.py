from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradeShippingaddressUpdateRequest(BaseRequest):

    def __init__(
        self,
        tid: int = None,
        receiver_name: str = None,
        receiver_phone: str = None,
        receiver_mobile: str = None,
        receiver_state: str = None,
        receiver_city: str = None,
        receiver_district: str = None,
        receiver_address: str = None,
        receiver_zip: str = None,
        receiver_town: str = None
    ):
        """
            交易编号。
        """
        self._tid = tid
        """
            收货人全名。最大长度为50个字节。
        """
        self._receiver_name = receiver_name
        """
            座机号码。最大长度为30个字节。传-1表示删除
        """
        self._receiver_phone = receiver_phone
        """
            移动电话。最大长度为11个字节。传-1表示删除
        """
        self._receiver_mobile = receiver_mobile
        """
            省份。最大长度为32个字节。如：浙江
        """
        self._receiver_state = receiver_state
        """
            城市。最大长度为32个字节。如：杭州
        """
        self._receiver_city = receiver_city
        """
            区/县。最大长度为32个字节。如：西湖区
        """
        self._receiver_district = receiver_district
        """
            收货地址。最大长度为228个字节。
        """
        self._receiver_address = receiver_address
        """
            邮政编码。必须由6个数字组成。注：邮政编码根据地址信息自动填入，不可单独修改
        """
        self._receiver_zip = receiver_zip
        """
            四级地址。最大长度为32个字节。如：五常街道
        """
        self._receiver_town = receiver_town

    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, int):
            self._tid = tid
        else:
            raise TypeError("tid must be int")

    @property
    def receiver_name(self):
        return self._receiver_name

    @receiver_name.setter
    def receiver_name(self, receiver_name):
        if isinstance(receiver_name, str):
            self._receiver_name = receiver_name
        else:
            raise TypeError("receiver_name must be str")

    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, receiver_phone):
        if isinstance(receiver_phone, str):
            self._receiver_phone = receiver_phone
        else:
            raise TypeError("receiver_phone must be str")

    @property
    def receiver_mobile(self):
        return self._receiver_mobile

    @receiver_mobile.setter
    def receiver_mobile(self, receiver_mobile):
        if isinstance(receiver_mobile, str):
            self._receiver_mobile = receiver_mobile
        else:
            raise TypeError("receiver_mobile must be str")

    @property
    def receiver_state(self):
        return self._receiver_state

    @receiver_state.setter
    def receiver_state(self, receiver_state):
        if isinstance(receiver_state, str):
            self._receiver_state = receiver_state
        else:
            raise TypeError("receiver_state must be str")

    @property
    def receiver_city(self):
        return self._receiver_city

    @receiver_city.setter
    def receiver_city(self, receiver_city):
        if isinstance(receiver_city, str):
            self._receiver_city = receiver_city
        else:
            raise TypeError("receiver_city must be str")

    @property
    def receiver_district(self):
        return self._receiver_district

    @receiver_district.setter
    def receiver_district(self, receiver_district):
        if isinstance(receiver_district, str):
            self._receiver_district = receiver_district
        else:
            raise TypeError("receiver_district must be str")

    @property
    def receiver_address(self):
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address):
        if isinstance(receiver_address, str):
            self._receiver_address = receiver_address
        else:
            raise TypeError("receiver_address must be str")

    @property
    def receiver_zip(self):
        return self._receiver_zip

    @receiver_zip.setter
    def receiver_zip(self, receiver_zip):
        if isinstance(receiver_zip, str):
            self._receiver_zip = receiver_zip
        else:
            raise TypeError("receiver_zip must be str")

    @property
    def receiver_town(self):
        return self._receiver_town

    @receiver_town.setter
    def receiver_town(self, receiver_town):
        if isinstance(receiver_town, str):
            self._receiver_town = receiver_town
        else:
            raise TypeError("receiver_town must be str")


    def get_api_name(self):
        return "taobao.trade.shippingaddress.update"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._receiver_name is not None:
            request_dict["receiver_name"] = convert_basic(self._receiver_name)

        if self._receiver_phone is not None:
            request_dict["receiver_phone"] = convert_basic(self._receiver_phone)

        if self._receiver_mobile is not None:
            request_dict["receiver_mobile"] = convert_basic(self._receiver_mobile)

        if self._receiver_state is not None:
            request_dict["receiver_state"] = convert_basic(self._receiver_state)

        if self._receiver_city is not None:
            request_dict["receiver_city"] = convert_basic(self._receiver_city)

        if self._receiver_district is not None:
            request_dict["receiver_district"] = convert_basic(self._receiver_district)

        if self._receiver_address is not None:
            request_dict["receiver_address"] = convert_basic(self._receiver_address)

        if self._receiver_zip is not None:
            request_dict["receiver_zip"] = convert_basic(self._receiver_zip)

        if self._receiver_town is not None:
            request_dict["receiver_town"] = convert_basic(self._receiver_town)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


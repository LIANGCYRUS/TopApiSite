from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsAddressAddRequest(BaseRequest):

    def __init__(
        self,
        contact_name: str = None,
        province: str = None,
        city: str = None,
        country: str = None,
        addr: str = None,
        zip_code: str = None,
        phone: str = None,
        mobile_phone: str = None,
        seller_company: str = None,
        memo: str = None,
        send_def: bool = None,
        get_def: bool = None,
        cancel_def: bool = None
    ):
        """
            联系人姓名 <font color='red'>长度不可超过20个字节</font>
        """
        self._contact_name = contact_name
        """
            所在省
        """
        self._province = province
        """
            所在市
        """
        self._city = city
        """
            区、县
<br><font color='red'>如果所在地区是海外的可以为空，否则为必参</font>
        """
        self._country = country
        """
            详细街道地址，不需要重复填写省/市/区
        """
        self._addr = addr
        """
            地区邮政编码
<br><font color='red'>如果所在地区是海外的可以为空，否则为必参</font>
        """
        self._zip_code = zip_code
        """
            电话号码,手机与电话必需有一个
        """
        self._phone = phone
        """
            手机号码，手机与电话必需有一个
<br><font color='red'>手机号码不能超过20位</font>
        """
        self._mobile_phone = mobile_phone
        """
            公司名称,<br><font color="red">公司名称长能不能超过20字节</font>
        """
        self._seller_company = seller_company
        """
            备注,<br><font color='red'>备注不能超过256字节</font>
        """
        self._memo = memo
        """
            默认发货地址。<br>
<font color='red'>选择此项(true)，将当前地址设为默认发货地址，撤消原默认发货地址</font>
        """
        self._send_def = send_def
        """
            默认取货地址。<br>
<font color='red'>选择此项(true)，将当前地址设为默认取货地址，撤消原默认取货地址</font>
        """
        self._get_def = get_def
        """
            默认退货地址。<br>
<font color='red'>选择此项(true)，将当前地址设为默认退货地址，撤消原默认退货地址</font>
        """
        self._cancel_def = cancel_def

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        if isinstance(contact_name, str):
            self._contact_name = contact_name
        else:
            raise TypeError("contact_name must be str")

    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, province):
        if isinstance(province, str):
            self._province = province
        else:
            raise TypeError("province must be str")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if isinstance(city, str):
            self._city = city
        else:
            raise TypeError("city must be str")

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country):
        if isinstance(country, str):
            self._country = country
        else:
            raise TypeError("country must be str")

    @property
    def addr(self):
        return self._addr

    @addr.setter
    def addr(self, addr):
        if isinstance(addr, str):
            self._addr = addr
        else:
            raise TypeError("addr must be str")

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        if isinstance(zip_code, str):
            self._zip_code = zip_code
        else:
            raise TypeError("zip_code must be str")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if isinstance(phone, str):
            self._phone = phone
        else:
            raise TypeError("phone must be str")

    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        if isinstance(mobile_phone, str):
            self._mobile_phone = mobile_phone
        else:
            raise TypeError("mobile_phone must be str")

    @property
    def seller_company(self):
        return self._seller_company

    @seller_company.setter
    def seller_company(self, seller_company):
        if isinstance(seller_company, str):
            self._seller_company = seller_company
        else:
            raise TypeError("seller_company must be str")

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, memo):
        if isinstance(memo, str):
            self._memo = memo
        else:
            raise TypeError("memo must be str")

    @property
    def send_def(self):
        return self._send_def

    @send_def.setter
    def send_def(self, send_def):
        if isinstance(send_def, bool):
            self._send_def = send_def
        else:
            raise TypeError("send_def must be bool")

    @property
    def get_def(self):
        return self._get_def

    @get_def.setter
    def get_def(self, get_def):
        if isinstance(get_def, bool):
            self._get_def = get_def
        else:
            raise TypeError("get_def must be bool")

    @property
    def cancel_def(self):
        return self._cancel_def

    @cancel_def.setter
    def cancel_def(self, cancel_def):
        if isinstance(cancel_def, bool):
            self._cancel_def = cancel_def
        else:
            raise TypeError("cancel_def must be bool")


    def get_api_name(self):
        return "taobao.logistics.address.add"

    def to_dict(self):
        request_dict = {}
        if self._contact_name is not None:
            request_dict["contact_name"] = convert_basic(self._contact_name)

        if self._province is not None:
            request_dict["province"] = convert_basic(self._province)

        if self._city is not None:
            request_dict["city"] = convert_basic(self._city)

        if self._country is not None:
            request_dict["country"] = convert_basic(self._country)

        if self._addr is not None:
            request_dict["addr"] = convert_basic(self._addr)

        if self._zip_code is not None:
            request_dict["zip_code"] = convert_basic(self._zip_code)

        if self._phone is not None:
            request_dict["phone"] = convert_basic(self._phone)

        if self._mobile_phone is not None:
            request_dict["mobile_phone"] = convert_basic(self._mobile_phone)

        if self._seller_company is not None:
            request_dict["seller_company"] = convert_basic(self._seller_company)

        if self._memo is not None:
            request_dict["memo"] = convert_basic(self._memo)

        if self._send_def is not None:
            request_dict["send_def"] = convert_basic(self._send_def)

        if self._get_def is not None:
            request_dict["get_def"] = convert_basic(self._get_def)

        if self._cancel_def is not None:
            request_dict["cancel_def"] = convert_basic(self._cancel_def)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


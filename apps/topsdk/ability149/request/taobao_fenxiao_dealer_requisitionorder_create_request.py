from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDealerRequisitionorderCreateRequest(BaseRequest):

    def __init__(
        self,
        order_detail: list = None,
        logistics_type: str = None,
        province: str = None,
        city: str = None,
        district: str = None,
        address: str = None,
        post_code: str = None,
        phone: str = None,
        mobile: str = None,
        buyer_name: str = None,
        id_card_number: str = None
    ):
        """
            采购清单，存放多个采购明细，每个采购明细内部以‘:’隔开，多个采购明细之间以‘,’隔开. 例(分销产品id:skuid:购买数量:申请单价,分销产品id:skuid:购买数量:申请单价)，申请单价的单位为分。不存在sku请留空skuid，如（分销产品id::购买数量:申请单价）
        """
        self._order_detail = order_detail
        """
            配送方式。SELF_PICKUP：自提；LOGISTICS：仓库发货
        """
        self._logistics_type = logistics_type
        """
            收货人所在省份
        """
        self._province = province
        """
            收货人所在市
        """
        self._city = city
        """
            收货人所在区
        """
        self._district = district
        """
            收货人所在街道地址
        """
        self._address = address
        """
            收货人所在地区邮政编码
        """
        self._post_code = post_code
        """
            买家联系电话（此字段和mobile字段至少填写一个）
        """
        self._phone = phone
        """
            买家的手机号码（1、此字段与phone字段至少填写一个。2、自提方式下此字段必填，保存提货人联系电话）
        """
        self._mobile = mobile
        """
            买家姓名（自提方式填写提货人姓名）
        """
        self._buyer_name = buyer_name
        """
            身份证号（自提方式必填，填写提货人身份证号码，提货时用于确认提货人身份）
        """
        self._id_card_number = id_card_number

    @property
    def order_detail(self):
        return self._order_detail

    @order_detail.setter
    def order_detail(self, order_detail):
        if isinstance(order_detail, list):
            self._order_detail = order_detail
        else:
            raise TypeError("order_detail must be list")

    @property
    def logistics_type(self):
        return self._logistics_type

    @logistics_type.setter
    def logistics_type(self, logistics_type):
        if isinstance(logistics_type, str):
            self._logistics_type = logistics_type
        else:
            raise TypeError("logistics_type must be str")

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
    def district(self):
        return self._district

    @district.setter
    def district(self, district):
        if isinstance(district, str):
            self._district = district
        else:
            raise TypeError("district must be str")

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str):
            self._address = address
        else:
            raise TypeError("address must be str")

    @property
    def post_code(self):
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        if isinstance(post_code, str):
            self._post_code = post_code
        else:
            raise TypeError("post_code must be str")

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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        if isinstance(mobile, str):
            self._mobile = mobile
        else:
            raise TypeError("mobile must be str")

    @property
    def buyer_name(self):
        return self._buyer_name

    @buyer_name.setter
    def buyer_name(self, buyer_name):
        if isinstance(buyer_name, str):
            self._buyer_name = buyer_name
        else:
            raise TypeError("buyer_name must be str")

    @property
    def id_card_number(self):
        return self._id_card_number

    @id_card_number.setter
    def id_card_number(self, id_card_number):
        if isinstance(id_card_number, str):
            self._id_card_number = id_card_number
        else:
            raise TypeError("id_card_number must be str")


    def get_api_name(self):
        return "taobao.fenxiao.dealer.requisitionorder.create"

    def to_dict(self):
        request_dict = {}
        if self._order_detail is not None:
            request_dict["order_detail"] = convert_basic_list(self._order_detail)

        if self._logistics_type is not None:
            request_dict["logistics_type"] = convert_basic(self._logistics_type)

        if self._province is not None:
            request_dict["province"] = convert_basic(self._province)

        if self._city is not None:
            request_dict["city"] = convert_basic(self._city)

        if self._district is not None:
            request_dict["district"] = convert_basic(self._district)

        if self._address is not None:
            request_dict["address"] = convert_basic(self._address)

        if self._post_code is not None:
            request_dict["post_code"] = convert_basic(self._post_code)

        if self._phone is not None:
            request_dict["phone"] = convert_basic(self._phone)

        if self._mobile is not None:
            request_dict["mobile"] = convert_basic(self._mobile)

        if self._buyer_name is not None:
            request_dict["buyer_name"] = convert_basic(self._buyer_name)

        if self._id_card_number is not None:
            request_dict["id_card_number"] = convert_basic(self._id_card_number)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


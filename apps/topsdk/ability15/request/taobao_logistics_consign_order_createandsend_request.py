from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsConsignOrderCreateandsendRequest(BaseRequest):

    def __init__(
        self,
        company_id: int = None,
        trade_id: int = None,
        mail_no: str = None,
        order_source: int = None,
        user_id: int = None,
        logis_type: int = None,
        order_type: int = None,
        shipping: str = None,
        item_json_string: str = None,
        s_address: str = None,
        s_city_name: str = None,
        s_name: str = None,
        s_prov_name: str = None,
        s_dist_name: str = None,
        s_area_id: int = None,
        s_telephone: str = None,
        s_mobile_phone: str = None,
        s_zip_code: str = None,
        r_telephone: str = None,
        r_prov_name: str = None,
        r_address: str = None,
        r_city_name: str = None,
        r_mobile_phone: str = None,
        r_dist_name: str = None,
        r_zip_code: str = None,
        r_name: str = None,
        r_area_id: int = None
    ):
        """
            物流公司ID
        """
        self._company_id = company_id
        """
            交易流水号，淘外订单号或者商家内部交易流水号
        """
        self._trade_id = trade_id
        """
            运单号
        """
        self._mail_no = mail_no
        """
            订单来源，值选择：30
        """
        self._order_source = order_source
        """
            用户ID
        """
        self._user_id = user_id
        """
            物流订单物流类型，值固定选择：2
        """
        self._logis_type = logis_type
        """
            订单类型，值固定选择：30
        """
        self._order_type = order_type
        """
            费用承担方式 1买家承担运费 2卖家承担运费
        """
        self._shipping = shipping
        """
            物品的json数据。
        """
        self._item_json_string = item_json_string
        """
            发件人街道地址
        """
        self._s_address = s_address
        """
            市
        """
        self._s_city_name = s_city_name
        """
            发件人名称
        """
        self._s_name = s_name
        """
            省
        """
        self._s_prov_name = s_prov_name
        """
            区
        """
        self._s_dist_name = s_dist_name
        """
            发件人区域ID
        """
        self._s_area_id = s_area_id
        """
            电话号码
        """
        self._s_telephone = s_telephone
        """
            手机号码
        """
        self._s_mobile_phone = s_mobile_phone
        """
            发件人出编
        """
        self._s_zip_code = s_zip_code
        """
            电话号码
        """
        self._r_telephone = r_telephone
        """
            省
        """
        self._r_prov_name = r_prov_name
        """
            收件人街道地址
        """
        self._r_address = r_address
        """
            市
        """
        self._r_city_name = r_city_name
        """
            手机号码
        """
        self._r_mobile_phone = r_mobile_phone
        """
            区
        """
        self._r_dist_name = r_dist_name
        """
            收件人邮编
        """
        self._r_zip_code = r_zip_code
        """
            收件人名称
        """
        self._r_name = r_name
        """
            收件人区域ID
        """
        self._r_area_id = r_area_id

    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        if isinstance(company_id, int):
            self._company_id = company_id
        else:
            raise TypeError("company_id must be int")

    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        if isinstance(trade_id, int):
            self._trade_id = trade_id
        else:
            raise TypeError("trade_id must be int")

    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, mail_no):
        if isinstance(mail_no, str):
            self._mail_no = mail_no
        else:
            raise TypeError("mail_no must be str")

    @property
    def order_source(self):
        return self._order_source

    @order_source.setter
    def order_source(self, order_source):
        if isinstance(order_source, int):
            self._order_source = order_source
        else:
            raise TypeError("order_source must be int")

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int):
            self._user_id = user_id
        else:
            raise TypeError("user_id must be int")

    @property
    def logis_type(self):
        return self._logis_type

    @logis_type.setter
    def logis_type(self, logis_type):
        if isinstance(logis_type, int):
            self._logis_type = logis_type
        else:
            raise TypeError("logis_type must be int")

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, int):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be int")

    @property
    def shipping(self):
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        if isinstance(shipping, str):
            self._shipping = shipping
        else:
            raise TypeError("shipping must be str")

    @property
    def item_json_string(self):
        return self._item_json_string

    @item_json_string.setter
    def item_json_string(self, item_json_string):
        if isinstance(item_json_string, str):
            self._item_json_string = item_json_string
        else:
            raise TypeError("item_json_string must be str")

    @property
    def s_address(self):
        return self._s_address

    @s_address.setter
    def s_address(self, s_address):
        if isinstance(s_address, str):
            self._s_address = s_address
        else:
            raise TypeError("s_address must be str")

    @property
    def s_city_name(self):
        return self._s_city_name

    @s_city_name.setter
    def s_city_name(self, s_city_name):
        if isinstance(s_city_name, str):
            self._s_city_name = s_city_name
        else:
            raise TypeError("s_city_name must be str")

    @property
    def s_name(self):
        return self._s_name

    @s_name.setter
    def s_name(self, s_name):
        if isinstance(s_name, str):
            self._s_name = s_name
        else:
            raise TypeError("s_name must be str")

    @property
    def s_prov_name(self):
        return self._s_prov_name

    @s_prov_name.setter
    def s_prov_name(self, s_prov_name):
        if isinstance(s_prov_name, str):
            self._s_prov_name = s_prov_name
        else:
            raise TypeError("s_prov_name must be str")

    @property
    def s_dist_name(self):
        return self._s_dist_name

    @s_dist_name.setter
    def s_dist_name(self, s_dist_name):
        if isinstance(s_dist_name, str):
            self._s_dist_name = s_dist_name
        else:
            raise TypeError("s_dist_name must be str")

    @property
    def s_area_id(self):
        return self._s_area_id

    @s_area_id.setter
    def s_area_id(self, s_area_id):
        if isinstance(s_area_id, int):
            self._s_area_id = s_area_id
        else:
            raise TypeError("s_area_id must be int")

    @property
    def s_telephone(self):
        return self._s_telephone

    @s_telephone.setter
    def s_telephone(self, s_telephone):
        if isinstance(s_telephone, str):
            self._s_telephone = s_telephone
        else:
            raise TypeError("s_telephone must be str")

    @property
    def s_mobile_phone(self):
        return self._s_mobile_phone

    @s_mobile_phone.setter
    def s_mobile_phone(self, s_mobile_phone):
        if isinstance(s_mobile_phone, str):
            self._s_mobile_phone = s_mobile_phone
        else:
            raise TypeError("s_mobile_phone must be str")

    @property
    def s_zip_code(self):
        return self._s_zip_code

    @s_zip_code.setter
    def s_zip_code(self, s_zip_code):
        if isinstance(s_zip_code, str):
            self._s_zip_code = s_zip_code
        else:
            raise TypeError("s_zip_code must be str")

    @property
    def r_telephone(self):
        return self._r_telephone

    @r_telephone.setter
    def r_telephone(self, r_telephone):
        if isinstance(r_telephone, str):
            self._r_telephone = r_telephone
        else:
            raise TypeError("r_telephone must be str")

    @property
    def r_prov_name(self):
        return self._r_prov_name

    @r_prov_name.setter
    def r_prov_name(self, r_prov_name):
        if isinstance(r_prov_name, str):
            self._r_prov_name = r_prov_name
        else:
            raise TypeError("r_prov_name must be str")

    @property
    def r_address(self):
        return self._r_address

    @r_address.setter
    def r_address(self, r_address):
        if isinstance(r_address, str):
            self._r_address = r_address
        else:
            raise TypeError("r_address must be str")

    @property
    def r_city_name(self):
        return self._r_city_name

    @r_city_name.setter
    def r_city_name(self, r_city_name):
        if isinstance(r_city_name, str):
            self._r_city_name = r_city_name
        else:
            raise TypeError("r_city_name must be str")

    @property
    def r_mobile_phone(self):
        return self._r_mobile_phone

    @r_mobile_phone.setter
    def r_mobile_phone(self, r_mobile_phone):
        if isinstance(r_mobile_phone, str):
            self._r_mobile_phone = r_mobile_phone
        else:
            raise TypeError("r_mobile_phone must be str")

    @property
    def r_dist_name(self):
        return self._r_dist_name

    @r_dist_name.setter
    def r_dist_name(self, r_dist_name):
        if isinstance(r_dist_name, str):
            self._r_dist_name = r_dist_name
        else:
            raise TypeError("r_dist_name must be str")

    @property
    def r_zip_code(self):
        return self._r_zip_code

    @r_zip_code.setter
    def r_zip_code(self, r_zip_code):
        if isinstance(r_zip_code, str):
            self._r_zip_code = r_zip_code
        else:
            raise TypeError("r_zip_code must be str")

    @property
    def r_name(self):
        return self._r_name

    @r_name.setter
    def r_name(self, r_name):
        if isinstance(r_name, str):
            self._r_name = r_name
        else:
            raise TypeError("r_name must be str")

    @property
    def r_area_id(self):
        return self._r_area_id

    @r_area_id.setter
    def r_area_id(self, r_area_id):
        if isinstance(r_area_id, int):
            self._r_area_id = r_area_id
        else:
            raise TypeError("r_area_id must be int")


    def get_api_name(self):
        return "taobao.logistics.consign.order.createandsend"

    def to_dict(self):
        request_dict = {}
        if self._company_id is not None:
            request_dict["company_id"] = convert_basic(self._company_id)

        if self._trade_id is not None:
            request_dict["trade_id"] = convert_basic(self._trade_id)

        if self._mail_no is not None:
            request_dict["mail_no"] = convert_basic(self._mail_no)

        if self._order_source is not None:
            request_dict["order_source"] = convert_basic(self._order_source)

        if self._user_id is not None:
            request_dict["user_id"] = convert_basic(self._user_id)

        if self._logis_type is not None:
            request_dict["logis_type"] = convert_basic(self._logis_type)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._shipping is not None:
            request_dict["shipping"] = convert_basic(self._shipping)

        if self._item_json_string is not None:
            request_dict["item_json_string"] = convert_basic(self._item_json_string)

        if self._s_address is not None:
            request_dict["s_address"] = convert_basic(self._s_address)

        if self._s_city_name is not None:
            request_dict["s_city_name"] = convert_basic(self._s_city_name)

        if self._s_name is not None:
            request_dict["s_name"] = convert_basic(self._s_name)

        if self._s_prov_name is not None:
            request_dict["s_prov_name"] = convert_basic(self._s_prov_name)

        if self._s_dist_name is not None:
            request_dict["s_dist_name"] = convert_basic(self._s_dist_name)

        if self._s_area_id is not None:
            request_dict["s_area_id"] = convert_basic(self._s_area_id)

        if self._s_telephone is not None:
            request_dict["s_telephone"] = convert_basic(self._s_telephone)

        if self._s_mobile_phone is not None:
            request_dict["s_mobile_phone"] = convert_basic(self._s_mobile_phone)

        if self._s_zip_code is not None:
            request_dict["s_zip_code"] = convert_basic(self._s_zip_code)

        if self._r_telephone is not None:
            request_dict["r_telephone"] = convert_basic(self._r_telephone)

        if self._r_prov_name is not None:
            request_dict["r_prov_name"] = convert_basic(self._r_prov_name)

        if self._r_address is not None:
            request_dict["r_address"] = convert_basic(self._r_address)

        if self._r_city_name is not None:
            request_dict["r_city_name"] = convert_basic(self._r_city_name)

        if self._r_mobile_phone is not None:
            request_dict["r_mobile_phone"] = convert_basic(self._r_mobile_phone)

        if self._r_dist_name is not None:
            request_dict["r_dist_name"] = convert_basic(self._r_dist_name)

        if self._r_zip_code is not None:
            request_dict["r_zip_code"] = convert_basic(self._r_zip_code)

        if self._r_name is not None:
            request_dict["r_name"] = convert_basic(self._r_name)

        if self._r_area_id is not None:
            request_dict["r_area_id"] = convert_basic(self._r_area_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


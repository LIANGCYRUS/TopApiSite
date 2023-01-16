from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRpReturngoodsAgreeRequest(BaseRequest):

    def __init__(
        self,
        refund_id: int = None,
        refund_phase: str = None,
        refund_version: int = None,
        remark: str = None,
        address: str = None,
        seller_address_id: int = None,
        mobile: str = None,
        post: str = None,
        name: str = None,
        tel: str = None,
        post_fee_bear_role: int = None,
        virtual_return_goods: bool = None
    ):
        """
            退款编号
        """
        self._refund_id = refund_id
        """
            售中：onsale，售后：aftersale，天猫退款为必填项。
        """
        self._refund_phase = refund_phase
        """
            退款版本号，天猫退款为必填项。
        """
        self._refund_version = refund_version
        """
            卖家退货留言，天猫退款为必填项。
        """
        self._remark = remark
        """
            卖家提供的退货地址，淘宝退款为必填项。
        """
        self._address = address
        """
            卖家收货地址编号，天猫淘宝退款都为必填项。
        """
        self._seller_address_id = seller_address_id
        """
            卖家手机，淘宝退款为必填项。
        """
        self._mobile = mobile
        """
            卖家提供的退货地址的邮编，淘宝退款为必填项。
        """
        self._post = post
        """
            卖家姓名，淘宝退款为必填项。
        """
        self._name = name
        """
            卖家座机，淘宝退款为必填项。
        """
        self._tel = tel
        """
            邮费承担方，买家承担值为1，卖家承担值为0
        """
        self._post_fee_bear_role = post_fee_bear_role
        """
            是否虚拟退货，可选项
        """
        self._virtual_return_goods = virtual_return_goods

    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        if isinstance(refund_id, int):
            self._refund_id = refund_id
        else:
            raise TypeError("refund_id must be int")

    @property
    def refund_phase(self):
        return self._refund_phase

    @refund_phase.setter
    def refund_phase(self, refund_phase):
        if isinstance(refund_phase, str):
            self._refund_phase = refund_phase
        else:
            raise TypeError("refund_phase must be str")

    @property
    def refund_version(self):
        return self._refund_version

    @refund_version.setter
    def refund_version(self, refund_version):
        if isinstance(refund_version, int):
            self._refund_version = refund_version
        else:
            raise TypeError("refund_version must be int")

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, remark):
        if isinstance(remark, str):
            self._remark = remark
        else:
            raise TypeError("remark must be str")

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
    def seller_address_id(self):
        return self._seller_address_id

    @seller_address_id.setter
    def seller_address_id(self, seller_address_id):
        if isinstance(seller_address_id, int):
            self._seller_address_id = seller_address_id
        else:
            raise TypeError("seller_address_id must be int")

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
    def post(self):
        return self._post

    @post.setter
    def post(self, post):
        if isinstance(post, str):
            self._post = post
        else:
            raise TypeError("post must be str")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, tel):
        if isinstance(tel, str):
            self._tel = tel
        else:
            raise TypeError("tel must be str")

    @property
    def post_fee_bear_role(self):
        return self._post_fee_bear_role

    @post_fee_bear_role.setter
    def post_fee_bear_role(self, post_fee_bear_role):
        if isinstance(post_fee_bear_role, int):
            self._post_fee_bear_role = post_fee_bear_role
        else:
            raise TypeError("post_fee_bear_role must be int")

    @property
    def virtual_return_goods(self):
        return self._virtual_return_goods

    @virtual_return_goods.setter
    def virtual_return_goods(self, virtual_return_goods):
        if isinstance(virtual_return_goods, bool):
            self._virtual_return_goods = virtual_return_goods
        else:
            raise TypeError("virtual_return_goods must be bool")


    def get_api_name(self):
        return "taobao.rp.returngoods.agree"

    def to_dict(self):
        request_dict = {}
        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._refund_phase is not None:
            request_dict["refund_phase"] = convert_basic(self._refund_phase)

        if self._refund_version is not None:
            request_dict["refund_version"] = convert_basic(self._refund_version)

        if self._remark is not None:
            request_dict["remark"] = convert_basic(self._remark)

        if self._address is not None:
            request_dict["address"] = convert_basic(self._address)

        if self._seller_address_id is not None:
            request_dict["seller_address_id"] = convert_basic(self._seller_address_id)

        if self._mobile is not None:
            request_dict["mobile"] = convert_basic(self._mobile)

        if self._post is not None:
            request_dict["post"] = convert_basic(self._post)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._tel is not None:
            request_dict["tel"] = convert_basic(self._tel)

        if self._post_fee_bear_role is not None:
            request_dict["post_fee_bear_role"] = convert_basic(self._post_fee_bear_role)

        if self._virtual_return_goods is not None:
            request_dict["virtual_return_goods"] = convert_basic(self._virtual_return_goods)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


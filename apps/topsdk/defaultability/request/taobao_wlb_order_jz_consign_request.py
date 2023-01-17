from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderJzConsignRequest(BaseRequest):

    def __init__(
        self,
        tid: int = None,
        sender_id: int = None,
        lg_tp_dto: object = None,
        ins_tp_dto: object = None,
        jz_receiver_to: object = None,
        ins_receiver_to: object = None,
        jz_top_args: object = None
    ):
        """
            交易号
        """
        self._tid = tid
        """
            卖家联系人地址库ID，可以通过taobao.logistics.address.search接口查询到地址库ID。如果为空，取的卖家的默认取货地址
        """
        self._sender_id = sender_id
        """
            物流公司信息
        """
        self._lg_tp_dto = lg_tp_dto
        """
            安装公司信息,需要安装时,才填写
        """
        self._ins_tp_dto = ins_tp_dto
        """
            家装收货人信息,如果为空,则取默认收货信息
        """
        self._jz_receiver_to = jz_receiver_to
        """
            安装收货人信息,如果为空,则取默认收货人信息
        """
        self._ins_receiver_to = ins_receiver_to
        """
            发货参数
        """
        self._jz_top_args = jz_top_args

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
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        if isinstance(sender_id, int):
            self._sender_id = sender_id
        else:
            raise TypeError("sender_id must be int")

    @property
    def lg_tp_dto(self):
        return self._lg_tp_dto

    @lg_tp_dto.setter
    def lg_tp_dto(self, lg_tp_dto):
        if isinstance(lg_tp_dto, object):
            self._lg_tp_dto = lg_tp_dto
        else:
            raise TypeError("lg_tp_dto must be object")

    @property
    def ins_tp_dto(self):
        return self._ins_tp_dto

    @ins_tp_dto.setter
    def ins_tp_dto(self, ins_tp_dto):
        if isinstance(ins_tp_dto, object):
            self._ins_tp_dto = ins_tp_dto
        else:
            raise TypeError("ins_tp_dto must be object")

    @property
    def jz_receiver_to(self):
        return self._jz_receiver_to

    @jz_receiver_to.setter
    def jz_receiver_to(self, jz_receiver_to):
        if isinstance(jz_receiver_to, object):
            self._jz_receiver_to = jz_receiver_to
        else:
            raise TypeError("jz_receiver_to must be object")

    @property
    def ins_receiver_to(self):
        return self._ins_receiver_to

    @ins_receiver_to.setter
    def ins_receiver_to(self, ins_receiver_to):
        if isinstance(ins_receiver_to, object):
            self._ins_receiver_to = ins_receiver_to
        else:
            raise TypeError("ins_receiver_to must be object")

    @property
    def jz_top_args(self):
        return self._jz_top_args

    @jz_top_args.setter
    def jz_top_args(self, jz_top_args):
        if isinstance(jz_top_args, object):
            self._jz_top_args = jz_top_args
        else:
            raise TypeError("jz_top_args must be object")


    def get_api_name(self):
        return "taobao.wlb.order.jz.consign"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._sender_id is not None:
            request_dict["sender_id"] = convert_basic(self._sender_id)

        if self._lg_tp_dto is not None:
            request_dict["lg_tp_dto"] = convert_struct(self._lg_tp_dto)

        if self._ins_tp_dto is not None:
            request_dict["ins_tp_dto"] = convert_struct(self._ins_tp_dto)

        if self._jz_receiver_to is not None:
            request_dict["jz_receiver_to"] = convert_struct(self._jz_receiver_to)

        if self._ins_receiver_to is not None:
            request_dict["ins_receiver_to"] = convert_struct(self._ins_receiver_to)

        if self._jz_top_args is not None:
            request_dict["jz_top_args"] = convert_struct(self._jz_top_args)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoWlbOrderJzConsignTpdto:
    def __init__(
        self,
        code: str = None,
        name: str = None
    ):
        """
            公司编码
        """
        self.code = code
        """
            公司名称
        """
        self.name = name

class TaobaoWlbOrderJzConsignTpdto:
    def __init__(
        self,
        code: str = None,
        name: str = None
    ):
        """
            公司编码
        """
        self.code = code
        """
            公司名称
        """
        self.name = name

class TaobaoWlbOrderJzConsignJzReceiverTo:
    def __init__(
        self,
        address: str = None,
        city: str = None,
        contact_name: str = None,
        country: str = None,
        district: str = None,
        mobile_phone: str = None,
        province: str = None,
        street: str = None,
        tele_phone: str = None,
        zip_code: str = None
    ):
        """
            详细地址
        """
        self.address = address
        """
            市
        """
        self.city = city
        """
            收货人名称
        """
        self.contact_name = contact_name
        """
            国家
        """
        self.country = country
        """
            区
        """
        self.district = district
        """
            手机号
        """
        self.mobile_phone = mobile_phone
        """
            省
        """
        self.province = province
        """
            街道
        """
        self.street = street
        """
            座机号
        """
        self.tele_phone = tele_phone
        """
            邮编
        """
        self.zip_code = zip_code

class TaobaoWlbOrderJzConsignJzReceiverTo:
    def __init__(
        self,
        mobile_phone: str = None,
        tele_phone: str = None,
        street: str = None,
        province: str = None,
        district: str = None,
        country: str = None,
        contact_name: str = None,
        city: str = None,
        address: str = None,
        zip_code: str = None
    ):
        """
            手机号
        """
        self.mobile_phone = mobile_phone
        """
            座机号
        """
        self.tele_phone = tele_phone
        """
            街道
        """
        self.street = street
        """
            省
        """
        self.province = province
        """
            区
        """
        self.district = district
        """
            国家
        """
        self.country = country
        """
            收货人名称
        """
        self.contact_name = contact_name
        """
            市
        """
        self.city = city
        """
            详细地址
        """
        self.address = address
        """
            邮编
        """
        self.zip_code = zip_code

class TaobaoWlbOrderJzConsignJzTopArgs:
    def __init__(
        self,
        mail_no: str = None,
        package_number: str = None,
        package_remark: str = None,
        package_volume: str = None,
        package_weight: str = None,
        zy_company: str = None,
        zy_consign_time: str = None,
        zy_phone_number: str = None
    ):
        """
            运单号,用快递或商家自有发货时,必填
        """
        self.mail_no = mail_no
        """
            包裹数量
        """
        self.package_number = package_number
        """
            包裹备注
        """
        self.package_remark = package_remark
        """
            包裹体积
        """
        self.package_volume = package_volume
        """
            包裹重量
        """
        self.package_weight = package_weight
        """
            自有物流公司名称
        """
        self.zy_company = zy_company
        """
            自有物流发货时间,时间不能早于当前时间
        """
        self.zy_consign_time = zy_consign_time
        """
            自有物流公司电话
        """
        self.zy_phone_number = zy_phone_number


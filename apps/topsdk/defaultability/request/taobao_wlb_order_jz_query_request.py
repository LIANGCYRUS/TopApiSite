from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderJzQueryRequest(BaseRequest):

    def __init__(
        self,
        tid: int = None,
        sender_id: int = None,
        jz_receiver_to: object = None,
        ins_jz_receiver_t_o: object = None
    ):
        """
            交易id
        """
        self._tid = tid
        """
            卖家联系人地址库ID，可以通过taobao.logistics.address.search接口查询到地址库ID。如果为空，取的卖家的默认取货地址
        """
        self._sender_id = sender_id
        """
            家装收货人信息
        """
        self._jz_receiver_to = jz_receiver_to
        """
            家装安装服务收货人信息
        """
        self._ins_jz_receiver_t_o = ins_jz_receiver_t_o

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
    def jz_receiver_to(self):
        return self._jz_receiver_to

    @jz_receiver_to.setter
    def jz_receiver_to(self, jz_receiver_to):
        if isinstance(jz_receiver_to, object):
            self._jz_receiver_to = jz_receiver_to
        else:
            raise TypeError("jz_receiver_to must be object")

    @property
    def ins_jz_receiver_t_o(self):
        return self._ins_jz_receiver_t_o

    @ins_jz_receiver_t_o.setter
    def ins_jz_receiver_t_o(self, ins_jz_receiver_t_o):
        if isinstance(ins_jz_receiver_t_o, object):
            self._ins_jz_receiver_t_o = ins_jz_receiver_t_o
        else:
            raise TypeError("ins_jz_receiver_t_o must be object")


    def get_api_name(self):
        return "taobao.wlb.order.jz.query"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._sender_id is not None:
            request_dict["sender_id"] = convert_basic(self._sender_id)

        if self._jz_receiver_to is not None:
            request_dict["jz_receiver_to"] = convert_struct(self._jz_receiver_to)

        if self._ins_jz_receiver_t_o is not None:
            request_dict["ins_jz_receiver_t_o"] = convert_struct(self._ins_jz_receiver_t_o)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoWlbOrderJzQueryJzReceiverTo:
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

class TaobaoWlbOrderJzQueryJzReceiverTo:
    def __init__(
        self,
        zip_code: str = None,
        tele_phone: str = None,
        street: str = None,
        province: str = None,
        mobile_phone: str = None,
        district: str = None,
        country: str = None,
        contact_name: str = None,
        city: str = None,
        address: str = None
    ):
        """
            邮编
        """
        self.zip_code = zip_code
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
            手机号
        """
        self.mobile_phone = mobile_phone
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


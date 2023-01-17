from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsOrdersGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        tid: int = None,
        buyer_nick: str = None,
        status: str = None,
        seller_confirm: str = None,
        receiver_name: str = None,
        start_created: datetime = None,
        end_created: datetime = None,
        freight_payer: str = None,
        type: str = None,
        page_no: int = None,
        page_size: int = None,
        ouid: str = None
    ):
        """
            需返回的字段列表.可选值:Shipping 物流数据结构中的以下字段: <br>
tid,order_code,seller_nick,buyer_nick,delivery_start, delivery_end,out_sid,item_title,receiver_name, created,modified,status,type,freight_payer,seller_confirm,company_name,sub_tids,is_spilt；<br>多个字段之间用","分隔。如tid,seller_nick,buyer_nick,delivery_start。
        """
        self._fields = fields
        """
            交易ID.如果加入tid参数的话,不用传其他的参数,若传入tid：非拆单场景，仅会返回一条物流订单信息；拆单场景，会返回多条物流订单信息
        """
        self._tid = tid
        """
            买家昵称
        """
        self._buyer_nick = buyer_nick
        """
            物流状态.查看数据结构 Shipping 中的status字段.
        """
        self._status = status
        """
            卖家是否发货.可选值:yes(是),no(否).如:yes
        """
        self._seller_confirm = seller_confirm
        """
            收货人姓名
        """
        self._receiver_name = receiver_name
        """
            创建时间开始
        """
        self._start_created = start_created
        """
            创建时间结束
        """
        self._end_created = end_created
        """
            谁承担运费.可选值:buyer(买家),seller(卖家).如:buyer
        """
        self._freight_payer = freight_payer
        """
            物流方式.可选值:post(平邮),express(快递),ems(EMS).如:post
        """
        self._type = type
        """
            页码.该字段没传 或 值<1 ,则默认page_no为1
        """
        self._page_no = page_no
        """
            每页条数.该字段没传 或 值<1 ,则默认page_size为40
        """
        self._page_size = page_size
        """
            系统自动生成
        """
        self._ouid = ouid

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")

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
    def buyer_nick(self):
        return self._buyer_nick

    @buyer_nick.setter
    def buyer_nick(self, buyer_nick):
        if isinstance(buyer_nick, str):
            self._buyer_nick = buyer_nick
        else:
            raise TypeError("buyer_nick must be str")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")

    @property
    def seller_confirm(self):
        return self._seller_confirm

    @seller_confirm.setter
    def seller_confirm(self, seller_confirm):
        if isinstance(seller_confirm, str):
            self._seller_confirm = seller_confirm
        else:
            raise TypeError("seller_confirm must be str")

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
    def start_created(self):
        return self._start_created

    @start_created.setter
    def start_created(self, start_created):
        if isinstance(start_created, datetime):
            self._start_created = start_created
        else:
            raise TypeError("start_created must be datetime")

    @property
    def end_created(self):
        return self._end_created

    @end_created.setter
    def end_created(self, end_created):
        if isinstance(end_created, datetime):
            self._end_created = end_created
        else:
            raise TypeError("end_created must be datetime")

    @property
    def freight_payer(self):
        return self._freight_payer

    @freight_payer.setter
    def freight_payer(self, freight_payer):
        if isinstance(freight_payer, str):
            self._freight_payer = freight_payer
        else:
            raise TypeError("freight_payer must be str")

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

    @property
    def ouid(self):
        return self._ouid

    @ouid.setter
    def ouid(self, ouid):
        if isinstance(ouid, str):
            self._ouid = ouid
        else:
            raise TypeError("ouid must be str")


    def get_api_name(self):
        return "taobao.logistics.orders.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._buyer_nick is not None:
            request_dict["buyer_nick"] = convert_basic(self._buyer_nick)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._seller_confirm is not None:
            request_dict["seller_confirm"] = convert_basic(self._seller_confirm)

        if self._receiver_name is not None:
            request_dict["receiver_name"] = convert_basic(self._receiver_name)

        if self._start_created is not None:
            request_dict["start_created"] = convert_basic(self._start_created)

        if self._end_created is not None:
            request_dict["end_created"] = convert_basic(self._end_created)

        if self._freight_payer is not None:
            request_dict["freight_payer"] = convert_basic(self._freight_payer)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._ouid is not None:
            request_dict["ouid"] = convert_basic(self._ouid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSpecialRefundsReceiveGetRequest(BaseRequest):

    def __init__(
        self,
        buyer_nick: str = None,
        end_modified: datetime = None,
        fields: list = None,
        page_no: int = None,
        page_size: int = None,
        start_modified: datetime = None,
        status: str = None,
        type: str = None,
        use_has_next: bool = None,
        buyer_open_uid: str = None
    ):
        """
            买家昵称
        """
        self._buyer_nick = buyer_nick
        """
            查询修改时间结束。格式: yyyy-MM-dd HH:mm:ss
        """
        self._end_modified = end_modified
        """
            需要返回的字段。目前支持有：refund_id, tid, title, buyer_nick, seller_nick, total_fee, status, created, refund_fee, oid, good_status, company_name, sid, payment, reason, desc, has_good_return, modified, order_status,refund_phase
        """
        self._fields = fields
        """
            页码。取值范围:大于零的整数; 默认值:1
        """
        self._page_no = page_no
        """
            每页条数。取值范围:大于零的整数; 默认值:40;最大值:100
        """
        self._page_size = page_size
        """
            查询修改时间开始。格式: yyyy-MM-dd HH:mm:ss
        """
        self._start_modified = start_modified
        """
            退款状态，默认查询所有退款状态的数据，除了默认值外每次只能查询一种状态。WAIT_SELLER_AGREE(买家已经申请退款，等待卖家同意) WAIT_BUYER_RETURN_GOODS(卖家已经同意退款，等待买家退货) WAIT_SELLER_CONFIRM_GOODS(买家已经退货，等待卖家确认收货) SELLER_REFUSE_BUYER(卖家拒绝退款) CLOSED(退款关闭) SUCCESS(退款成功)
        """
        self._status = status
        """
            交易类型列表，一次查询多种类型可用半角逗号分隔，默认同时查询guarantee_trade, auto_delivery这两种类型的数据，<a href="http://open.taobao.com/doc/detail.htm?id=102855" target="_blank">查看可选值</a>
        """
        self._type = type
        """
            是否启用has_next的分页方式，如果指定true,则返回的结果中不包含总记录数，但是会新增一个是否存在下一页的的字段，通过此种方式获取增量退款，接口调用成功率在原有的基础上有所提升。
        """
        self._use_has_next = use_has_next
        """
            买家openId
        """
        self._buyer_open_uid = buyer_open_uid

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
    def end_modified(self):
        return self._end_modified

    @end_modified.setter
    def end_modified(self, end_modified):
        if isinstance(end_modified, datetime):
            self._end_modified = end_modified
        else:
            raise TypeError("end_modified must be datetime")

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
    def start_modified(self):
        return self._start_modified

    @start_modified.setter
    def start_modified(self, start_modified):
        if isinstance(start_modified, datetime):
            self._start_modified = start_modified
        else:
            raise TypeError("start_modified must be datetime")

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
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")

    @property
    def use_has_next(self):
        return self._use_has_next

    @use_has_next.setter
    def use_has_next(self, use_has_next):
        if isinstance(use_has_next, bool):
            self._use_has_next = use_has_next
        else:
            raise TypeError("use_has_next must be bool")

    @property
    def buyer_open_uid(self):
        return self._buyer_open_uid

    @buyer_open_uid.setter
    def buyer_open_uid(self, buyer_open_uid):
        if isinstance(buyer_open_uid, str):
            self._buyer_open_uid = buyer_open_uid
        else:
            raise TypeError("buyer_open_uid must be str")


    def get_api_name(self):
        return "taobao.special.refunds.receive.get"

    def to_dict(self):
        request_dict = {}
        if self._buyer_nick is not None:
            request_dict["buyer_nick"] = convert_basic(self._buyer_nick)

        if self._end_modified is not None:
            request_dict["end_modified"] = convert_basic(self._end_modified)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._start_modified is not None:
            request_dict["start_modified"] = convert_basic(self._start_modified)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._use_has_next is not None:
            request_dict["use_has_next"] = convert_basic(self._use_has_next)

        if self._buyer_open_uid is not None:
            request_dict["buyer_open_uid"] = convert_basic(self._buyer_open_uid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


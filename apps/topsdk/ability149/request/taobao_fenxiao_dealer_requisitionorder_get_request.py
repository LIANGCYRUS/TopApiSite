from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDealerRequisitionorderGetRequest(BaseRequest):

    def __init__(
        self,
        start_date: datetime = None,
        end_date: datetime = None,
        page_no: int = None,
        page_size: int = None,
        order_status: int = None,
        identity: int = None,
        fields: str = None
    ):
        """
            采购申请/经销采购单最早修改时间
        """
        self._start_date = start_date
        """
            采购申请/经销采购单最迟修改时间。与start_date字段的最大时间间隔不能超过30天
        """
        self._end_date = end_date
        """
            页码（大于0的整数。无值或小于1的值按默认值1计）
        """
        self._page_no = page_no
        """
            每页条数（大于0但小于等于50的整数。无值或大于50或小于1的值按默认值50计）
        """
        self._page_size = page_size
        """
            采购申请/经销采购单状态。
0：全部状态。
1：分销商提交申请，待供应商审核。
2：供应商驳回申请，待分销商确认。
3：供应商修改后，待分销商确认。
4：分销商拒绝修改，待供应商再审核。
5：审核通过下单成功，待分销商付款。
7：付款成功，待供应商发货。
8：供应商发货，待分销商收货。
9：分销商收货，交易成功。
10：采购申请/经销采购单关闭。

注：无值按默认值0计，超出状态范围返回错误信息。
        """
        self._order_status = order_status
        """
            查询者自己在所要查询的采购申请/经销采购单中的身份。
1：供应商。
2：分销商。
注：填写其他值当做错误处理。
        """
        self._identity = identity
        """
            多个字段用","分隔。 fields 如果为空：返回所有采购申请/经销采购单对象(dealer_orders)字段。 如果不为空：返回指定采购单对象(dealer_orders)字段。 例1： dealer_order_details.product_id 表示只返回product_id 例2： dealer_order_details 表示只返回明细列表
        """
        self._fields = fields

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, datetime):
            self._start_date = start_date
        else:
            raise TypeError("start_date must be datetime")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, datetime):
            self._end_date = end_date
        else:
            raise TypeError("end_date must be datetime")

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
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        if isinstance(order_status, int):
            self._order_status = order_status
        else:
            raise TypeError("order_status must be int")

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, identity):
        if isinstance(identity, int):
            self._identity = identity
        else:
            raise TypeError("identity must be int")

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, str):
            self._fields = fields
        else:
            raise TypeError("fields must be str")


    def get_api_name(self):
        return "taobao.fenxiao.dealer.requisitionorder.get"

    def to_dict(self):
        request_dict = {}
        if self._start_date is not None:
            request_dict["start_date"] = convert_basic(self._start_date)

        if self._end_date is not None:
            request_dict["end_date"] = convert_basic(self._end_date)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._order_status is not None:
            request_dict["order_status"] = convert_basic(self._order_status)

        if self._identity is not None:
            request_dict["identity"] = convert_basic(self._identity)

        if self._fields is not None:
            request_dict["fields"] = convert_basic(self._fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


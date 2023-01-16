from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoRefundQueryRequest(BaseRequest):

    def __init__(
        self,
        start_date: datetime = None,
        end_date: datetime = None,
        page_no: int = None,
        page_size: int = None,
        query_seller_refund: bool = None,
        trade_types: list = None,
        user_role_type: int = None,
        channel_codes: list = None,
        refund_flow_types: list = None
    ):
        """
            查询退款单的修改时间开始,格式如:yyyy-MM-dd HH:mm:ss
        """
        self._start_date = start_date
        """
            查询退款单的修改时间结束,格式如:yyyy-MM-dd HH:mm:ss
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
            是否查询下游消费者的退款信息
        """
        self._query_seller_refund = query_seller_refund
        """
            查询的经营模式，当不指定时，默认查询代销订单 代销：1 经销：2 寄售（自营寄售）：5 平台寄售
        """
        self._trade_types = trade_types
        """
            角色，供应商：2，分销商：1
        """
        self._user_role_type = user_role_type
        """
            渠道市场编码，可批量指定。 当不指定时，按照配置的分销市场生效 渠道编码枚举：1-供销平台（淘宝）；2-供销平台（天猫）；3-供销平台（天猫超市）；5-供销平台（淘乡甜）；110001-供销平台（全球购）；110007-淘分销；200002-消费电子市场
        """
        self._channel_codes = channel_codes
        """
            退款流程类型：4：发货前退款；1：发货后退款不退货；2：发货后退款退货；3：售后退款；5：拒收；6：售后退货退款
        """
        self._refund_flow_types = refund_flow_types

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
    def query_seller_refund(self):
        return self._query_seller_refund

    @query_seller_refund.setter
    def query_seller_refund(self, query_seller_refund):
        if isinstance(query_seller_refund, bool):
            self._query_seller_refund = query_seller_refund
        else:
            raise TypeError("query_seller_refund must be bool")

    @property
    def trade_types(self):
        return self._trade_types

    @trade_types.setter
    def trade_types(self, trade_types):
        if isinstance(trade_types, list):
            self._trade_types = trade_types
        else:
            raise TypeError("trade_types must be list")

    @property
    def user_role_type(self):
        return self._user_role_type

    @user_role_type.setter
    def user_role_type(self, user_role_type):
        if isinstance(user_role_type, int):
            self._user_role_type = user_role_type
        else:
            raise TypeError("user_role_type must be int")

    @property
    def channel_codes(self):
        return self._channel_codes

    @channel_codes.setter
    def channel_codes(self, channel_codes):
        if isinstance(channel_codes, list):
            self._channel_codes = channel_codes
        else:
            raise TypeError("channel_codes must be list")

    @property
    def refund_flow_types(self):
        return self._refund_flow_types

    @refund_flow_types.setter
    def refund_flow_types(self, refund_flow_types):
        if isinstance(refund_flow_types, list):
            self._refund_flow_types = refund_flow_types
        else:
            raise TypeError("refund_flow_types must be list")


    def get_api_name(self):
        return "taobao.fenxiao.refund.query"

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

        if self._query_seller_refund is not None:
            request_dict["query_seller_refund"] = convert_basic(self._query_seller_refund)

        if self._trade_types is not None:
            request_dict["trade_types"] = convert_basic_list(self._trade_types)

        if self._user_role_type is not None:
            request_dict["user_role_type"] = convert_basic(self._user_role_type)

        if self._channel_codes is not None:
            request_dict["channel_codes"] = convert_basic_list(self._channel_codes)

        if self._refund_flow_types is not None:
            request_dict["refund_flow_types"] = convert_basic_list(self._refund_flow_types)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


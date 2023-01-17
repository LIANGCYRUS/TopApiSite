from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportsOrderGetRequest(BaseRequest):

    def __init__(
        self,
        trade_id: int = None,
        gmt_create_start: datetime = None,
        gmt_create_end: datetime = None,
        status_code: str = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            交易订单号
        """
        self._trade_id = trade_id
        """
            交易订单开始创建时间
        """
        self._gmt_create_start = gmt_create_start
        """
            交易订单结束创建时间
        """
        self._gmt_create_end = gmt_create_end
        """
            物流订单状态编码。以下依（物流订单状态编码，描述）的形式列举出来：(TIN_CONSING,发货中),(SENT_WAIT_COMPANY_MAKE_SURE,待仓库收货),(ORDER_CANCELED,订单关闭),(COMPANY_MAKE_SURE,海外仓已揽收),(REJECTED_RECEIVED_BY_COMPANY,海外仓拒收),(ORDER_REFUNDING,退货中),(ORDER_REFUND_BY_COMPANY,订单已退货),(EXCEPTION_IN_COMPANY,海外仓内异常),(FAILED_PAID_SHIPPING_FEE,支付失败),(PAID_SHIPPING_FEE,待仓库发货),(COMPANY_CONSIGN_CONFIRM,海外仓已发货),(WAIT_CUSTOMS_MAKE_SURE,清关已收货),(EXCEPTION_IN_CUSTOMS,清关异常),(CUSTOMSING,清关中),(COMPANY_DELIVERY,国内配送)。
        """
        self._status_code = status_code
        """
            页码。取值范围:大于零的整数; 默认值:1
        """
        self._page_no = page_no
        """
            每页条数。取值范围:大于0小于等于100的整数; 默认值:40; 最小值：1；最大值:20
        """
        self._page_size = page_size

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
    def gmt_create_start(self):
        return self._gmt_create_start

    @gmt_create_start.setter
    def gmt_create_start(self, gmt_create_start):
        if isinstance(gmt_create_start, datetime):
            self._gmt_create_start = gmt_create_start
        else:
            raise TypeError("gmt_create_start must be datetime")

    @property
    def gmt_create_end(self):
        return self._gmt_create_end

    @gmt_create_end.setter
    def gmt_create_end(self, gmt_create_end):
        if isinstance(gmt_create_end, datetime):
            self._gmt_create_end = gmt_create_end
        else:
            raise TypeError("gmt_create_end must be datetime")

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        if isinstance(status_code, str):
            self._status_code = status_code
        else:
            raise TypeError("status_code must be str")

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


    def get_api_name(self):
        return "taobao.wlb.imports.order.get"

    def to_dict(self):
        request_dict = {}
        if self._trade_id is not None:
            request_dict["trade_id"] = convert_basic(self._trade_id)

        if self._gmt_create_start is not None:
            request_dict["gmt_create_start"] = convert_basic(self._gmt_create_start)

        if self._gmt_create_end is not None:
            request_dict["gmt_create_end"] = convert_basic(self._gmt_create_end)

        if self._status_code is not None:
            request_dict["status_code"] = convert_basic(self._status_code)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


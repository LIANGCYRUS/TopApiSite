from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsExpressModifyAppointRequest(BaseRequest):

    def __init__(
        self,
        express_modify_appoint_top_request: object = None
    ):
        """
            改约请求对象
        """
        self._express_modify_appoint_top_request = express_modify_appoint_top_request

    @property
    def express_modify_appoint_top_request(self):
        return self._express_modify_appoint_top_request

    @express_modify_appoint_top_request.setter
    def express_modify_appoint_top_request(self, express_modify_appoint_top_request):
        if isinstance(express_modify_appoint_top_request, object):
            self._express_modify_appoint_top_request = express_modify_appoint_top_request
        else:
            raise TypeError("express_modify_appoint_top_request must be object")


    def get_api_name(self):
        return "taobao.logistics.express.modify.appoint"

    def to_dict(self):
        request_dict = {}
        if self._express_modify_appoint_top_request is not None:
            request_dict["express_modify_appoint_top_request"] = convert_struct(self._express_modify_appoint_top_request)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoLogisticsExpressModifyAppointExpressModifyAppointTopRequestDto:
    def __init__(
        self,
        sc_date: datetime = None,
        sub_trade_ids: list = None,
        trade_id: str = None,
        seller_id: int = None,
        receiver_mobile: str = None,
        os_date: datetime = None,
        receiver_name: str = None,
        feature: str = None,
        out_order_code: str = None,
        receiver_address: str = None
    ):
        """
            应到达日期
        """
        self.sc_date = sc_date
        """
            子交易单号
        """
        self.sub_trade_ids = sub_trade_ids
        """
            交易号
        """
        self.trade_id = trade_id
        """
            卖家Id
        """
        self.seller_id = seller_id
        """
            收货人电话
        """
        self.receiver_mobile = receiver_mobile
        """
            改约日期
        """
        self.os_date = os_date
        """
            收货人姓名
        """
        self.receiver_name = receiver_name
        """
            扩展字段
        """
        self.feature = feature
        """
            外部订单号
        """
        self.out_order_code = out_order_code
        """
            收货人地址
        """
        self.receiver_address = receiver_address


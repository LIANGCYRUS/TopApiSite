from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRefundStatusGetRequest(BaseRequest):

    def __init__(
        self,
        query_param: object = None
    ):
        """
            入参对象
        """
        self._query_param = query_param

    @property
    def query_param(self):
        return self._query_param

    @query_param.setter
    def query_param(self, query_param):
        if isinstance(query_param, object):
            self._query_param = query_param
        else:
            raise TypeError("query_param must be object")


    def get_api_name(self):
        return "taobao.refund.status.get"

    def to_dict(self):
        request_dict = {}
        if self._query_param is not None:
            request_dict["query_param"] = convert_struct(self._query_param)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoRefundStatusGetRefundQueryByOrderIdRequest:
    def __init__(
        self,
        biz_order_id: int = None
    ):
        """
            订单号
        """
        self.biz_order_id = biz_order_id


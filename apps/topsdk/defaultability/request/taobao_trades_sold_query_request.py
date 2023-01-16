from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradesSoldQueryRequest(BaseRequest):

    def __init__(
        self,
        query_list: list = None,
        scene: str = None,
        order_type: str = None
    ):
        """
            查询条件列表，多个条件之间是OR关系，最多支持20个。receiver_name、receiver_mobile、receiver_phone至少有一个值不为空。
        """
        self._query_list = query_list
        """
            业务场景编码。不同场景，策略不同。请根据产品功能选择相应的场景编号。可选的场景：1001(客服咨询)、1002(售后服务)，<a href="https://open.taobao.com/doc.htm?docId=120186&docType=1" target="_blank">详情点击</a>
        """
        self._scene = scene
        """
            订单类型，默认值为1，可选值为：交易(1)，分销(2)，换货(3)
        """
        self._order_type = order_type

    @property
    def query_list(self):
        return self._query_list

    @query_list.setter
    def query_list(self, query_list):
        if isinstance(query_list, list):
            self._query_list = query_list
        else:
            raise TypeError("query_list must be list")

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, scene):
        if isinstance(scene, str):
            self._scene = scene
        else:
            raise TypeError("scene must be str")

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, str):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be str")


    def get_api_name(self):
        return "taobao.trades.sold.query"

    def to_dict(self):
        request_dict = {}
        if self._query_list is not None:
            request_dict["query_list"] = convert_struct_list(self._query_list)

        if self._scene is not None:
            request_dict["scene"] = convert_basic(self._scene)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoTradesSoldQueryOrderQuery:
    def __init__(
        self,
        receiver_phone: str = None,
        receiver_mobile: str = None,
        receiver_name: str = None,
        end_created: datetime = None,
        start_created: datetime = None
    ):
        """
            收件人电话号码
        """
        self.receiver_phone = receiver_phone
        """
            收件人的手机号
        """
        self.receiver_mobile = receiver_mobile
        """
            收件人的姓名
        """
        self.receiver_name = receiver_name
        """
            查询三个月内交易创建时间开始。格式:yyyy-MM-dd HH:mm:ss
        """
        self.end_created = end_created
        """
            查询交易创建时间结束。格式:yyyy-MM-dd HH:mm:ss
        """
        self.start_created = start_created


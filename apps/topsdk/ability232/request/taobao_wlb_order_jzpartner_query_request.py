from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOrderJzpartnerQueryRequest(BaseRequest):

    def __init__(
        self,
        taobao_trade_id: int = None,
        service_type: int = None
    ):
        """
            淘宝交易订单号，如果不填写Tid则必须填写serviceType。如果填写Tid，则表明只需要查询对应订单的服务商。
        """
        self._taobao_trade_id = taobao_trade_id
        """
            serviceType表示查询所有的支持服务类型的服务商。 家装干线服务     11 家装干支服务     12 家装干支装服务   13 卫浴大件干线     14 卫浴大件干支     15 卫浴大件安装     16 地板干线         17 地板干支         18 地板安装         19 灯具安装         20 卫浴小件安装     21 （注：同一个服务商针对不同类型的serviceType是具有不同的tpCode的）
        """
        self._service_type = service_type

    @property
    def taobao_trade_id(self):
        return self._taobao_trade_id

    @taobao_trade_id.setter
    def taobao_trade_id(self, taobao_trade_id):
        if isinstance(taobao_trade_id, int):
            self._taobao_trade_id = taobao_trade_id
        else:
            raise TypeError("taobao_trade_id must be int")

    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        if isinstance(service_type, int):
            self._service_type = service_type
        else:
            raise TypeError("service_type must be int")


    def get_api_name(self):
        return "taobao.wlb.order.jzpartner.query"

    def to_dict(self):
        request_dict = {}
        if self._taobao_trade_id is not None:
            request_dict["taobao_trade_id"] = convert_basic(self._taobao_trade_id)

        if self._service_type is not None:
            request_dict["service_type"] = convert_basic(self._service_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


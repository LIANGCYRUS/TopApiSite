from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsDummySendRequest(BaseRequest):

    def __init__(
        self,
        feature: str = None,
        seller_ip: str = None,
        tid: int = None
    ):
        """
            feature参数格式<br>范例: identCode=tid1:识别码1,识别码2|tid2:识别码3;machineCode=tid3:3C机器号A,3C机器号B<br>identCode为识别码的KEY,machineCode为3C的KEY,多个key之间用”;”分隔<br>“tid1:识别码1,识别码2|tid2:识别码3”为identCode对应的value。"|"不同商品间的分隔符。<br>例1商品和2商品，之间就用"|"分开。<br>TID就是商品代表的子订单号，对应taobao.trade.fullinfo.get 接口获得的oid字段。(通过OID可以唯一定位到当前商品上)<br>":"TID和具体传入参数间的分隔符。冒号前表示TID,之后代表该商品的参数属性。<br>"," 属性间分隔符。（对应商品数量，当存在一个商品的数量超过1个时，用逗号分开）。<br>具体:当订单中A商品的数量为2个，其中手机串号分别为"12345","67890"。<br>参数格式：identCode=TIDA:12345,67890。TIDA对应了A宝贝，冒号后用逗号分隔的"12345","67890".说明本订单A宝贝的数量为2，值分别为"12345","67890"。<br>当存在"|"时，就说明订单中存在多个商品，商品间用"|"分隔了开来。|"之后的内容含义同上。
        """
        self._feature = feature
        """
            商家的IP地址
        """
        self._seller_ip = seller_ip
        """
            淘宝交易ID
        """
        self._tid = tid

    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, feature):
        if isinstance(feature, str):
            self._feature = feature
        else:
            raise TypeError("feature must be str")

    @property
    def seller_ip(self):
        return self._seller_ip

    @seller_ip.setter
    def seller_ip(self, seller_ip):
        if isinstance(seller_ip, str):
            self._seller_ip = seller_ip
        else:
            raise TypeError("seller_ip must be str")

    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, int):
            self._tid = tid
        else:
            raise TypeError("tid must be int")


    def get_api_name(self):
        return "taobao.logistics.dummy.send"

    def to_dict(self):
        request_dict = {}
        if self._feature is not None:
            request_dict["feature"] = convert_basic(self._feature)

        if self._seller_ip is not None:
            request_dict["seller_ip"] = convert_basic(self._seller_ip)

        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


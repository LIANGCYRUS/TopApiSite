from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaAscpLogisticsOfflineSendRequest(BaseRequest):

    def __init__(
        self,
        sender_id: int = None,
        feature: str = None,
        tid: str = None,
        sub_tid: str = None,
        consign_pkgs: list = None,
        cancel_id: int = None
    ):
        """
            卖家联系人地址库ID，可以通过taobao.logistics.address.search接口查询到地址库ID。如果为空，取的卖家的默认取货地址
        """
        self._sender_id = sender_id
        """
            feature参数格式 范例: identCode=tid1:识别码1,识别码2|tid2:识别码3;machineCode=tid3:3C机器号A,3C机器号B identCode为识别码的KEY,machineCode为3C的KEY,多个key之间用”;”分隔 “tid1:识别码1,识别码2|tid2:识别码3”为identCode对应的value。 "|"不同商品间的分隔符。 例1商品和2商品，之间就用"|"分开。 TID就是商品代表的子订单号，对应taobao.trade.fullinfo.get 接口获得的oid字段。(通过OID可以唯一定位到当前商品上) ":"TID和具体传入参数间的分隔符。冒号前表示TID,之后代表该商品的参数属性。 "," 属性间分隔符。（对应商品数量，当存在一个商品的数量超过1个时，用逗号分开）。 具体:当订单中A商品的数量为2个，其中手机串号分别为"12345","67890"。 参数格式：identCode=TIDA:12345,67890。 TIDA对应了A宝贝，冒号后用逗号分隔的"12345","67890".说明本订单A宝贝的数量为2，值分别为"12345","67890"。 当存在"|"时，就说明订单中存在多个商品，商品间用"|"分隔了开来。|"之后的内容含义同上。retailStoreId=12345，发货门店ID或仓信息。retailStoreType=STORE: 发货门店类别，STORE表示门店，WAREHOUSE表示电商仓。对于全渠道订单回传的商家，retailStoreId和retailStoreType字段为必填字段
        """
        self._feature = feature
        """
            淘宝交易ID
        """
        self._tid = tid
        """
            需要拆单发货的子订单集合，针对的是一笔交易下有多个子订单需要分开发货的场景；1次可传人多个子订单号，子订单间用逗号隔开；为空表示不做拆单发货。
        """
        self._sub_tid = sub_tid
        """
            包裹信息
        """
        self._consign_pkgs = consign_pkgs
        """
            卖家联系人地址库ID，可以通过taobao.logistics.address.search接口查询到地址库ID。 如果为空，取的卖家的默认退货地址
        """
        self._cancel_id = cancel_id

    @property
    def sender_id(self):
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        if isinstance(sender_id, int):
            self._sender_id = sender_id
        else:
            raise TypeError("sender_id must be int")

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
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, str):
            self._tid = tid
        else:
            raise TypeError("tid must be str")

    @property
    def sub_tid(self):
        return self._sub_tid

    @sub_tid.setter
    def sub_tid(self, sub_tid):
        if isinstance(sub_tid, str):
            self._sub_tid = sub_tid
        else:
            raise TypeError("sub_tid must be str")

    @property
    def consign_pkgs(self):
        return self._consign_pkgs

    @consign_pkgs.setter
    def consign_pkgs(self, consign_pkgs):
        if isinstance(consign_pkgs, list):
            self._consign_pkgs = consign_pkgs
        else:
            raise TypeError("consign_pkgs must be list")

    @property
    def cancel_id(self):
        return self._cancel_id

    @cancel_id.setter
    def cancel_id(self, cancel_id):
        if isinstance(cancel_id, int):
            self._cancel_id = cancel_id
        else:
            raise TypeError("cancel_id must be int")


    def get_api_name(self):
        return "alibaba.ascp.logistics.offline.send"

    def to_dict(self):
        request_dict = {}
        if self._sender_id is not None:
            request_dict["sender_id"] = convert_basic(self._sender_id)

        if self._feature is not None:
            request_dict["feature"] = convert_basic(self._feature)

        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._sub_tid is not None:
            request_dict["sub_tid"] = convert_basic(self._sub_tid)

        if self._consign_pkgs is not None:
            request_dict["consign_pkgs"] = convert_struct_list(self._consign_pkgs)

        if self._cancel_id is not None:
            request_dict["cancel_id"] = convert_basic(self._cancel_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class AlibabaAscpLogisticsOfflineSendTopConsignPkgRequest:
    def __init__(
        self,
        out_sid: str = None,
        company_code: str = None
    ):
        """
            运单号.具体一个物流公司的真实运单号码。淘宝官方物流会校验，请谨慎传入
        """
        self.out_sid = out_sid
        """
            物流公司代码.如"POST"就代表中国邮政,"ZJS"就代表宅急送.调用 taobao.logistics.companies.get 获取
        """
        self.company_code = company_code


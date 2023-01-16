from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaAscpLogisticsConsignResendRequest(BaseRequest):

    def __init__(
        self,
        tid: str = None,
        sub_tids: str = None,
        consign_pkgs: list = None
    ):
        """
            订单id
        """
        self._tid = tid
        """
            拆单子订单列表，对应的数据是：子订单号列表。可以不传，但是如果传了则必须符合传递的规则。子订单必须是操作的物流订单的子订单的真子集
        """
        self._sub_tids = sub_tids
        """
            包裹包含的运单号及快递公司编号,多包裹时，需要包含所有包裹的运单号等信息
        """
        self._consign_pkgs = consign_pkgs

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
    def sub_tids(self):
        return self._sub_tids

    @sub_tids.setter
    def sub_tids(self, sub_tids):
        if isinstance(sub_tids, str):
            self._sub_tids = sub_tids
        else:
            raise TypeError("sub_tids must be str")

    @property
    def consign_pkgs(self):
        return self._consign_pkgs

    @consign_pkgs.setter
    def consign_pkgs(self, consign_pkgs):
        if isinstance(consign_pkgs, list):
            self._consign_pkgs = consign_pkgs
        else:
            raise TypeError("consign_pkgs must be list")


    def get_api_name(self):
        return "alibaba.ascp.logistics.consign.resend"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._sub_tids is not None:
            request_dict["sub_tids"] = convert_basic(self._sub_tids)

        if self._consign_pkgs is not None:
            request_dict["consign_pkgs"] = convert_struct_list(self._consign_pkgs)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class AlibabaAscpLogisticsConsignResendTopConsignPkgRequest:
    def __init__(
        self,
        company_code: str = None,
        out_sid: str = None
    ):
        """
            物流公司代码.如"POST"代表中国邮政,"ZJS"代表宅急送。调用 taobao.logistics.companies.get 获取
        """
        self.company_code = company_code
        """
            运单号.具体一个物流公司的真实运单号码。淘宝官方物流会校验，请谨慎传入
        """
        self.out_sid = out_sid


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRpRefundsAgreeRequest(BaseRequest):

    def __init__(
        self,
        code: str = None,
        refund_infos: str = None
    ):
        """
            短信验证码，如果退款金额达到一定的数量，后端会返回调用失败，并同时往卖家的手机发送一条短信验证码。接下来用收到的短信验证码再次发起API调用即可完成退款操作。
        """
        self._code = code
        """
            退款信息，格式：refund_id|amount|version|phase，其中refund_id为退款编号，amount为退款金额（以分为单位），version为退款最后更新时间（时间戳格式），phase为退款阶段（可选值为：onsale, aftersale，天猫退款必值，淘宝退款不需要传），多个退款以半角逗号分隔。
        """
        self._refund_infos = refund_infos

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if isinstance(code, str):
            self._code = code
        else:
            raise TypeError("code must be str")

    @property
    def refund_infos(self):
        return self._refund_infos

    @refund_infos.setter
    def refund_infos(self, refund_infos):
        if isinstance(refund_infos, str):
            self._refund_infos = refund_infos
        else:
            raise TypeError("refund_infos must be str")


    def get_api_name(self):
        return "taobao.rp.refunds.agree"

    def to_dict(self):
        request_dict = {}
        if self._code is not None:
            request_dict["code"] = convert_basic(self._code)

        if self._refund_infos is not None:
            request_dict["refund_infos"] = convert_basic(self._refund_infos)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


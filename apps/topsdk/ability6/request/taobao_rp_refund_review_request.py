from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRpRefundReviewRequest(BaseRequest):

    def __init__(
        self,
        operator: str = None,
        refund_id: int = None,
        refund_phase: str = None,
        refund_version: int = None,
        message: str = None,
        result: bool = None
    ):
        """
            审核人姓名
        """
        self._operator = operator
        """
            退款单编号
        """
        self._refund_id = refund_id
        """
            退款阶段，可选值：售中：onsale，售后：aftersale
        """
        self._refund_phase = refund_phase
        """
            退款最后更新时间，以时间戳的方式表示
        """
        self._refund_version = refund_version
        """
            审核留言
        """
        self._message = message
        """
            审核是否可用于批量退款，可选值：true（审核通过），false（审核不通过或反审核）
        """
        self._result = result

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        if isinstance(operator, str):
            self._operator = operator
        else:
            raise TypeError("operator must be str")

    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        if isinstance(refund_id, int):
            self._refund_id = refund_id
        else:
            raise TypeError("refund_id must be int")

    @property
    def refund_phase(self):
        return self._refund_phase

    @refund_phase.setter
    def refund_phase(self, refund_phase):
        if isinstance(refund_phase, str):
            self._refund_phase = refund_phase
        else:
            raise TypeError("refund_phase must be str")

    @property
    def refund_version(self):
        return self._refund_version

    @refund_version.setter
    def refund_version(self, refund_version):
        if isinstance(refund_version, int):
            self._refund_version = refund_version
        else:
            raise TypeError("refund_version must be int")

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        if isinstance(message, str):
            self._message = message
        else:
            raise TypeError("message must be str")

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, result):
        if isinstance(result, bool):
            self._result = result
        else:
            raise TypeError("result must be bool")


    def get_api_name(self):
        return "taobao.rp.refund.review"

    def to_dict(self):
        request_dict = {}
        if self._operator is not None:
            request_dict["operator"] = convert_basic(self._operator)

        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._refund_phase is not None:
            request_dict["refund_phase"] = convert_basic(self._refund_phase)

        if self._refund_version is not None:
            request_dict["refund_version"] = convert_basic(self._refund_version)

        if self._message is not None:
            request_dict["message"] = convert_basic(self._message)

        if self._result is not None:
            request_dict["result"] = convert_basic(self._result)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


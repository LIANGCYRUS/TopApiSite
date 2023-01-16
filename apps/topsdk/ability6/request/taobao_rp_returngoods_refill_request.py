from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRpReturngoodsRefillRequest(BaseRequest):

    def __init__(
        self,
        refund_id: int = None,
        refund_phase: str = None,
        logistics_waybill_no: str = None,
        logistics_company_code: str = None
    ):
        """
            退款单编号
        """
        self._refund_id = refund_id
        """
            退款阶段，可选值：售中：onsale，售后：aftersale
        """
        self._refund_phase = refund_phase
        """
            物流公司运单号
        """
        self._logistics_waybill_no = logistics_waybill_no
        """
            物流公司编号
        """
        self._logistics_company_code = logistics_company_code

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
    def logistics_waybill_no(self):
        return self._logistics_waybill_no

    @logistics_waybill_no.setter
    def logistics_waybill_no(self, logistics_waybill_no):
        if isinstance(logistics_waybill_no, str):
            self._logistics_waybill_no = logistics_waybill_no
        else:
            raise TypeError("logistics_waybill_no must be str")

    @property
    def logistics_company_code(self):
        return self._logistics_company_code

    @logistics_company_code.setter
    def logistics_company_code(self, logistics_company_code):
        if isinstance(logistics_company_code, str):
            self._logistics_company_code = logistics_company_code
        else:
            raise TypeError("logistics_company_code must be str")


    def get_api_name(self):
        return "taobao.rp.returngoods.refill"

    def to_dict(self):
        request_dict = {}
        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._refund_phase is not None:
            request_dict["refund_phase"] = convert_basic(self._refund_phase)

        if self._logistics_waybill_no is not None:
            request_dict["logistics_waybill_no"] = convert_basic(self._logistics_waybill_no)

        if self._logistics_company_code is not None:
            request_dict["logistics_company_code"] = convert_basic(self._logistics_company_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


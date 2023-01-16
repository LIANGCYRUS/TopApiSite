from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRpReturngoodsRefuseRequest(BaseRequest):

    def __init__(
        self,
        refund_id: int = None,
        refund_phase: str = None,
        refund_version: int = None,
        refuse_proof: bytes = None,
        refuse_reason_id: int = None
    ):
        """
            退款编号
        """
        self._refund_id = refund_id
        """
            退款服务状态，售后或者售中
        """
        self._refund_phase = refund_phase
        """
            退款版本号
        """
        self._refund_version = refund_version
        """
            拒绝退货凭证图片，必须图片格式，大小不能超过5M
        """
        self._refuse_proof = refuse_proof
        """
            拒绝原因编号，会提供拒绝原因列表供选择
        """
        self._refuse_reason_id = refuse_reason_id

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
    def refuse_proof(self):
        return self._refuse_proof

    @refuse_proof.setter
    def refuse_proof(self, refuse_proof):
        if isinstance(refuse_proof, bytes):
            self._refuse_proof = refuse_proof
        else:
            raise TypeError("refuse_proof must be bytes")

    @property
    def refuse_reason_id(self):
        return self._refuse_reason_id

    @refuse_reason_id.setter
    def refuse_reason_id(self, refuse_reason_id):
        if isinstance(refuse_reason_id, int):
            self._refuse_reason_id = refuse_reason_id
        else:
            raise TypeError("refuse_reason_id must be int")


    def get_api_name(self):
        return "taobao.rp.returngoods.refuse"

    def to_dict(self):
        request_dict = {}
        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._refund_phase is not None:
            request_dict["refund_phase"] = convert_basic(self._refund_phase)

        if self._refund_version is not None:
            request_dict["refund_version"] = convert_basic(self._refund_version)

        if self._refuse_reason_id is not None:
            request_dict["refuse_reason_id"] = convert_basic(self._refuse_reason_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._refuse_proof is not None:
            file_param_dict["refuse_proof"] = convert_basic(self._refuse_proof)
        return file_param_dict


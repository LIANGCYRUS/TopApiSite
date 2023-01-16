from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRefundNegotiatereturnRequest(BaseRequest):

    def __init__(
        self,
        refund_id: int = None,
        refund_version: int = None,
        refund_fee: int = None,
        address_id: int = None
    ):
        """
            退款编号
        """
        self._refund_id = refund_id
        """
            退款版本号
        """
        self._refund_version = refund_version
        """
            退款金额，单位（分）
        """
        self._refund_fee = refund_fee
        """
            地址ID，通过协商退货退款渲染接口获取到的
        """
        self._address_id = address_id

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
    def refund_version(self):
        return self._refund_version

    @refund_version.setter
    def refund_version(self, refund_version):
        if isinstance(refund_version, int):
            self._refund_version = refund_version
        else:
            raise TypeError("refund_version must be int")

    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, refund_fee):
        if isinstance(refund_fee, int):
            self._refund_fee = refund_fee
        else:
            raise TypeError("refund_fee must be int")

    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        if isinstance(address_id, int):
            self._address_id = address_id
        else:
            raise TypeError("address_id must be int")


    def get_api_name(self):
        return "taobao.refund.negotiatereturn"

    def to_dict(self):
        request_dict = {}
        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._refund_version is not None:
            request_dict["refund_version"] = convert_basic(self._refund_version)

        if self._refund_fee is not None:
            request_dict["refund_fee"] = convert_basic(self._refund_fee)

        if self._address_id is not None:
            request_dict["address_id"] = convert_basic(self._address_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


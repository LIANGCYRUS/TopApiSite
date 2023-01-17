from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbImportThreeplOfflineConsignRequest(BaseRequest):

    def __init__(
        self,
        trade_id: int = None,
        res_id: int = None,
        res_code: str = None,
        from_id: int = None,
        waybill_no: str = None
    ):
        """
            交易单号
        """
        self._trade_id = trade_id
        """
            资源id
        """
        self._res_id = res_id
        """
            资源code
        """
        self._res_code = res_code
        """
            发件人地址库id
        """
        self._from_id = from_id
        """
            运单号
        """
        self._waybill_no = waybill_no

    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        if isinstance(trade_id, int):
            self._trade_id = trade_id
        else:
            raise TypeError("trade_id must be int")

    @property
    def res_id(self):
        return self._res_id

    @res_id.setter
    def res_id(self, res_id):
        if isinstance(res_id, int):
            self._res_id = res_id
        else:
            raise TypeError("res_id must be int")

    @property
    def res_code(self):
        return self._res_code

    @res_code.setter
    def res_code(self, res_code):
        if isinstance(res_code, str):
            self._res_code = res_code
        else:
            raise TypeError("res_code must be str")

    @property
    def from_id(self):
        return self._from_id

    @from_id.setter
    def from_id(self, from_id):
        if isinstance(from_id, int):
            self._from_id = from_id
        else:
            raise TypeError("from_id must be int")

    @property
    def waybill_no(self):
        return self._waybill_no

    @waybill_no.setter
    def waybill_no(self, waybill_no):
        if isinstance(waybill_no, str):
            self._waybill_no = waybill_no
        else:
            raise TypeError("waybill_no must be str")


    def get_api_name(self):
        return "taobao.wlb.import.threepl.offline.consign"

    def to_dict(self):
        request_dict = {}
        if self._trade_id is not None:
            request_dict["trade_id"] = convert_basic(self._trade_id)

        if self._res_id is not None:
            request_dict["res_id"] = convert_basic(self._res_id)

        if self._res_code is not None:
            request_dict["res_code"] = convert_basic(self._res_code)

        if self._from_id is not None:
            request_dict["from_id"] = convert_basic(self._from_id)

        if self._waybill_no is not None:
            request_dict["waybill_no"] = convert_basic(self._waybill_no)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


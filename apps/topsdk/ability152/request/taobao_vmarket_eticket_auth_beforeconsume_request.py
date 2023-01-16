from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketAuthBeforeconsumeRequest(BaseRequest):

    def __init__(
        self,
        verify_code: str = None,
        operatorid: str = None,
        storeid: str = None
    ):
        """
            核销的码，只支持单个码，多个码核销需要多次调用
        """
        self._verify_code = verify_code
        """
            核销方的ID，如果是普通码商必须传入机具ID,如果是私有码商家（即原有的信任商家）可默认传入私有码商ID
        """
        self._operatorid = operatorid
        """
            网点ID,网点授权核销时，必须传入；其他核销方式可不传
        """
        self._storeid = storeid

    @property
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        if isinstance(verify_code, str):
            self._verify_code = verify_code
        else:
            raise TypeError("verify_code must be str")

    @property
    def operatorid(self):
        return self._operatorid

    @operatorid.setter
    def operatorid(self, operatorid):
        if isinstance(operatorid, str):
            self._operatorid = operatorid
        else:
            raise TypeError("operatorid must be str")

    @property
    def storeid(self):
        return self._storeid

    @storeid.setter
    def storeid(self, storeid):
        if isinstance(storeid, str):
            self._storeid = storeid
        else:
            raise TypeError("storeid must be str")


    def get_api_name(self):
        return "taobao.vmarket.eticket.auth.beforeconsume"

    def to_dict(self):
        request_dict = {}
        if self._verify_code is not None:
            request_dict["verify_code"] = convert_basic(self._verify_code)

        if self._operatorid is not None:
            request_dict["operatorid"] = convert_basic(self._operatorid)

        if self._storeid is not None:
            request_dict["storeid"] = convert_basic(self._storeid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


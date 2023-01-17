from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsInstantTraceSearchRequest(BaseRequest):

    def __init__(
        self,
        mail_no: str = None,
        is_split: int = None,
        sub_tid: str = None,
        tid: int = None
    ):
        """
            运单号
        """
        self._mail_no = mail_no
        """
            是否拆单
        """
        self._is_split = is_split
        """
            子订单列表
        """
        self._sub_tid = sub_tid
        """
            交易单号
        """
        self._tid = tid

    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, mail_no):
        if isinstance(mail_no, str):
            self._mail_no = mail_no
        else:
            raise TypeError("mail_no must be str")

    @property
    def is_split(self):
        return self._is_split

    @is_split.setter
    def is_split(self, is_split):
        if isinstance(is_split, int):
            self._is_split = is_split
        else:
            raise TypeError("is_split must be int")

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
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, int):
            self._tid = tid
        else:
            raise TypeError("tid must be int")


    def get_api_name(self):
        return "taobao.logistics.instant.trace.search"

    def to_dict(self):
        request_dict = {}
        if self._mail_no is not None:
            request_dict["mail_no"] = convert_basic(self._mail_no)

        if self._is_split is not None:
            request_dict["is_split"] = convert_basic(self._is_split)

        if self._sub_tid is not None:
            request_dict["sub_tid"] = convert_basic(self._sub_tid)

        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


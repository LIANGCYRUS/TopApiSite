from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketOplogsGetRequest(BaseRequest):

    def __init__(
        self,
        type: int = None,
        start_time: datetime = None,
        end_time: datetime = None,
        code: str = None,
        mobile: str = None,
        posid: str = None,
        codemerchant_id: int = None,
        page_no: int = None,
        page_size: int = None,
        sort: str = None
    ):
        """
            0:全部 1:核销 2:冲正
        """
        self._type = type
        """
            开始时间
        """
        self._start_time = start_time
        """
            结束时间
        """
        self._end_time = end_time
        """
            核销码
        """
        self._code = code
        """
            手机号后四位
        """
        self._mobile = mobile
        """
            核销身份
        """
        self._posid = posid
        """
            码商ID
        """
        self._codemerchant_id = codemerchant_id
        """
            当前页码
        """
        self._page_no = page_no
        """
            每页显示的记录数，最大为40，默认为40
        """
        self._page_size = page_size
        """
            排序方式
        """
        self._sort = sort

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if isinstance(start_time, datetime):
            self._start_time = start_time
        else:
            raise TypeError("start_time must be datetime")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        if isinstance(end_time, datetime):
            self._end_time = end_time
        else:
            raise TypeError("end_time must be datetime")

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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        if isinstance(mobile, str):
            self._mobile = mobile
        else:
            raise TypeError("mobile must be str")

    @property
    def posid(self):
        return self._posid

    @posid.setter
    def posid(self, posid):
        if isinstance(posid, str):
            self._posid = posid
        else:
            raise TypeError("posid must be str")

    @property
    def codemerchant_id(self):
        return self._codemerchant_id

    @codemerchant_id.setter
    def codemerchant_id(self, codemerchant_id):
        if isinstance(codemerchant_id, int):
            self._codemerchant_id = codemerchant_id
        else:
            raise TypeError("codemerchant_id must be int")

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, sort):
        if isinstance(sort, str):
            self._sort = sort
        else:
            raise TypeError("sort must be str")


    def get_api_name(self):
        return "taobao.vmarket.eticket.oplogs.get"

    def to_dict(self):
        request_dict = {}
        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._start_time is not None:
            request_dict["start_time"] = convert_basic(self._start_time)

        if self._end_time is not None:
            request_dict["end_time"] = convert_basic(self._end_time)

        if self._code is not None:
            request_dict["code"] = convert_basic(self._code)

        if self._mobile is not None:
            request_dict["mobile"] = convert_basic(self._mobile)

        if self._posid is not None:
            request_dict["posid"] = convert_basic(self._posid)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._sort is not None:
            request_dict["sort"] = convert_basic(self._sort)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


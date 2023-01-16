from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPromotionCouponsGetRequest(BaseRequest):

    def __init__(
        self,
        coupon_id: int = None,
        end_time: datetime = None,
        denominations: int = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            优惠券的id，唯一标识这个优惠券
        """
        self._coupon_id = coupon_id
        """
            优惠券的截止日期
        """
        self._end_time = end_time
        """
            优惠券的面额，必须是3，5，10，20，50,100
        """
        self._denominations = denominations
        """
            查询的页号，结果集是分页返回的，每页20条
        """
        self._page_no = page_no
        """
            每页条数
        """
        self._page_size = page_size

    @property
    def coupon_id(self):
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        if isinstance(coupon_id, int):
            self._coupon_id = coupon_id
        else:
            raise TypeError("coupon_id must be int")

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
    def denominations(self):
        return self._denominations

    @denominations.setter
    def denominations(self, denominations):
        if isinstance(denominations, int):
            self._denominations = denominations
        else:
            raise TypeError("denominations must be int")

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


    def get_api_name(self):
        return "taobao.promotion.coupons.get"

    def to_dict(self):
        request_dict = {}
        if self._coupon_id is not None:
            request_dict["coupon_id"] = convert_basic(self._coupon_id)

        if self._end_time is not None:
            request_dict["end_time"] = convert_basic(self._end_time)

        if self._denominations is not None:
            request_dict["denominations"] = convert_basic(self._denominations)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPromotionMealGetRequest(BaseRequest):

    def __init__(
        self,
        meal_id: int = None,
        status: str = None
    ):
        """
            搭配套餐id
        """
        self._meal_id = meal_id
        """
            套餐状态。有效：VALID;失效：INVALID(有效套餐为可使用的套餐,无效套餐为套餐中有商品下架或库存为0时)。默认时两种情况都会查询。
        """
        self._status = status

    @property
    def meal_id(self):
        return self._meal_id

    @meal_id.setter
    def meal_id(self, meal_id):
        if isinstance(meal_id, int):
            self._meal_id = meal_id
        else:
            raise TypeError("meal_id must be int")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")


    def get_api_name(self):
        return "taobao.promotion.meal.get"

    def to_dict(self):
        request_dict = {}
        if self._meal_id is not None:
            request_dict["meal_id"] = convert_basic(self._meal_id)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


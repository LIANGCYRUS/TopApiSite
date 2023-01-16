from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPromotionLimitdiscountDetailGetRequest(BaseRequest):

    def __init__(
        self,
        limit_discount_id: int = None
    ):
        """
            限时打折ID。这个针对查询唯一限时打折情况。
        """
        self._limit_discount_id = limit_discount_id

    @property
    def limit_discount_id(self):
        return self._limit_discount_id

    @limit_discount_id.setter
    def limit_discount_id(self, limit_discount_id):
        if isinstance(limit_discount_id, int):
            self._limit_discount_id = limit_discount_id
        else:
            raise TypeError("limit_discount_id must be int")


    def get_api_name(self):
        return "taobao.promotion.limitdiscount.detail.get"

    def to_dict(self):
        request_dict = {}
        if self._limit_discount_id is not None:
            request_dict["limit_discount_id"] = convert_basic(self._limit_discount_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


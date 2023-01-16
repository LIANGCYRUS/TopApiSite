from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPromotionActivityGetRequest(BaseRequest):

    def __init__(
        self,
        activity_id: int = None
    ):
        """
            活动的id
        """
        self._activity_id = activity_id

    @property
    def activity_id(self):
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        if isinstance(activity_id, int):
            self._activity_id = activity_id
        else:
            raise TypeError("activity_id must be int")


    def get_api_name(self):
        return "taobao.promotion.activity.get"

    def to_dict(self):
        request_dict = {}
        if self._activity_id is not None:
            request_dict["activity_id"] = convert_basic(self._activity_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


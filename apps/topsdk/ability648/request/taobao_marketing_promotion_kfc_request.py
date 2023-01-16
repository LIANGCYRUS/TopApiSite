from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoMarketingPromotionKfcRequest(BaseRequest):

    def __init__(
        self,
        promotion_title: str = None,
        promotion_desc: str = None
    ):
        """
            活动名称
        """
        self._promotion_title = promotion_title
        """
            活动描述
        """
        self._promotion_desc = promotion_desc

    @property
    def promotion_title(self):
        return self._promotion_title

    @promotion_title.setter
    def promotion_title(self, promotion_title):
        if isinstance(promotion_title, str):
            self._promotion_title = promotion_title
        else:
            raise TypeError("promotion_title must be str")

    @property
    def promotion_desc(self):
        return self._promotion_desc

    @promotion_desc.setter
    def promotion_desc(self, promotion_desc):
        if isinstance(promotion_desc, str):
            self._promotion_desc = promotion_desc
        else:
            raise TypeError("promotion_desc must be str")


    def get_api_name(self):
        return "taobao.marketing.promotion.kfc"

    def to_dict(self):
        request_dict = {}
        if self._promotion_title is not None:
            request_dict["promotion_title"] = convert_basic(self._promotion_title)

        if self._promotion_desc is not None:
            request_dict["promotion_desc"] = convert_basic(self._promotion_desc)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


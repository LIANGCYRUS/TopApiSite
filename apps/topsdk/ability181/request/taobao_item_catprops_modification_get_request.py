from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemCatpropsModificationGetRequest(BaseRequest):

    def __init__(
        self,
        category_id: int = None,
        item_id: str = None,
        start_time: str = None
    ):
        """
            类目Id（与商品Id二选一即可）
        """
        self._category_id = category_id
        """
            商品Id（与类目Id二选一即可。若同时传入商品Id和类目Id，则优先使用商品Id。若填写商品Id，则起始时间设为该商品最近修改时间）
        """
        self._item_id = item_id
        """
            起始请求时间（建议传入，默认为90天内）
        """
        self._start_time = start_time

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        if isinstance(category_id, int):
            self._category_id = category_id
        else:
            raise TypeError("category_id must be int")

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, str):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be str")

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if isinstance(start_time, str):
            self._start_time = start_time
        else:
            raise TypeError("start_time must be str")


    def get_api_name(self):
        return "taobao.item.catprops.modification.get"

    def to_dict(self):
        request_dict = {}
        if self._category_id is not None:
            request_dict["category_id"] = convert_basic(self._category_id)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._start_time is not None:
            request_dict["start_time"] = convert_basic(self._start_time)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


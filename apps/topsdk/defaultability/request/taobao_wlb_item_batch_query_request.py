from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbItemBatchQueryRequest(BaseRequest):

    def __init__(
        self,
        item_ids: str = None,
        store_code: str = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            需要查询的商品ID列表，以字符串表示，ID间以;隔开
        """
        self._item_ids = item_ids
        """
            仓库编号
        """
        self._store_code = store_code
        """
            分页查询参数，指定查询页数，默认为1
        """
        self._page_no = page_no
        """
            分页查询参数，每页查询数量，默认20，最大值50,大于50时按照50条查询
        """
        self._page_size = page_size

    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        if isinstance(item_ids, str):
            self._item_ids = item_ids
        else:
            raise TypeError("item_ids must be str")

    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, store_code):
        if isinstance(store_code, str):
            self._store_code = store_code
        else:
            raise TypeError("store_code must be str")

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
        return "taobao.wlb.item.batch.query"

    def to_dict(self):
        request_dict = {}
        if self._item_ids is not None:
            request_dict["item_ids"] = convert_basic(self._item_ids)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


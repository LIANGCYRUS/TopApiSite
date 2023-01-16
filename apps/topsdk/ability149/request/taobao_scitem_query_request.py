from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoScitemQueryRequest(BaseRequest):

    def __init__(
        self,
        item_name: str = None,
        outer_code: str = None,
        wms_code: str = None,
        bar_code: str = None,
        item_type: int = None,
        page_index: int = None,
        page_size: int = None
    ):
        """
            商品名称
        """
        self._item_name = item_name
        """
            商家给商品的一个编码
        """
        self._outer_code = outer_code
        """
            仓库编码
        """
        self._wms_code = wms_code
        """
            条形码
        """
        self._bar_code = bar_code
        """
            ITEM类型(只允许输入以下英文或空) NORMAL 0:普通商品; COMBINE 1:是否是组合商品 DISTRIBUTION
        """
        self._item_type = item_type
        """
            当前页码数
        """
        self._page_index = page_index
        """
            分页记录个数，如果用户输入的记录数大于50，则一页显示50条记录
        """
        self._page_size = page_size

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        if isinstance(item_name, str):
            self._item_name = item_name
        else:
            raise TypeError("item_name must be str")

    @property
    def outer_code(self):
        return self._outer_code

    @outer_code.setter
    def outer_code(self, outer_code):
        if isinstance(outer_code, str):
            self._outer_code = outer_code
        else:
            raise TypeError("outer_code must be str")

    @property
    def wms_code(self):
        return self._wms_code

    @wms_code.setter
    def wms_code(self, wms_code):
        if isinstance(wms_code, str):
            self._wms_code = wms_code
        else:
            raise TypeError("wms_code must be str")

    @property
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, bar_code):
        if isinstance(bar_code, str):
            self._bar_code = bar_code
        else:
            raise TypeError("bar_code must be str")

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        if isinstance(item_type, int):
            self._item_type = item_type
        else:
            raise TypeError("item_type must be int")

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        if isinstance(page_index, int):
            self._page_index = page_index
        else:
            raise TypeError("page_index must be int")

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
        return "taobao.scitem.query"

    def to_dict(self):
        request_dict = {}
        if self._item_name is not None:
            request_dict["item_name"] = convert_basic(self._item_name)

        if self._outer_code is not None:
            request_dict["outer_code"] = convert_basic(self._outer_code)

        if self._wms_code is not None:
            request_dict["wms_code"] = convert_basic(self._wms_code)

        if self._bar_code is not None:
            request_dict["bar_code"] = convert_basic(self._bar_code)

        if self._item_type is not None:
            request_dict["item_type"] = convert_basic(self._item_type)

        if self._page_index is not None:
            request_dict["page_index"] = convert_basic(self._page_index)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


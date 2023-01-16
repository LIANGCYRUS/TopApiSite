from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbItemQueryRequest(BaseRequest):

    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        name: str = None,
        title: str = None,
        item_code: str = None,
        is_sku: str = None,
        parent_id: int = None,
        status: str = None,
        item_type: str = None
    ):
        """
            当前页
        """
        self._page_no = page_no
        """
            分页记录个数，如果用户输入的记录数大于50，则一页显示50条记录
        """
        self._page_size = page_size
        """
            商品名称
        """
        self._name = name
        """
            商品前台销售名字
        """
        self._title = title
        """
            商家编码
        """
        self._item_code = item_code
        """
            是否是最小库存单元，只有最小库存单元的商品才可以有库存,值只能给"true","false"来表示;  若值不在范围内，则按true处理
        """
        self._is_sku = is_sku
        """
            父ID,只有is_sku=1时才能有父ID，商品也可以没有付商品
        """
        self._parent_id = parent_id
        """
            只能输入以下值或空：  ITEM_STATUS_VALID -- 1 表示 有效；  ITEM_STATUS_LOCK -- 2 表示锁住。  若值不在范围内，按ITEM_STATUS_VALID处理
        """
        self._status = status
        """
            ITEM类型(只允许输入以下英文或空)  NORMAL 0:普通商品;  COMBINE 1:是否是组合商品  DISTRIBUTION 2:是否是分销商品(货主是别人)  若值不在范围内，则按NORMAL处理
        """
        self._item_type = item_type

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise TypeError("title must be str")

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        if isinstance(item_code, str):
            self._item_code = item_code
        else:
            raise TypeError("item_code must be str")

    @property
    def is_sku(self):
        return self._is_sku

    @is_sku.setter
    def is_sku(self, is_sku):
        if isinstance(is_sku, str):
            self._is_sku = is_sku
        else:
            raise TypeError("is_sku must be str")

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        if isinstance(parent_id, int):
            self._parent_id = parent_id
        else:
            raise TypeError("parent_id must be int")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        if isinstance(item_type, str):
            self._item_type = item_type
        else:
            raise TypeError("item_type must be str")


    def get_api_name(self):
        return "taobao.wlb.item.query"

    def to_dict(self):
        request_dict = {}
        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._title is not None:
            request_dict["title"] = convert_basic(self._title)

        if self._item_code is not None:
            request_dict["item_code"] = convert_basic(self._item_code)

        if self._is_sku is not None:
            request_dict["is_sku"] = convert_basic(self._is_sku)

        if self._parent_id is not None:
            request_dict["parent_id"] = convert_basic(self._parent_id)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._item_type is not None:
            request_dict["item_type"] = convert_basic(self._item_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


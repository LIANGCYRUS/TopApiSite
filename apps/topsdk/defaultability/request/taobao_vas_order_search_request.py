from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVasOrderSearchRequest(BaseRequest):

    def __init__(
        self,
        nick: str = None,
        article_code: str = None,
        item_code: str = None,
        start_created: datetime = None,
        end_created: datetime = None,
        biz_order_id: int = None,
        order_id: int = None,
        biz_type: int = None,
        page_size: int = None,
        page_no: int = None
    ):
        """
            淘宝会员名
        """
        self._nick = nick
        """
            应用收费代码，从合作伙伴后台（my.open.taobao.com）-收费管理-收费项目列表 能够获得该应用的收费代码
        """
        self._article_code = article_code
        """
            收费项目代码，从合作伙伴后台（my.open.taobao.com）-收费管理-收费项目列表 能够获得收费项目代码
        """
        self._item_code = item_code
        """
            订单创建时间（订购时间）起始值（当start_created和end_created都不填写时，默认返回最近90天的数据）
        """
        self._start_created = start_created
        """
            订单创建时间（订购时间）结束值
        """
        self._end_created = end_created
        """
            订单号
        """
        self._biz_order_id = biz_order_id
        """
            子订单号
        """
        self._order_id = order_id
        """
            订单类型，1=新订 2=续订 3=升级 4=后台赠送 5=后台自动续订 6=订单审核后生成订购关系（暂时用不到） 空=全部
        """
        self._biz_type = biz_type
        """
            一页包含的记录数
        """
        self._page_size = page_size
        """
            页码
        """
        self._page_no = page_no

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, nick):
        if isinstance(nick, str):
            self._nick = nick
        else:
            raise TypeError("nick must be str")

    @property
    def article_code(self):
        return self._article_code

    @article_code.setter
    def article_code(self, article_code):
        if isinstance(article_code, str):
            self._article_code = article_code
        else:
            raise TypeError("article_code must be str")

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
    def start_created(self):
        return self._start_created

    @start_created.setter
    def start_created(self, start_created):
        if isinstance(start_created, datetime):
            self._start_created = start_created
        else:
            raise TypeError("start_created must be datetime")

    @property
    def end_created(self):
        return self._end_created

    @end_created.setter
    def end_created(self, end_created):
        if isinstance(end_created, datetime):
            self._end_created = end_created
        else:
            raise TypeError("end_created must be datetime")

    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, biz_order_id):
        if isinstance(biz_order_id, int):
            self._biz_order_id = biz_order_id
        else:
            raise TypeError("biz_order_id must be int")

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        if isinstance(order_id, int):
            self._order_id = order_id
        else:
            raise TypeError("order_id must be int")

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, int):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be int")

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")


    def get_api_name(self):
        return "taobao.vas.order.search"

    def to_dict(self):
        request_dict = {}
        if self._nick is not None:
            request_dict["nick"] = convert_basic(self._nick)

        if self._article_code is not None:
            request_dict["article_code"] = convert_basic(self._article_code)

        if self._item_code is not None:
            request_dict["item_code"] = convert_basic(self._item_code)

        if self._start_created is not None:
            request_dict["start_created"] = convert_basic(self._start_created)

        if self._end_created is not None:
            request_dict["end_created"] = convert_basic(self._end_created)

        if self._biz_order_id is not None:
            request_dict["biz_order_id"] = convert_basic(self._biz_order_id)

        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


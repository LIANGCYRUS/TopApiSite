from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbInventorylogQueryRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        store_code: str = None,
        order_code: str = None,
        gmt_start: datetime = None,
        gmt_end: datetime = None,
        page_no: int = None,
        page_size: int = None,
        op_user_id: int = None,
        op_type: str = None
    ):
        """
            商品ID
        """
        self._item_id = item_id
        """
            仓库编码
        """
        self._store_code = store_code
        """
            单号
        """
        self._order_code = order_code
        """
            起始修改时间,大于等于该时间
        """
        self._gmt_start = gmt_start
        """
            结束修改时间,小于等于该时间
        """
        self._gmt_end = gmt_end
        """
            当前页
        """
        self._page_no = page_no
        """
            分页记录个数
        """
        self._page_size = page_size
        """
            可指定授权的用户来查询
        """
        self._op_user_id = op_user_id
        """
            库存操作作类型(可以为空) CHU_KU 1-出库 RU_KU 2-入库 FREEZE 3-冻结 THAW 4-解冻 CHECK_FREEZE 5-冻结确认 CHANGE_KU 6-库存类型变更 若值不在范围内，则按CHU_KU处理
        """
        self._op_type = op_type

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, int):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be int")

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
    def order_code(self):
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        if isinstance(order_code, str):
            self._order_code = order_code
        else:
            raise TypeError("order_code must be str")

    @property
    def gmt_start(self):
        return self._gmt_start

    @gmt_start.setter
    def gmt_start(self, gmt_start):
        if isinstance(gmt_start, datetime):
            self._gmt_start = gmt_start
        else:
            raise TypeError("gmt_start must be datetime")

    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, gmt_end):
        if isinstance(gmt_end, datetime):
            self._gmt_end = gmt_end
        else:
            raise TypeError("gmt_end must be datetime")

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
    def op_user_id(self):
        return self._op_user_id

    @op_user_id.setter
    def op_user_id(self, op_user_id):
        if isinstance(op_user_id, int):
            self._op_user_id = op_user_id
        else:
            raise TypeError("op_user_id must be int")

    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        if isinstance(op_type, str):
            self._op_type = op_type
        else:
            raise TypeError("op_type must be str")


    def get_api_name(self):
        return "taobao.wlb.inventorylog.query"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._order_code is not None:
            request_dict["order_code"] = convert_basic(self._order_code)

        if self._gmt_start is not None:
            request_dict["gmt_start"] = convert_basic(self._gmt_start)

        if self._gmt_end is not None:
            request_dict["gmt_end"] = convert_basic(self._gmt_end)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._op_user_id is not None:
            request_dict["op_user_id"] = convert_basic(self._op_user_id)

        if self._op_type is not None:
            request_dict["op_type"] = convert_basic(self._op_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


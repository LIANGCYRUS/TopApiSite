from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsInventoryQueryRequest(BaseRequest):

    def __init__(
        self,
        page_size: int = None,
        page_no: int = None,
        channel_code: str = None,
        due_date: datetime = None,
        produce_date: datetime = None,
        batch_code: str = None,
        type: int = None,
        inventory_type: int = None,
        store_code: str = None,
        item_id: str = None
    ):
        """
            每页多少条，最大50条
        """
        self._page_size = page_size
        """
            分页的第几页
        """
        self._page_no = page_no
        """
            渠道编码，type=3时字段传值有效。（TB 淘系， OTHERS 其他）
        """
        self._channel_code = channel_code
        """
            失效日期，type=2时字段传值有效。
        """
        self._due_date = due_date
        """
            生产日期，type=2时字段传值有效。
        """
        self._produce_date = produce_date
        """
            库存批次号，type=2时字段传值有效。 商品设置为批次管理时，商品产生批次库存。当商品为批次管理时，此字段不传值，返回所有批次库存信息。
        """
        self._batch_code = batch_code
        """
            库存查询类型 1-	汇总库存，不区分批次和渠道 2-	批次库存，库存按商品批次维度划分 3-	渠道库存，库存按渠道维度划分 （当前业务不支持批次库存和渠道库存共存，批次库存无渠道属性，渠道库存无批次属性）
        """
        self._type = type
        """
            库存类型。 (1 正品 101 残次 102 机损 103 箱损 201 冻结库存 301 在途库存 )
        """
        self._inventory_type = inventory_type
        """
            仓库编码
        """
        self._store_code = store_code
        """
            菜鸟商品ID
        """
        self._item_id = item_id

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

    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, channel_code):
        if isinstance(channel_code, str):
            self._channel_code = channel_code
        else:
            raise TypeError("channel_code must be str")

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        if isinstance(due_date, datetime):
            self._due_date = due_date
        else:
            raise TypeError("due_date must be datetime")

    @property
    def produce_date(self):
        return self._produce_date

    @produce_date.setter
    def produce_date(self, produce_date):
        if isinstance(produce_date, datetime):
            self._produce_date = produce_date
        else:
            raise TypeError("produce_date must be datetime")

    @property
    def batch_code(self):
        return self._batch_code

    @batch_code.setter
    def batch_code(self, batch_code):
        if isinstance(batch_code, str):
            self._batch_code = batch_code
        else:
            raise TypeError("batch_code must be str")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")

    @property
    def inventory_type(self):
        return self._inventory_type

    @inventory_type.setter
    def inventory_type(self, inventory_type):
        if isinstance(inventory_type, int):
            self._inventory_type = inventory_type
        else:
            raise TypeError("inventory_type must be int")

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
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, str):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be str")


    def get_api_name(self):
        return "taobao.wlb.wms.inventory.query"

    def to_dict(self):
        request_dict = {}
        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._channel_code is not None:
            request_dict["channel_code"] = convert_basic(self._channel_code)

        if self._due_date is not None:
            request_dict["due_date"] = convert_basic(self._due_date)

        if self._produce_date is not None:
            request_dict["produce_date"] = convert_basic(self._produce_date)

        if self._batch_code is not None:
            request_dict["batch_code"] = convert_basic(self._batch_code)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._inventory_type is not None:
            request_dict["inventory_type"] = convert_basic(self._inventory_type)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


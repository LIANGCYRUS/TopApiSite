from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDistributorProductsGetRequest(BaseRequest):

    def __init__(
        self,
        pids: list = None,
        item_ids: list = None,
        supplier_nick: str = None,
        trade_type: str = None,
        download_status: str = None,
        productcat_id: int = None,
        fields: list = None,
        start_time: datetime = None,
        end_time: datetime = None,
        time_type: str = None,
        page_no: int = None,
        page_size: int = None,
        order_by: str = None
    ):
        """
            产品ID列表（最大限制30），用逗号分割，例如：“1001,1002,1003,1004,1005”
        """
        self._pids = pids
        """
            根据商品ID列表查询，优先级次于产品ID列表，高于其他分页查询条件。如果商品不是分销商品，自动过滤。最大限制20，用逗号分割，例如：“1001,1002,1003,1004,1005”
        """
        self._item_ids = item_ids
        """
            供应商nick，分页查询时，必传
        """
        self._supplier_nick = supplier_nick
        """
            分销方式；可选择：AGENT ： 代销；DEALER：经销；DIRECT：直营
        """
        self._trade_type = trade_type
        """
            下载状态，默认是未下载；可选值：UNDOWNLOAD：未下载 ；DOWNLOADED：已下载；下载：指将供应商授权的产品发布为店铺新宝贝的过程，下载成功后，分销商需要将新生成的宝贝重新编辑并上架后售卖。
        """
        self._download_status = download_status
        """
            产品线ID
        """
        self._productcat_id = productcat_id
        """
            指定查询额外的信息，可选值：skus（sku数据）、images（多图），多个可选值用逗号分割。
        """
        self._fields = fields
        """
            开始修改时间
        """
        self._start_time = start_time
        """
            结束时间
        """
        self._end_time = end_time
        """
            time_type
        """
        self._time_type = time_type
        """
            页码（大于0的整数，默认1）
        """
        self._page_no = page_no
        """
            每页记录数（默认20，最大50）
        """
        self._page_size = page_size
        """
            order_by
        """
        self._order_by = order_by

    @property
    def pids(self):
        return self._pids

    @pids.setter
    def pids(self, pids):
        if isinstance(pids, list):
            self._pids = pids
        else:
            raise TypeError("pids must be list")

    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        if isinstance(item_ids, list):
            self._item_ids = item_ids
        else:
            raise TypeError("item_ids must be list")

    @property
    def supplier_nick(self):
        return self._supplier_nick

    @supplier_nick.setter
    def supplier_nick(self, supplier_nick):
        if isinstance(supplier_nick, str):
            self._supplier_nick = supplier_nick
        else:
            raise TypeError("supplier_nick must be str")

    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        if isinstance(trade_type, str):
            self._trade_type = trade_type
        else:
            raise TypeError("trade_type must be str")

    @property
    def download_status(self):
        return self._download_status

    @download_status.setter
    def download_status(self, download_status):
        if isinstance(download_status, str):
            self._download_status = download_status
        else:
            raise TypeError("download_status must be str")

    @property
    def productcat_id(self):
        return self._productcat_id

    @productcat_id.setter
    def productcat_id(self, productcat_id):
        if isinstance(productcat_id, int):
            self._productcat_id = productcat_id
        else:
            raise TypeError("productcat_id must be int")

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        if isinstance(start_time, datetime):
            self._start_time = start_time
        else:
            raise TypeError("start_time must be datetime")

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        if isinstance(end_time, datetime):
            self._end_time = end_time
        else:
            raise TypeError("end_time must be datetime")

    @property
    def time_type(self):
        return self._time_type

    @time_type.setter
    def time_type(self, time_type):
        if isinstance(time_type, str):
            self._time_type = time_type
        else:
            raise TypeError("time_type must be str")

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
    def order_by(self):
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        if isinstance(order_by, str):
            self._order_by = order_by
        else:
            raise TypeError("order_by must be str")


    def get_api_name(self):
        return "taobao.fenxiao.distributor.products.get"

    def to_dict(self):
        request_dict = {}
        if self._pids is not None:
            request_dict["pids"] = convert_basic_list(self._pids)

        if self._item_ids is not None:
            request_dict["item_ids"] = convert_basic_list(self._item_ids)

        if self._supplier_nick is not None:
            request_dict["supplier_nick"] = convert_basic(self._supplier_nick)

        if self._trade_type is not None:
            request_dict["trade_type"] = convert_basic(self._trade_type)

        if self._download_status is not None:
            request_dict["download_status"] = convert_basic(self._download_status)

        if self._productcat_id is not None:
            request_dict["productcat_id"] = convert_basic(self._productcat_id)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._start_time is not None:
            request_dict["start_time"] = convert_basic(self._start_time)

        if self._end_time is not None:
            request_dict["end_time"] = convert_basic(self._end_time)

        if self._time_type is not None:
            request_dict["time_type"] = convert_basic(self._time_type)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._order_by is not None:
            request_dict["order_by"] = convert_basic(self._order_by)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


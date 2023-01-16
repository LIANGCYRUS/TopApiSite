from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDistributorItemsGetRequest(BaseRequest):

    def __init__(
        self,
        distributor_id: int = None,
        product_id: int = None,
        start_modified: datetime = None,
        end_modified: datetime = None,
        page_size: int = None,
        page_no: int = None
    ):
        """
            分销商ID 。
        """
        self._distributor_id = distributor_id
        """
            产品ID
        """
        self._product_id = product_id
        """
            设置开始时间。空为不设置。
        """
        self._start_modified = start_modified
        """
            设置结束时间,空为不设置。
        """
        self._end_modified = end_modified
        """
            每页记录数（默认20，最大50）
        """
        self._page_size = page_size
        """
            页码（大于0的整数，默认1）
        """
        self._page_no = page_no

    @property
    def distributor_id(self):
        return self._distributor_id

    @distributor_id.setter
    def distributor_id(self, distributor_id):
        if isinstance(distributor_id, int):
            self._distributor_id = distributor_id
        else:
            raise TypeError("distributor_id must be int")

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self._product_id = product_id
        else:
            raise TypeError("product_id must be int")

    @property
    def start_modified(self):
        return self._start_modified

    @start_modified.setter
    def start_modified(self, start_modified):
        if isinstance(start_modified, datetime):
            self._start_modified = start_modified
        else:
            raise TypeError("start_modified must be datetime")

    @property
    def end_modified(self):
        return self._end_modified

    @end_modified.setter
    def end_modified(self, end_modified):
        if isinstance(end_modified, datetime):
            self._end_modified = end_modified
        else:
            raise TypeError("end_modified must be datetime")

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
        return "taobao.fenxiao.distributor.items.get"

    def to_dict(self):
        request_dict = {}
        if self._distributor_id is not None:
            request_dict["distributor_id"] = convert_basic(self._distributor_id)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._start_modified is not None:
            request_dict["start_modified"] = convert_basic(self._start_modified)

        if self._end_modified is not None:
            request_dict["end_modified"] = convert_basic(self._end_modified)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductsGetRequest(BaseRequest):

    def __init__(
        self,
        outer_id: str = None,
        productcat_id: int = None,
        pids: list = None,
        fields: list = None,
        start_modified: datetime = None,
        end_modified: datetime = None,
        page_no: int = None,
        page_size: int = None,
        sku_number: str = None,
        is_authz: str = None,
        item_ids: list = None
    ):
        """
            商家编码
        """
        self._outer_id = outer_id
        """
            产品线ID
        """
        self._productcat_id = productcat_id
        """
            产品ID列表（最大限制30），用逗号分割，例如：“1001,1002,1003,1004,1005”
        """
        self._pids = pids
        """
            指定查询额外的信息，可选值：skus（sku数据）、images（多图），多个可选值用逗号分割。
        """
        self._fields = fields
        """
            开始修改时间
        """
        self._start_modified = start_modified
        """
            结束修改时间
        """
        self._end_modified = end_modified
        """
            页码（大于0的整数，默认1）
        """
        self._page_no = page_no
        """
            每页记录数（默认20，最大50）
        """
        self._page_size = page_size
        """
            sku商家编码
        """
        self._sku_number = sku_number
        """
            查询产品列表时，查询入参“是否需要授权”
yes:需要授权 
no:不需要授权
        """
        self._is_authz = is_authz
        """
            可根据导入的商品ID列表查询，优先级次于产品ID、sku_numbers，高于其他分页查询条件。最大限制20，用逗号分割，例如：“1001,1002,1003,1004,1005”
        """
        self._item_ids = item_ids

    @property
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")

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
    def pids(self):
        return self._pids

    @pids.setter
    def pids(self, pids):
        if isinstance(pids, list):
            self._pids = pids
        else:
            raise TypeError("pids must be list")

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
    def sku_number(self):
        return self._sku_number

    @sku_number.setter
    def sku_number(self, sku_number):
        if isinstance(sku_number, str):
            self._sku_number = sku_number
        else:
            raise TypeError("sku_number must be str")

    @property
    def is_authz(self):
        return self._is_authz

    @is_authz.setter
    def is_authz(self, is_authz):
        if isinstance(is_authz, str):
            self._is_authz = is_authz
        else:
            raise TypeError("is_authz must be str")

    @property
    def item_ids(self):
        return self._item_ids

    @item_ids.setter
    def item_ids(self, item_ids):
        if isinstance(item_ids, list):
            self._item_ids = item_ids
        else:
            raise TypeError("item_ids must be list")


    def get_api_name(self):
        return "taobao.fenxiao.products.get"

    def to_dict(self):
        request_dict = {}
        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._productcat_id is not None:
            request_dict["productcat_id"] = convert_basic(self._productcat_id)

        if self._pids is not None:
            request_dict["pids"] = convert_basic_list(self._pids)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._start_modified is not None:
            request_dict["start_modified"] = convert_basic(self._start_modified)

        if self._end_modified is not None:
            request_dict["end_modified"] = convert_basic(self._end_modified)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._sku_number is not None:
            request_dict["sku_number"] = convert_basic(self._sku_number)

        if self._is_authz is not None:
            request_dict["is_authz"] = convert_basic(self._is_authz)

        if self._item_ids is not None:
            request_dict["item_ids"] = convert_basic_list(self._item_ids)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


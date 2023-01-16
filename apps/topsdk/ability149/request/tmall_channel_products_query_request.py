from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallChannelProductsQueryRequest(BaseRequest):

    def __init__(
        self,
        product_number: str = None,
        sku_number: str = None,
        product_ids: list = None,
        page_size: int = None,
        product_line_id: int = None,
        page_num: int = None
    ):
        """
            商家产品编码
        """
        self._product_number = product_number
        """
            商家SKU编码
        """
        self._sku_number = sku_number
        """
            产品Id
        """
        self._product_ids = product_ids
        """
            分页大小
        """
        self._page_size = page_size
        """
            产品线Id
        """
        self._product_line_id = product_line_id
        """
            页码数，从1开始
        """
        self._page_num = page_num

    @property
    def product_number(self):
        return self._product_number

    @product_number.setter
    def product_number(self, product_number):
        if isinstance(product_number, str):
            self._product_number = product_number
        else:
            raise TypeError("product_number must be str")

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
    def product_ids(self):
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        if isinstance(product_ids, list):
            self._product_ids = product_ids
        else:
            raise TypeError("product_ids must be list")

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
    def product_line_id(self):
        return self._product_line_id

    @product_line_id.setter
    def product_line_id(self, product_line_id):
        if isinstance(product_line_id, int):
            self._product_line_id = product_line_id
        else:
            raise TypeError("product_line_id must be int")

    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        if isinstance(page_num, int):
            self._page_num = page_num
        else:
            raise TypeError("page_num must be int")


    def get_api_name(self):
        return "tmall.channel.products.query"

    def to_dict(self):
        request_dict = {}
        if self._product_number is not None:
            request_dict["product_number"] = convert_basic(self._product_number)

        if self._sku_number is not None:
            request_dict["sku_number"] = convert_basic(self._sku_number)

        if self._product_ids is not None:
            request_dict["product_ids"] = convert_basic_list(self._product_ids)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._product_line_id is not None:
            request_dict["product_line_id"] = convert_basic(self._product_line_id)

        if self._page_num is not None:
            request_dict["page_num"] = convert_basic(self._page_num)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


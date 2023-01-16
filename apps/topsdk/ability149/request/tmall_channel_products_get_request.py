from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallChannelProductsGetRequest(BaseRequest):

    def __init__(
        self,
        top_query_product_d_o: object = None
    ):
        """
            top_query_product_d_o
        """
        self._top_query_product_d_o = top_query_product_d_o

    @property
    def top_query_product_d_o(self):
        return self._top_query_product_d_o

    @top_query_product_d_o.setter
    def top_query_product_d_o(self, top_query_product_d_o):
        if isinstance(top_query_product_d_o, object):
            self._top_query_product_d_o = top_query_product_d_o
        else:
            raise TypeError("top_query_product_d_o must be object")


    def get_api_name(self):
        return "tmall.channel.products.get"

    def to_dict(self):
        request_dict = {}
        if self._top_query_product_d_o is not None:
            request_dict["top_query_product_d_o"] = convert_struct(self._top_query_product_d_o)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TmallChannelProductsGetTopQueryProductDo:
    def __init__(
        self,
        ids: list = None,
        page_size: int = None,
        product_line_id: int = None,
        page_num: int = None,
        product_outer_id: str = None,
        item_ids: list = None,
        sku_outer_id: str = None,
        channel: int = None
    ):
        """
            要查询的产品id 列表
        """
        self.ids = ids
        """
            分页大小
        """
        self.page_size = page_size
        """
            产品线id
        """
        self.product_line_id = product_line_id
        """
            当前要查看的页数
        """
        self.page_num = page_num
        """
            产品商家编码
        """
        self.product_outer_id = product_outer_id
        """
            关联的前端宝贝id列表
        """
        self.item_ids = item_ids
        """
            sku商家编码
        """
        self.sku_outer_id = sku_outer_id
        """
            渠道[21 零售plus]
        """
        self.channel = channel


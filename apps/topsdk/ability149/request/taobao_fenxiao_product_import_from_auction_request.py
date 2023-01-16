from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductImportFromAuctionRequest(BaseRequest):

    def __init__(
        self,
        trade_type: int = None,
        auction_id: int = None,
        product_line_id: int = None
    ):
        """
            导入产品需要支持的交易类型：[1 代销][ 2 经销 ][3 代销和经销]
        """
        self._trade_type = trade_type
        """
            店铺宝贝id
        """
        self._auction_id = auction_id
        """
            产品线id
        """
        self._product_line_id = product_line_id

    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        if isinstance(trade_type, int):
            self._trade_type = trade_type
        else:
            raise TypeError("trade_type must be int")

    @property
    def auction_id(self):
        return self._auction_id

    @auction_id.setter
    def auction_id(self, auction_id):
        if isinstance(auction_id, int):
            self._auction_id = auction_id
        else:
            raise TypeError("auction_id must be int")

    @property
    def product_line_id(self):
        return self._product_line_id

    @product_line_id.setter
    def product_line_id(self, product_line_id):
        if isinstance(product_line_id, int):
            self._product_line_id = product_line_id
        else:
            raise TypeError("product_line_id must be int")


    def get_api_name(self):
        return "taobao.fenxiao.product.import.from.auction"

    def to_dict(self):
        request_dict = {}
        if self._trade_type is not None:
            request_dict["trade_type"] = convert_basic(self._trade_type)

        if self._auction_id is not None:
            request_dict["auction_id"] = convert_basic(self._auction_id)

        if self._product_line_id is not None:
            request_dict["product_line_id"] = convert_basic(self._product_line_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


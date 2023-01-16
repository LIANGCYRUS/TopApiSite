from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDistributorProductQuantityGetRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        sku_id: int = None
    ):
        """
            产品ID
        """
        self._product_id = product_id
        """
            SKU ID
        """
        self._sku_id = sku_id

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
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, sku_id):
        if isinstance(sku_id, int):
            self._sku_id = sku_id
        else:
            raise TypeError("sku_id must be int")


    def get_api_name(self):
        return "taobao.fenxiao.distributor.product.quantity.get"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


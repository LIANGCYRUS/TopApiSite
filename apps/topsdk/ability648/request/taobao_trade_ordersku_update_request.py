from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradeOrderskuUpdateRequest(BaseRequest):

    def __init__(
        self,
        oid: int = None,
        sku_id: int = None,
        sku_props: str = None
    ):
        """
            子订单编号（对于单笔订单的交易可以传交易编号）。
        """
        self._oid = oid
        """
            销售属性编号，可以通过taobao.item.skus.get获取订单对应的商品的所有销售属性。
        """
        self._sku_id = sku_id
        """
            销售属性组合串，格式：p1:v1;p2:v2，如：1627207:28329;20509:28314。可以通过taobao.item.skus.get获取订单对应的商品的所有销售属性。
        """
        self._sku_props = sku_props

    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, oid):
        if isinstance(oid, int):
            self._oid = oid
        else:
            raise TypeError("oid must be int")

    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, sku_id):
        if isinstance(sku_id, int):
            self._sku_id = sku_id
        else:
            raise TypeError("sku_id must be int")

    @property
    def sku_props(self):
        return self._sku_props

    @sku_props.setter
    def sku_props(self, sku_props):
        if isinstance(sku_props, str):
            self._sku_props = sku_props
        else:
            raise TypeError("sku_props must be str")


    def get_api_name(self):
        return "taobao.trade.ordersku.update"

    def to_dict(self):
        request_dict = {}
        if self._oid is not None:
            request_dict["oid"] = convert_basic(self._oid)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        if self._sku_props is not None:
            request_dict["sku_props"] = convert_basic(self._sku_props)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


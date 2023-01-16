from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductGradepriceUpdateRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        sku_id: int = None,
        trade_type: str = None,
        target_type: str = None,
        ids: list = None,
        prices: list = None
    ):
        """
            产品Id
        """
        self._product_id = product_id
        """
            skuId，如果产品有skuId,必须要输入skuId;没有skuId的时候不必选
        """
        self._sku_id = sku_id
        """
            交易类型： AGENT(代销)、DEALER(经销)，ALL(代销和经销)
        """
        self._trade_type = trade_type
        """
            选择折扣方式：GRADE（按等级进行设置）;DISCITUTOR(按分销商进行设置）。例如"GRADE,DISTRIBUTOR"
        """
        self._target_type = target_type
        """
            会员等级的id或者分销商id，例如：”1001,2001,1002”
        """
        self._ids = ids
        """
            优惠价格,大小为0到100000000之间的整数或两位小数，例：优惠价格为：100元2角5分，传入的参数应写成：100.25
        """
        self._prices = prices

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
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        if isinstance(target_type, str):
            self._target_type = target_type
        else:
            raise TypeError("target_type must be str")

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, ids):
        if isinstance(ids, list):
            self._ids = ids
        else:
            raise TypeError("ids must be list")

    @property
    def prices(self):
        return self._prices

    @prices.setter
    def prices(self, prices):
        if isinstance(prices, list):
            self._prices = prices
        else:
            raise TypeError("prices must be list")


    def get_api_name(self):
        return "taobao.fenxiao.product.gradeprice.update"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        if self._trade_type is not None:
            request_dict["trade_type"] = convert_basic(self._trade_type)

        if self._target_type is not None:
            request_dict["target_type"] = convert_basic(self._target_type)

        if self._ids is not None:
            request_dict["ids"] = convert_basic_list(self._ids)

        if self._prices is not None:
            request_dict["prices"] = convert_basic_list(self._prices)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


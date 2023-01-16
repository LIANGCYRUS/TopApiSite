from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductSkuAddRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        standard_price: str = None,
        agent_cost_price: str = None,
        dealer_cost_price: str = None,
        quantity: int = None,
        sku_number: str = None,
        properties: str = None
    ):
        """
            产品ID
        """
        self._product_id = product_id
        """
            采购基准价，最大值1000000000
        """
        self._standard_price = standard_price
        """
            代销采购价
        """
        self._agent_cost_price = agent_cost_price
        """
            经销采购价
        """
        self._dealer_cost_price = dealer_cost_price
        """
            sku产品库存，在0到1000000之间，如果不传，则库存为0
        """
        self._quantity = quantity
        """
            商家编码
        """
        self._sku_number = sku_number
        """
            sku属性
        """
        self._properties = properties

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
    def standard_price(self):
        return self._standard_price

    @standard_price.setter
    def standard_price(self, standard_price):
        if isinstance(standard_price, str):
            self._standard_price = standard_price
        else:
            raise TypeError("standard_price must be str")

    @property
    def agent_cost_price(self):
        return self._agent_cost_price

    @agent_cost_price.setter
    def agent_cost_price(self, agent_cost_price):
        if isinstance(agent_cost_price, str):
            self._agent_cost_price = agent_cost_price
        else:
            raise TypeError("agent_cost_price must be str")

    @property
    def dealer_cost_price(self):
        return self._dealer_cost_price

    @dealer_cost_price.setter
    def dealer_cost_price(self, dealer_cost_price):
        if isinstance(dealer_cost_price, str):
            self._dealer_cost_price = dealer_cost_price
        else:
            raise TypeError("dealer_cost_price must be str")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int):
            self._quantity = quantity
        else:
            raise TypeError("quantity must be int")

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
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        if isinstance(properties, str):
            self._properties = properties
        else:
            raise TypeError("properties must be str")


    def get_api_name(self):
        return "taobao.fenxiao.product.sku.add"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._standard_price is not None:
            request_dict["standard_price"] = convert_basic(self._standard_price)

        if self._agent_cost_price is not None:
            request_dict["agent_cost_price"] = convert_basic(self._agent_cost_price)

        if self._dealer_cost_price is not None:
            request_dict["dealer_cost_price"] = convert_basic(self._dealer_cost_price)

        if self._quantity is not None:
            request_dict["quantity"] = convert_basic(self._quantity)

        if self._sku_number is not None:
            request_dict["sku_number"] = convert_basic(self._sku_number)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductQuantityUpdateRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        type: int = None,
        quantity: str = None,
        properties: str = None
    ):
        """
            产品ID
        """
        self._product_id = product_id
        """
            库存更新方式，可选。1为全量更新，2为增量更新。如果不填，默认为全量更新。当选择全量更新时，如果库存更新值传入的是负数，会出错并返回错误码；当选择增量更新时，如果库存更新值为负数且绝对值大于当前库存，则sku库存会设置为0
        """
        self._type = type
        """
            库存修改值。产品有sku时，与sku属性顺序对应，用,分隔。产品无sku时，只写库存值。
当全量更新库存时，quantity必须为大于等于0的正整数；当增量更新库存时，quantity为整数，可小于等于0。若增量更新时传入的库存为负数，则负数与实际库存之和不能小于0。比如当前实际库存为1，传入增量更新quantity=-1，库存改为0
        """
        self._quantity = quantity
        """
            sku属性值，产品有sku时填写，多个sku用,分隔。为空时默认该产品无sku，则只修改产品的库存。请参照taobao.fenxiao.products.get接口返回的properties设置入参
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
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, str):
            self._quantity = quantity
        else:
            raise TypeError("quantity must be str")

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
        return "taobao.fenxiao.product.quantity.update"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._quantity is not None:
            request_dict["quantity"] = convert_basic(self._quantity)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


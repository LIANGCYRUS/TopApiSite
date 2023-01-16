from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemQuantityUpdateRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        sku_id: int = None,
        outer_id: str = None,
        quantity: int = None,
        type: int = None
    ):
        """
            商品数字ID，必填参数
        """
        self._num_iid = num_iid
        """
            要操作的SKU的数字ID，可选。如果不填默认修改宝贝的库存，如果填上则修改该SKU的库存
        """
        self._sku_id = sku_id
        """
            SKU的商家编码，可选参数。如果不填则默认修改宝贝的库存，如果填了则按照商家编码搜索出对应的SKU并修改库存。当sku_id和本字段都填写时以sku_id为准搜索对应SKU
        """
        self._outer_id = outer_id
        """
            库存修改值，必选。当全量更新库存时，quantity必须为大于等于0的正整数；当增量更新库存时，quantity为整数，可小于等于0。若增量更新时传入的库存为负数，则负数与实际库存之和不能小于0。比如当前实际库存为1，传入增量更新quantity=-1，库存改为0
        """
        self._quantity = quantity
        """
            库存更新方式，可选。1为全量更新，2为增量更新。如果不填，默认为全量更新
        """
        self._type = type

    @property
    def num_iid(self):
        return self._num_iid

    @num_iid.setter
    def num_iid(self, num_iid):
        if isinstance(num_iid, int):
            self._num_iid = num_iid
        else:
            raise TypeError("num_iid must be int")

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
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")

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
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")


    def get_api_name(self):
        return "taobao.item.quantity.update"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._quantity is not None:
            request_dict["quantity"] = convert_basic(self._quantity)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


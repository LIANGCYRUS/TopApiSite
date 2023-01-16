from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoScitemMapAddRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        sku_id: int = None,
        sc_item_id: int = None,
        outer_code: str = None,
        need_check: bool = None
    ):
        """
            前台ic商品id
        """
        self._item_id = item_id
        """
            前台ic商品skuid
        """
        self._sku_id = sku_id
        """
            sc_item_id和outer_code 其中一个不能为空
        """
        self._sc_item_id = sc_item_id
        """
            sc_item_id和outer_code 其中一个不能为空
        """
        self._outer_code = outer_code
        """
            默认值为false
true:进行高级校验,前端商品或SKU的商家编码必须与后端商品的商家编码一致，否则会拒绝关联
false:不进行高级校验
        """
        self._need_check = need_check

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, int):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be int")

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
    def sc_item_id(self):
        return self._sc_item_id

    @sc_item_id.setter
    def sc_item_id(self, sc_item_id):
        if isinstance(sc_item_id, int):
            self._sc_item_id = sc_item_id
        else:
            raise TypeError("sc_item_id must be int")

    @property
    def outer_code(self):
        return self._outer_code

    @outer_code.setter
    def outer_code(self, outer_code):
        if isinstance(outer_code, str):
            self._outer_code = outer_code
        else:
            raise TypeError("outer_code must be str")

    @property
    def need_check(self):
        return self._need_check

    @need_check.setter
    def need_check(self, need_check):
        if isinstance(need_check, bool):
            self._need_check = need_check
        else:
            raise TypeError("need_check must be bool")


    def get_api_name(self):
        return "taobao.scitem.map.add"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        if self._sc_item_id is not None:
            request_dict["sc_item_id"] = convert_basic(self._sc_item_id)

        if self._outer_code is not None:
            request_dict["outer_code"] = convert_basic(self._outer_code)

        if self._need_check is not None:
            request_dict["need_check"] = convert_basic(self._need_check)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


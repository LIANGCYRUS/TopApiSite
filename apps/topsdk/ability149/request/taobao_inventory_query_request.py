from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoInventoryQueryRequest(BaseRequest):

    def __init__(
        self,
        sc_item_ids: str = None,
        sc_item_codes: str = None,
        seller_nick: str = None,
        store_codes: str = None
    ):
        """
            后端商品ID 列表，控制到50个
        """
        self._sc_item_ids = sc_item_ids
        """
            后端商品的商家编码列表，控制到50个
        """
        self._sc_item_codes = sc_item_codes
        """
            卖家昵称
        """
        self._seller_nick = seller_nick
        """
            仓库列表:GLY001^GLY002
        """
        self._store_codes = store_codes

    @property
    def sc_item_ids(self):
        return self._sc_item_ids

    @sc_item_ids.setter
    def sc_item_ids(self, sc_item_ids):
        if isinstance(sc_item_ids, str):
            self._sc_item_ids = sc_item_ids
        else:
            raise TypeError("sc_item_ids must be str")

    @property
    def sc_item_codes(self):
        return self._sc_item_codes

    @sc_item_codes.setter
    def sc_item_codes(self, sc_item_codes):
        if isinstance(sc_item_codes, str):
            self._sc_item_codes = sc_item_codes
        else:
            raise TypeError("sc_item_codes must be str")

    @property
    def seller_nick(self):
        return self._seller_nick

    @seller_nick.setter
    def seller_nick(self, seller_nick):
        if isinstance(seller_nick, str):
            self._seller_nick = seller_nick
        else:
            raise TypeError("seller_nick must be str")

    @property
    def store_codes(self):
        return self._store_codes

    @store_codes.setter
    def store_codes(self, store_codes):
        if isinstance(store_codes, str):
            self._store_codes = store_codes
        else:
            raise TypeError("store_codes must be str")


    def get_api_name(self):
        return "taobao.inventory.query"

    def to_dict(self):
        request_dict = {}
        if self._sc_item_ids is not None:
            request_dict["sc_item_ids"] = convert_basic(self._sc_item_ids)

        if self._sc_item_codes is not None:
            request_dict["sc_item_codes"] = convert_basic(self._sc_item_codes)

        if self._seller_nick is not None:
            request_dict["seller_nick"] = convert_basic(self._seller_nick)

        if self._store_codes is not None:
            request_dict["store_codes"] = convert_basic(self._store_codes)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


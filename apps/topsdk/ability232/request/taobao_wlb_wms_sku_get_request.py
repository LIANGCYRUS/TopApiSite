from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsSkuGetRequest(BaseRequest):

    def __init__(
        self,
        item_code: str = None,
        item_id: str = None,
        owner_user_id: str = None
    ):
        """
            菜鸟商品ID,与itemcode必须有一个值不为空
        """
        self._item_code = item_code
        """
            商家商品编码,与itemid必须有一个值不为空
        """
        self._item_id = item_id
        """
            货主ID
        """
        self._owner_user_id = owner_user_id

    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        if isinstance(item_code, str):
            self._item_code = item_code
        else:
            raise TypeError("item_code must be str")

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, str):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be str")

    @property
    def owner_user_id(self):
        return self._owner_user_id

    @owner_user_id.setter
    def owner_user_id(self, owner_user_id):
        if isinstance(owner_user_id, str):
            self._owner_user_id = owner_user_id
        else:
            raise TypeError("owner_user_id must be str")


    def get_api_name(self):
        return "taobao.wlb.wms.sku.get"

    def to_dict(self):
        request_dict = {}
        if self._item_code is not None:
            request_dict["item_code"] = convert_basic(self._item_code)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._owner_user_id is not None:
            request_dict["owner_user_id"] = convert_basic(self._owner_user_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


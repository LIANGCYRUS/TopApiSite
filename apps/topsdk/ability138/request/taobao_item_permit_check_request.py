from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemPermitCheckRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        cid: int = None,
        type: str = None
    ):
        """
            商品id
        """
        self._item_id = item_id
        """
            类目id
        """
        self._cid = cid
        """
            发布类型。可选值:fixed(一口价),auction(拍卖)
        """
        self._type = type

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
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, cid):
        if isinstance(cid, int):
            self._cid = cid
        else:
            raise TypeError("cid must be int")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")


    def get_api_name(self):
        return "taobao.item.permit.check"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


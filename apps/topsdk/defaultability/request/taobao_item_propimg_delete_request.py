from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemPropimgDeleteRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        id: int = None
    ):
        """
            商品数字ID，必选
        """
        self._num_iid = num_iid
        """
            商品属性图片ID
        """
        self._id = id

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
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise TypeError("id must be int")


    def get_api_name(self):
        return "taobao.item.propimg.delete"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._id is not None:
            request_dict["id"] = convert_basic(self._id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemSkuGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        sku_id: int = None,
        num_iid: int = None
    ):
        """
            需返回的字段列表。可选值：Sku结构体中的所有字段；字段之间用“,”分隔。
        """
        self._fields = fields
        """
            Sku的id。可以通过taobao.item.seller.get得到
        """
        self._sku_id = sku_id
        """
            商品的数字IID（num_iid和nick必传一个，推荐用num_iid），传商品的数字id返回的结果里包含cspu（SKu上的产品规格信息）。
        """
        self._num_iid = num_iid

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")

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
    def num_iid(self):
        return self._num_iid

    @num_iid.setter
    def num_iid(self, num_iid):
        if isinstance(num_iid, int):
            self._num_iid = num_iid
        else:
            raise TypeError("num_iid must be int")


    def get_api_name(self):
        return "taobao.item.sku.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._sku_id is not None:
            request_dict["sku_id"] = convert_basic(self._sku_id)

        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


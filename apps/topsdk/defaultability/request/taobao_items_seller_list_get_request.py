from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemsSellerListGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        num_iids: list = None
    ):
        """
            需要返回的商品字段列表。可选值：点击返回结果中的Item结构体中能展示出来的所有字段，多个字段用“,”分隔。注：返回所有sku信息的字段名称是sku而不是skus。
        """
        self._fields = fields
        """
            商品ID列表，多个ID用半角逗号隔开，一次最多不超过20个。注：获取不存在的商品ID或获取别人的商品都不会报错，但没有商品数据返回。
        """
        self._num_iids = num_iids

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
    def num_iids(self):
        return self._num_iids

    @num_iids.setter
    def num_iids(self, num_iids):
        if isinstance(num_iids, list):
            self._num_iids = num_iids
        else:
            raise TypeError("num_iids must be list")


    def get_api_name(self):
        return "taobao.items.seller.list.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._num_iids is not None:
            request_dict["num_iids"] = convert_basic_list(self._num_iids)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


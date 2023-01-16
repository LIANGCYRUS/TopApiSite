from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoDiscountsGetRequest(BaseRequest):

    def __init__(
        self,
        discount_id: int = None,
        ext_fields: str = None
    ):
        """
            折扣ID
        """
        self._discount_id = discount_id
        """
            指定查询额外的信息，可选值：DETAIL（查询折扣详情），多个可选值用逗号分割。（只允许指定折扣ID情况下使用）
        """
        self._ext_fields = ext_fields

    @property
    def discount_id(self):
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        if isinstance(discount_id, int):
            self._discount_id = discount_id
        else:
            raise TypeError("discount_id must be int")

    @property
    def ext_fields(self):
        return self._ext_fields

    @ext_fields.setter
    def ext_fields(self, ext_fields):
        if isinstance(ext_fields, str):
            self._ext_fields = ext_fields
        else:
            raise TypeError("ext_fields must be str")


    def get_api_name(self):
        return "taobao.fenxiao.discounts.get"

    def to_dict(self):
        request_dict = {}
        if self._discount_id is not None:
            request_dict["discount_id"] = convert_basic(self._discount_id)

        if self._ext_fields is not None:
            request_dict["ext_fields"] = convert_basic(self._ext_fields)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


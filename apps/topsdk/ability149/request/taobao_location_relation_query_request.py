from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLocationRelationQueryRequest(BaseRequest):

    def __init__(
        self,
        location_relation: object = None
    ):
        """
            关系查询
        """
        self._location_relation = location_relation

    @property
    def location_relation(self):
        return self._location_relation

    @location_relation.setter
    def location_relation(self, location_relation):
        if isinstance(location_relation, object):
            self._location_relation = location_relation
        else:
            raise TypeError("location_relation must be object")


    def get_api_name(self):
        return "taobao.location.relation.query"

    def to_dict(self):
        request_dict = {}
        if self._location_relation is not None:
            request_dict["location_relation"] = convert_struct(self._location_relation)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoLocationRelationQueryLocationRelationDto:
    def __init__(
        self,
        target_inv_store_type: int = None,
        target_store_code: str = None,
        source_inv_store_type: int = None,
        source_store_code: str = None
    ):
        """
            实体类型 2：仓库  6：门店 （target,sorce 二选一填写，都填写报错）
        """
        self.target_inv_store_type = target_inv_store_type
        """
            实体code
        """
        self.target_store_code = target_store_code
        """
            实体类型 2：仓库  6：门店
        """
        self.source_inv_store_type = source_inv_store_type
        """
            实体code
        """
        self.source_store_code = source_store_code


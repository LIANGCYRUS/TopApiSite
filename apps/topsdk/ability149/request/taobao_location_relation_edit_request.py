from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLocationRelationEditRequest(BaseRequest):

    def __init__(
        self,
        location_relation_list: list = None
    ):
        """
            关系对象列表
        """
        self._location_relation_list = location_relation_list

    @property
    def location_relation_list(self):
        return self._location_relation_list

    @location_relation_list.setter
    def location_relation_list(self, location_relation_list):
        if isinstance(location_relation_list, list):
            self._location_relation_list = location_relation_list
        else:
            raise TypeError("location_relation_list must be list")


    def get_api_name(self):
        return "taobao.location.relation.edit"

    def to_dict(self):
        request_dict = {}
        if self._location_relation_list is not None:
            request_dict["location_relation_list"] = convert_struct_list(self._location_relation_list)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoLocationRelationEditLocationRelationDto:
    def __init__(
        self,
        status: int = None,
        target_inv_store_type: int = None,
        target_store_code: str = None,
        source_inv_store_type: int = None,
        source_store_code: str = None
    ):
        """
            状态  0 正常  -1 删除
        """
        self.status = status
        """
            实体类型 2：仓库 6：门店
        """
        self.target_inv_store_type = target_inv_store_type
        """
            实体code
        """
        self.target_store_code = target_store_code
        """
            实体类型 2：仓库 6：门店
        """
        self.source_inv_store_type = source_inv_store_type
        """
            实体code
        """
        self.source_store_code = source_store_code


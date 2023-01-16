from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoInventoryWarehouseManageRequest(BaseRequest):

    def __init__(
        self,
        ware_house_dto: object = None
    ):
        """
            仓库信息
        """
        self._ware_house_dto = ware_house_dto

    @property
    def ware_house_dto(self):
        return self._ware_house_dto

    @ware_house_dto.setter
    def ware_house_dto(self, ware_house_dto):
        if isinstance(ware_house_dto, object):
            self._ware_house_dto = ware_house_dto
        else:
            raise TypeError("ware_house_dto must be object")


    def get_api_name(self):
        return "taobao.inventory.warehouse.manage"

    def to_dict(self):
        request_dict = {}
        if self._ware_house_dto is not None:
            request_dict["ware_house_dto"] = convert_struct(self._ware_house_dto)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoInventoryWarehouseManageWareHouseDto:
    def __init__(
        self,
        address: str = None,
        address_area_name: str = None,
        alias_name: str = None,
        contact: str = None,
        phone: str = None,
        post_code: str = None,
        store_code: str = None,
        store_name: str = None,
        operate_type: str = None
    ):
        """
            详细地址描述
        """
        self.address = address
        """
            仓库地址信息,格式 :省~市~区县
        """
        self.address_area_name = address_area_name
        """
            别名
        """
        self.alias_name = alias_name
        """
            联系人
        """
        self.contact = contact
        """
            电话号码
        """
        self.phone = phone
        """
            邮编
        """
        self.post_code = post_code
        """
            仓库编码，仅允许使用字母、数字、下划线，并且在6-30个字符内
        """
        self.store_code = store_code
        """
            仓库名称
        """
        self.store_name = store_name
        """
            操作类型，新增:ADD;修改:UPDATE
        """
        self.operate_type = operate_type


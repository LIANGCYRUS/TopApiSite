from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class CainiaoMerchantInventoryAdjustRequest(BaseRequest):

    def __init__(
        self,
        adjust_request: list = None,
        app_name: str = None,
        operation: str = None
    ):
        """
            商家仓编辑库存
        """
        self._adjust_request = adjust_request
        """
            调用方应用名
        """
        self._app_name = app_name
        """
            操作
        """
        self._operation = operation

    @property
    def adjust_request(self):
        return self._adjust_request

    @adjust_request.setter
    def adjust_request(self, adjust_request):
        if isinstance(adjust_request, list):
            self._adjust_request = adjust_request
        else:
            raise TypeError("adjust_request must be list")

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        if isinstance(app_name, str):
            self._app_name = app_name
        else:
            raise TypeError("app_name must be str")

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, operation):
        if isinstance(operation, str):
            self._operation = operation
        else:
            raise TypeError("operation must be str")


    def get_api_name(self):
        return "cainiao.merchant.inventory.adjust"

    def to_dict(self):
        request_dict = {}
        if self._adjust_request is not None:
            request_dict["adjust_request"] = convert_struct_list(self._adjust_request)

        if self._app_name is not None:
            request_dict["app_name"] = convert_basic(self._app_name)

        if self._operation is not None:
            request_dict["operation"] = convert_basic(self._operation)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class CainiaoMerchantInventoryAdjustMerStoreInvAdjustDto:
    def __init__(
        self,
        inventory_type: int = None,
        attribute: dict = None,
        quantity: int = None,
        out_biz_code: str = None,
        store_code: str = None,
        sc_item_id: int = None
    ):
        """
            库存类型
        """
        self.inventory_type = inventory_type
        """
            扩展属性
        """
        self.attribute = attribute
        """
            数量
        """
        self.quantity = quantity
        """
            外部操作唯一编码
        """
        self.out_biz_code = out_biz_code
        """
            仓库编码
        """
        self.store_code = store_code
        """
            货品id
        """
        self.sc_item_id = sc_item_id


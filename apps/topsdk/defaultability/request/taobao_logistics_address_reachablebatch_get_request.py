from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsAddressReachablebatchGetRequest(BaseRequest):

    def __init__(
        self,
        address_list: list = None
    ):
        """
            筛单用户输入地址结构
        """
        self._address_list = address_list

    @property
    def address_list(self):
        return self._address_list

    @address_list.setter
    def address_list(self, address_list):
        if isinstance(address_list, list):
            self._address_list = address_list
        else:
            raise TypeError("address_list must be list")


    def get_api_name(self):
        return "taobao.logistics.address.reachablebatch.get"

    def to_dict(self):
        request_dict = {}
        if self._address_list is not None:
            request_dict["address_list"] = convert_struct_list(self._address_list)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoLogisticsAddressReachablebatchGetAddressReachable:
    def __init__(
        self,
        source_area_code: str = None,
        service_type: int = None,
        partner_id: str = None,
        area_code: str = None,
        address: str = None
    ):
        """
            发货地，标准区域编码(四级行政)，可以通过taobao.areas.get获取，如浙江省杭州市余杭区闲林街道为 330110011
        """
        self.source_area_code = source_area_code
        """
            服务对应的数字编码，如揽派范围对应88
        """
        self.service_type = service_type
        """
            物流公司编码ID，可以从这个接口获取所有物流公司的标准编码taobao.logistics.companies.get，可以传入多个值，以英文逗号分隔，如“1000000952,1000000953”
        """
        self.partner_id = partner_id
        """
            标准区域编码(三级行政区编码或是四级行政区)，可以通过taobao.areas.get获取，如北京市朝阳区为110105
        """
        self.area_code = area_code
        """
            详细地址
        """
        self.address = address


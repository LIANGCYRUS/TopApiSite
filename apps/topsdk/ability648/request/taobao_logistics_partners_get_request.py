from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsPartnersGetRequest(BaseRequest):

    def __init__(
        self,
        source_id: str = None,
        target_id: str = None,
        service_type: str = None,
        goods_value: str = None,
        is_need_carriage: bool = None
    ):
        """
            物流公司揽货地地区码（必须是区、县一级的）.参考:http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201401/t20140116_501070.html或者调用 taobao.areas.get 获取
        """
        self._source_id = source_id
        """
            物流公司派送地地区码（必须是区、县一级的）.参考:http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201401/t20140116_501070.html或者调用 taobao.areas.get 获取
        """
        self._target_id = target_id
        """
            服务类型，根据此参数可查出提供相应服务类型的物流公司信息(物流公司状态正常)，可选值：cod(货到付款)、online(在线下单)、 offline(自己联系)、limit(限时物流)。然后再根据source_id,target_id,goods_value这三个条件来过滤物流公司. 目前输入自己联系服务类型将会返回空，因为自己联系并没有具体的服务信息，所以不会有记录。
        """
        self._service_type = service_type
        """
            货物价格.只有当选择货到付款此参数才会有效
        """
        self._goods_value = goods_value
        """
            是否需要揽收资费信息，默认false。在此值为false时，返回内容中将无carriage。在未设置source_id或target_id的情况下，无法查询揽收资费信息。自己联系无揽收资费记录。
        """
        self._is_need_carriage = is_need_carriage

    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        if isinstance(source_id, str):
            self._source_id = source_id
        else:
            raise TypeError("source_id must be str")

    @property
    def target_id(self):
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        if isinstance(target_id, str):
            self._target_id = target_id
        else:
            raise TypeError("target_id must be str")

    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        if isinstance(service_type, str):
            self._service_type = service_type
        else:
            raise TypeError("service_type must be str")

    @property
    def goods_value(self):
        return self._goods_value

    @goods_value.setter
    def goods_value(self, goods_value):
        if isinstance(goods_value, str):
            self._goods_value = goods_value
        else:
            raise TypeError("goods_value must be str")

    @property
    def is_need_carriage(self):
        return self._is_need_carriage

    @is_need_carriage.setter
    def is_need_carriage(self, is_need_carriage):
        if isinstance(is_need_carriage, bool):
            self._is_need_carriage = is_need_carriage
        else:
            raise TypeError("is_need_carriage must be bool")


    def get_api_name(self):
        return "taobao.logistics.partners.get"

    def to_dict(self):
        request_dict = {}
        if self._source_id is not None:
            request_dict["source_id"] = convert_basic(self._source_id)

        if self._target_id is not None:
            request_dict["target_id"] = convert_basic(self._target_id)

        if self._service_type is not None:
            request_dict["service_type"] = convert_basic(self._service_type)

        if self._goods_value is not None:
            request_dict["goods_value"] = convert_basic(self._goods_value)

        if self._is_need_carriage is not None:
            request_dict["is_need_carriage"] = convert_basic(self._is_need_carriage)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


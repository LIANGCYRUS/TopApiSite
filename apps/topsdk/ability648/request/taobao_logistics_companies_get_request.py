from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsCompaniesGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        is_recommended: bool = None,
        order_mode: str = None
    ):
        """
            需返回的字段列表。可选值:LogisticCompany 结构中的所有字段;多个字段间用","逗号隔开.
如:id,code,name,reg_mail_no
<br><font color='red'>说明：</font>
<br>id：物流公司ID
<br>code：物流公司code
<br>name：物流公司名称
<br>reg_mail_no：物流公司对应的运单规则
        """
        self._fields = fields
        """
            是否查询推荐物流公司.可选值:true,false.如果不提供此参数,将会返回所有支持电话联系的物流公司.
        """
        self._is_recommended = is_recommended
        """
            推荐物流公司的下单方式.可选值:offline(电话联系/自己联系),online(在线下单),all(即电话联系又在线下单). 此参数仅仅用于is_recommended 为ture时。就是说对于推荐物流公司才可用.如果不选择此参数将会返回推荐物流中支持电话联系的物流公司.
        """
        self._order_mode = order_mode

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
    def is_recommended(self):
        return self._is_recommended

    @is_recommended.setter
    def is_recommended(self, is_recommended):
        if isinstance(is_recommended, bool):
            self._is_recommended = is_recommended
        else:
            raise TypeError("is_recommended must be bool")

    @property
    def order_mode(self):
        return self._order_mode

    @order_mode.setter
    def order_mode(self, order_mode):
        if isinstance(order_mode, str):
            self._order_mode = order_mode
        else:
            raise TypeError("order_mode must be str")


    def get_api_name(self):
        return "taobao.logistics.companies.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._is_recommended is not None:
            request_dict["is_recommended"] = convert_basic(self._is_recommended)

        if self._order_mode is not None:
            request_dict["order_mode"] = convert_basic(self._order_mode)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


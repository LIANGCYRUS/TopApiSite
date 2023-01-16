from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoDeliveryTemplateGetRequest(BaseRequest):

    def __init__(
        self,
        template_ids: list = None,
        fields: list = None,
        user_nick: str = None
    ):
        """
            需要查询的运费模板ID列表
        """
        self._template_ids = template_ids
        """
            需返回的字段列表。 <br/> 
<B>
可选值:示例中的值;各字段之间用","隔开
</B>
<br/><br/> 
<font color=blue>
template_id：查询模板ID <br/> 
template_name:查询模板名称 <br/> 
assumer：查询服务承担放 <br/> 
valuation:查询计价规则 <br/> 
supports:查询增值服务列表 <br/> 
created:查询模板创建时间 <br/> 
modified:查询修改时间<br/> 
consign_area_id:运费模板上设置的卖家发货地址最小级别ID<br/> 
address:卖家地址信息
</font>
<br/><br/> 
<font color=bule>
query_cod:查询货到付款运费信息<br/> 
query_post:查询平邮运费信息 <br/> 
query_express:查询快递公司运费信息 <br/> 
query_ems:查询EMS运费信息<br/> 
query_bzsd:查询普通保障速递运费信息<br/> 
query_wlb:查询物流宝保障速递运费信息<br/> 
query_furniture:查询家装物流运费信息
<font color=blue>
<br/><br/>
<font color=red>不能有空格</font>
        """
        self._fields = fields
        """
            在没有登录的情况下根据淘宝用户昵称查询指定的模板
        """
        self._user_nick = user_nick

    @property
    def template_ids(self):
        return self._template_ids

    @template_ids.setter
    def template_ids(self, template_ids):
        if isinstance(template_ids, list):
            self._template_ids = template_ids
        else:
            raise TypeError("template_ids must be list")

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
    def user_nick(self):
        return self._user_nick

    @user_nick.setter
    def user_nick(self, user_nick):
        if isinstance(user_nick, str):
            self._user_nick = user_nick
        else:
            raise TypeError("user_nick must be str")


    def get_api_name(self):
        return "taobao.delivery.template.get"

    def to_dict(self):
        request_dict = {}
        if self._template_ids is not None:
            request_dict["template_ids"] = convert_basic_list(self._template_ids)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._user_nick is not None:
            request_dict["user_nick"] = convert_basic(self._user_nick)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


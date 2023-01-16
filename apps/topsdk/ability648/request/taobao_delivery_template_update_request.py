from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoDeliveryTemplateUpdateRequest(BaseRequest):

    def __init__(
        self,
        name: str = None,
        template_id: int = None,
        assumer: int = None,
        template_types: str = None,
        template_dests: str = None,
        template_start_standards: str = None,
        template_start_fees: str = None,
        template_add_standards: str = None,
        template_add_fees: str = None
    ):
        """
            模板名称，长度不能大于50个字节
        """
        self._name = name
        """
            需要修改的模板对应的模板ID
        """
        self._template_id = template_id
        """
            可选值：0,1 <br>  说明<br>0:表示买家承担服务费;<br>1:表示卖家承担服务费
        """
        self._assumer = assumer
        """
            运费方式:平邮 (post),快递公司(express),EMS (ems),货到付款(cod)结构:value1;value2;value3;value4 
如: post;express;ems;cod 
<br/><font color=red>
注意:在添加多个运费方式时,字符串中使用 ";" 分号区分。template_dests(指定地区) template_start_standards(首费标准)、template_start_fees(首费)、template_add_standards(增费标准)、template_add_fees(增费)必须与template_types的分号数量相同. 
 </font>
<br/>
<font color=blue>
普通用户：post,ems,express三种运费方式必须填写一个，不能填写cod。
货到付款用户：如果填写了cod运费方式，则post,ems,express三种运费方式也必须填写一个，如果没有填写cod则填写的运费方式中必须存在express</font>
        """
        self._template_types = template_types
        """
            邮费子项涉及的地区.结构: value1;value2;value3,value4
<br>如:1,110000;1,110000;1,310000;1,320000,330000。 aredId解释(1=全国,110000=北京,310000=上海,320000=江苏,330000=浙江)
如果template_types设置为post;ems;exmpress;cod则表示为平邮(post)指定默认地区(全国)和北京地区的运费;其他的类似以分号区分一一对应
<br/>可以用taobao.areas.get接口获取.或者参考：http://www.stats.gov.cn/tjbz/xzqhdm/t20080215_402462675.htm
<br/><font color=red>每个运费方式设置的设涉及地区中必须包含全国地区（areaId=1）表示默认运费,可以只设置默认运费</font>
<br><font color=blue>注意:为多个地区指定指定不同（首费标准、首费、增费标准、增费一项不一样就算不同）的运费以逗号","区分，
template_start_standards(首费标准)、template_start_fees(首费)、
template_add_standards(增费标准)、
template_add_fees(增费)必须与template_types分号数量相同。如果为需要为多个地区指定相同运费则地区之间用“|”隔开即可。</font>
        """
        self._template_dests = template_dests
        """
            首费标准：当valuation(记价方式)为0时输入1-9999范围内的整数<br><font color=blue>首费标准目前只能为1</br>
<br><font color=red>输入的格式分号个数和template_types数量一致，逗号个数必须与template_dests以分号隔开之后一一对应的数量一致</font>
        """
        self._template_start_standards = template_start_standards
        """
            首费：输入0.01-999.99（最多包含两位小数）
<br/><font color=blue> 首费不能为0</font><br><font color=red>输入的格式分号个数和template_types数量一致，逗号个数必须与template_dests以分号隔开之后一一对应的数量一致</font>
        """
        self._template_start_fees = template_start_fees
        """
            增费标准：当valuation(记价方式)为0时输入1-9999范围内的整数<br><font color=blue>增费标准目前只能为1</font>
<br><font color=red>输入的格式分号个数和template_types数量一致，逗号个数必须与template_dests以分号隔开之后一一对应的数量一致</font>
        """
        self._template_add_standards = template_add_standards
        """
            增费：输入0.00-999.99（最多包含两位小数）<br/><font color=blue>增费可以为0</font><br/><font color=red>输入的格式分号个数和template_types数量一致，逗号个数必须与template_dests以分号隔开之后一一对应的数量一致</font>
        """
        self._template_add_fees = template_add_fees

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        if isinstance(template_id, int):
            self._template_id = template_id
        else:
            raise TypeError("template_id must be int")

    @property
    def assumer(self):
        return self._assumer

    @assumer.setter
    def assumer(self, assumer):
        if isinstance(assumer, int):
            self._assumer = assumer
        else:
            raise TypeError("assumer must be int")

    @property
    def template_types(self):
        return self._template_types

    @template_types.setter
    def template_types(self, template_types):
        if isinstance(template_types, str):
            self._template_types = template_types
        else:
            raise TypeError("template_types must be str")

    @property
    def template_dests(self):
        return self._template_dests

    @template_dests.setter
    def template_dests(self, template_dests):
        if isinstance(template_dests, str):
            self._template_dests = template_dests
        else:
            raise TypeError("template_dests must be str")

    @property
    def template_start_standards(self):
        return self._template_start_standards

    @template_start_standards.setter
    def template_start_standards(self, template_start_standards):
        if isinstance(template_start_standards, str):
            self._template_start_standards = template_start_standards
        else:
            raise TypeError("template_start_standards must be str")

    @property
    def template_start_fees(self):
        return self._template_start_fees

    @template_start_fees.setter
    def template_start_fees(self, template_start_fees):
        if isinstance(template_start_fees, str):
            self._template_start_fees = template_start_fees
        else:
            raise TypeError("template_start_fees must be str")

    @property
    def template_add_standards(self):
        return self._template_add_standards

    @template_add_standards.setter
    def template_add_standards(self, template_add_standards):
        if isinstance(template_add_standards, str):
            self._template_add_standards = template_add_standards
        else:
            raise TypeError("template_add_standards must be str")

    @property
    def template_add_fees(self):
        return self._template_add_fees

    @template_add_fees.setter
    def template_add_fees(self, template_add_fees):
        if isinstance(template_add_fees, str):
            self._template_add_fees = template_add_fees
        else:
            raise TypeError("template_add_fees must be str")


    def get_api_name(self):
        return "taobao.delivery.template.update"

    def to_dict(self):
        request_dict = {}
        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._template_id is not None:
            request_dict["template_id"] = convert_basic(self._template_id)

        if self._assumer is not None:
            request_dict["assumer"] = convert_basic(self._assumer)

        if self._template_types is not None:
            request_dict["template_types"] = convert_basic(self._template_types)

        if self._template_dests is not None:
            request_dict["template_dests"] = convert_basic(self._template_dests)

        if self._template_start_standards is not None:
            request_dict["template_start_standards"] = convert_basic(self._template_start_standards)

        if self._template_start_fees is not None:
            request_dict["template_start_fees"] = convert_basic(self._template_start_fees)

        if self._template_add_standards is not None:
            request_dict["template_add_standards"] = convert_basic(self._template_add_standards)

        if self._template_add_fees is not None:
            request_dict["template_add_fees"] = convert_basic(self._template_add_fees)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductcatAddRequest(BaseRequest):

    def __init__(
        self,
        name: str = None,
        retail_low_percent: int = None,
        retail_high_percent: int = None,
        agent_cost_percent: int = None,
        dealer_cost_percent: int = None
    ):
        """
            产品线名称
        """
        self._name = name
        """
            最低零售价比例，注意：100.00%，则输入为10000
        """
        self._retail_low_percent = retail_low_percent
        """
            最高零售价比例，注意：100.00%，则输入为10000
        """
        self._retail_high_percent = retail_high_percent
        """
            代销默认采购价比例，注意：100.00%，则输入为10000
        """
        self._agent_cost_percent = agent_cost_percent
        """
            经销默认采购价比例，注意：100.00%，则输入为10000
        """
        self._dealer_cost_percent = dealer_cost_percent

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
    def retail_low_percent(self):
        return self._retail_low_percent

    @retail_low_percent.setter
    def retail_low_percent(self, retail_low_percent):
        if isinstance(retail_low_percent, int):
            self._retail_low_percent = retail_low_percent
        else:
            raise TypeError("retail_low_percent must be int")

    @property
    def retail_high_percent(self):
        return self._retail_high_percent

    @retail_high_percent.setter
    def retail_high_percent(self, retail_high_percent):
        if isinstance(retail_high_percent, int):
            self._retail_high_percent = retail_high_percent
        else:
            raise TypeError("retail_high_percent must be int")

    @property
    def agent_cost_percent(self):
        return self._agent_cost_percent

    @agent_cost_percent.setter
    def agent_cost_percent(self, agent_cost_percent):
        if isinstance(agent_cost_percent, int):
            self._agent_cost_percent = agent_cost_percent
        else:
            raise TypeError("agent_cost_percent must be int")

    @property
    def dealer_cost_percent(self):
        return self._dealer_cost_percent

    @dealer_cost_percent.setter
    def dealer_cost_percent(self, dealer_cost_percent):
        if isinstance(dealer_cost_percent, int):
            self._dealer_cost_percent = dealer_cost_percent
        else:
            raise TypeError("dealer_cost_percent must be int")


    def get_api_name(self):
        return "taobao.fenxiao.productcat.add"

    def to_dict(self):
        request_dict = {}
        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._retail_low_percent is not None:
            request_dict["retail_low_percent"] = convert_basic(self._retail_low_percent)

        if self._retail_high_percent is not None:
            request_dict["retail_high_percent"] = convert_basic(self._retail_high_percent)

        if self._agent_cost_percent is not None:
            request_dict["agent_cost_percent"] = convert_basic(self._agent_cost_percent)

        if self._dealer_cost_percent is not None:
            request_dict["dealer_cost_percent"] = convert_basic(self._dealer_cost_percent)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


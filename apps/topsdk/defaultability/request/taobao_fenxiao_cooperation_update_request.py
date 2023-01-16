from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoCooperationUpdateRequest(BaseRequest):

    def __init__(
        self,
        distributor_id: int = None,
        grade_id: int = None,
        trade_type: str = None
    ):
        """
            分销商ID
        """
        self._distributor_id = distributor_id
        """
            等级ID(0代表取消)
        """
        self._grade_id = grade_id
        """
            分销方式(新增)： AGENT(代销)、DEALER(经销)(默认为代销)
        """
        self._trade_type = trade_type

    @property
    def distributor_id(self):
        return self._distributor_id

    @distributor_id.setter
    def distributor_id(self, distributor_id):
        if isinstance(distributor_id, int):
            self._distributor_id = distributor_id
        else:
            raise TypeError("distributor_id must be int")

    @property
    def grade_id(self):
        return self._grade_id

    @grade_id.setter
    def grade_id(self, grade_id):
        if isinstance(grade_id, int):
            self._grade_id = grade_id
        else:
            raise TypeError("grade_id must be int")

    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, trade_type):
        if isinstance(trade_type, str):
            self._trade_type = trade_type
        else:
            raise TypeError("trade_type must be str")


    def get_api_name(self):
        return "taobao.fenxiao.cooperation.update"

    def to_dict(self):
        request_dict = {}
        if self._distributor_id is not None:
            request_dict["distributor_id"] = convert_basic(self._distributor_id)

        if self._grade_id is not None:
            request_dict["grade_id"] = convert_basic(self._grade_id)

        if self._trade_type is not None:
            request_dict["trade_type"] = convert_basic(self._trade_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


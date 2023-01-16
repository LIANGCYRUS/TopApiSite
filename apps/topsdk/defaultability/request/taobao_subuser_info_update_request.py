from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSubuserInfoUpdateRequest(BaseRequest):

    def __init__(
        self,
        sub_id: int = None,
        is_dispatch: bool = None,
        is_disable_subaccount: bool = None
    ):
        """
            子账号ID
        """
        self._sub_id = sub_id
        """
            子账号是否参与分流 true:参与分流 false:不参与分流
        """
        self._is_dispatch = is_dispatch
        """
            是否停用子账号 true:表示停用该子账号false:表示开启该子账号
        """
        self._is_disable_subaccount = is_disable_subaccount

    @property
    def sub_id(self):
        return self._sub_id

    @sub_id.setter
    def sub_id(self, sub_id):
        if isinstance(sub_id, int):
            self._sub_id = sub_id
        else:
            raise TypeError("sub_id must be int")

    @property
    def is_dispatch(self):
        return self._is_dispatch

    @is_dispatch.setter
    def is_dispatch(self, is_dispatch):
        if isinstance(is_dispatch, bool):
            self._is_dispatch = is_dispatch
        else:
            raise TypeError("is_dispatch must be bool")

    @property
    def is_disable_subaccount(self):
        return self._is_disable_subaccount

    @is_disable_subaccount.setter
    def is_disable_subaccount(self, is_disable_subaccount):
        if isinstance(is_disable_subaccount, bool):
            self._is_disable_subaccount = is_disable_subaccount
        else:
            raise TypeError("is_disable_subaccount must be bool")


    def get_api_name(self):
        return "taobao.subuser.info.update"

    def to_dict(self):
        request_dict = {}
        if self._sub_id is not None:
            request_dict["sub_id"] = convert_basic(self._sub_id)

        if self._is_dispatch is not None:
            request_dict["is_dispatch"] = convert_basic(self._is_dispatch)

        if self._is_disable_subaccount is not None:
            request_dict["is_disable_subaccount"] = convert_basic(self._is_disable_subaccount)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


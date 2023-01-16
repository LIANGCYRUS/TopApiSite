from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallChannelTradeOrderCreateRequest(BaseRequest):

    def __init__(
        self,
        param0: object = None
    ):
        """
            入参
        """
        self._param0 = param0

    @property
    def param0(self):
        return self._param0

    @param0.setter
    def param0(self, param0):
        if isinstance(param0, object):
            self._param0 = param0
        else:
            raise TypeError("param0 must be object")


    def get_api_name(self):
        return "tmall.channel.trade.order.create"

    def to_dict(self):
        request_dict = {}
        if self._param0 is not None:
            request_dict["param0"] = convert_struct(self._param0)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TmallChannelTradeOrderCreateTopChannelSubPurchaseOrderCreateParam:
    def __init__(
        self,
        buy_quantity: int = None,
        product_sku_id: int = None,
        product_id: int = None
    ):
        """
            采购数量
        """
        self.buy_quantity = buy_quantity
        """
            采购货品SKU ID
        """
        self.product_sku_id = product_sku_id
        """
            采购货品ID
        """
        self.product_id = product_id

class TmallChannelTradeOrderCreateTopChannelPurchaseOrderCreateParam:
    def __init__(
        self,
        auto_audit: bool = None,
        down_account_id: int = None,
        request_no: str = None,
        items: list = None,
        down_role_type: int = None,
        down_account_type: int = None,
        down_user_nick: str = None,
        internal_code: str = None,
        channel: int = None
    ):
        """
            是否自动审批
        """
        self.auto_audit = auto_audit
        """
            分销商淘宝数字ID，如为空，down_user_nick必须输入
        """
        self.down_account_id = down_account_id
        """
            请求编码
        """
        self.request_no = request_no
        """
            采购明细
        """
        self.items = items
        """
            分销商渠道角色，默认分销终端商
        """
        self.down_role_type = down_role_type
        """
            分销商用户类型，默认淘宝用户
        """
        self.down_account_type = down_account_type
        """
            分销商昵称
        """
        self.down_user_nick = down_user_nick
        """
            内部编码
        """
        self.internal_code = internal_code
        """
            渠道编码，11-线下网批
        """
        self.channel = channel


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRefundsApplyGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        seller_nick: str = None,
        status: str = None,
        type: str = None,
        page_no: int = None,
        page_size: int = None
    ):
        """
            需要返回的字段。目前支持有：refund_id, tid, title, buyer_nick, seller_nick, total_fee, status, created, refund_fee
        """
        self._fields = fields
        """
            卖家昵称
        """
        self._seller_nick = seller_nick
        """
            退款状态，默认查询所有退款状态的数据，除了默认值外每次只能查询一种状态。
WAIT_SELLER_AGREE(买家已经申请退款，等待卖家同意) 
WAIT_BUYER_RETURN_GOODS(卖家已经同意退款，等待买家退货) 
WAIT_SELLER_CONFIRM_GOODS(买家已经退货，等待卖家确认收货) 
SELLER_REFUSE_BUYER(卖家拒绝退款) 
CLOSED(退款关闭) 
SUCCESS(退款成功)
        """
        self._status = status
        """
            交易类型列表，一次查询多种类型可用半角逗号分隔，默认同时查询guarantee_trade, auto_delivery的2种类型的数据。
fixed(一口价) 
auction(拍卖) 
guarantee_trade(一口价、拍卖) 
independent_simple_trade(旺店入门版交易) 
independent_shop_trade(旺店标准版交易) 
auto_delivery(自动发货) 
ec(直冲) 
cod(货到付款) 
fenxiao(分销) 
game_equipment(游戏装备) 
shopex_trade(ShopEX交易) 
netcn_trade(万网交易) 
external_trade(统一外部交易)
        """
        self._type = type
        """
            页码。传入值为 1 代表第一页，传入值为 2 代表第二页，依此类推。默认返回的数据是从第一页开始
        """
        self._page_no = page_no
        """
            每页条数。取值范围:大于零的整数; 默认值:40;最大值:100
        """
        self._page_size = page_size

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
    def seller_nick(self):
        return self._seller_nick

    @seller_nick.setter
    def seller_nick(self, seller_nick):
        if isinstance(seller_nick, str):
            self._seller_nick = seller_nick
        else:
            raise TypeError("seller_nick must be str")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")

    @property
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")


    def get_api_name(self):
        return "taobao.refunds.apply.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._seller_nick is not None:
            request_dict["seller_nick"] = convert_basic(self._seller_nick)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradesSoldGetRequest(BaseRequest):

    def __init__(
        self,
        buyer_open_id: str = None,
        fields: list = None,
        start_created: datetime = None,
        end_created: datetime = None,
        status: str = None,
        buyer_nick: str = None,
        type: str = None,
        ext_type: str = None,
        rate_status: str = None,
        tag: str = None,
        page_no: int = None,
        page_size: int = None,
        use_has_next: bool = None
    ):
        """
            买家的openId
        """
        self._buyer_open_id = buyer_open_id
        """
            需要返回的字段列表，多个字段用半角逗号分隔，可选值为返回示例中能看到的所有字段。rx_audit_status=0,处方药未审核
        """
        self._fields = fields
        """
            查询三个月内交易创建时间开始。格式:yyyy-MM-dd HH:mm:ss
        """
        self._start_created = start_created
        """
            查询交易创建时间结束。格式:yyyy-MM-dd HH:mm:ss
        """
        self._end_created = end_created
        """
            交易状态（<a href="http://open.taobao.com/doc/detail.htm?id=102856" target="_blank">查看可选值</a>），默认查询所有交易状态的数据，除了默认值外每次只能查询一种状态。
        """
        self._status = status
        """
            买家昵称
        """
        self._buyer_nick = buyer_nick
        """
            交易类型列表，同时查询多种交易类型可用逗号分隔。<span style="color:red;font-weight: bold;">默认同时查询guarantee_trade,auto_delivery,ec,cod,step 这5 种的交易类型的数据；查询所有交易类型的数据，需要设置下面全部可选值。</span>可选值：fixed(一口价)auction(拍卖)guarantee_trade(一口价、拍卖)step(分阶段付款，万人团，阶梯团订单）independent_simple_trade(旺店入门版交易)independent_shop_trade(旺店标准版交易)auto_delivery(自动发货)ec(直冲)cod(货到付款)game_equipment(游戏装备)shopex_trade(ShopEX交易)netcn_trade(万网交易)external_trade(统一外部交易)instant_trade (即时到账)b2c_cod(大商家货到付款)hotel_trade(酒店类型交易)super_market_trade(商超交易)super_market_cod_trade(商超货到付款交易)taohua(淘花网交易类型）waimai(外卖交易类型）o2o_offlinetrade（O2O交易）nopaid（即时到帐/趣味猜交易类型）step (万人团) eticket(电子凭证) tmall_i18n（天猫国际）;nopaid （无付款交易）insurance_plus（保险）finance（基金）注：guarantee_trade是一个组合查询条件，并不是一种交易类型，获取批量或单个订单中不会返回此种类型的订单。pre_auth_type(预授权0元购) lazada（获取lazada订单类型）
        """
        self._type = type
        """
            可选值有ershou(二手市场的订单）,service（商城服务子订单）mark（双十一大促活动异常订单）作为扩展类型筛选只能做单个ext_type查询，不能全部查询所有的ext_type类型
        """
        self._ext_type = ext_type
        """
            评价状态，默认查询所有评价状态的数据，除了默认值外每次只能查询一种状态。<br>可选值：RATE_UNBUYER(买家未评)RATE_UNSELLER(卖家未评)RATE_BUYER_UNSELLER(买家已评，卖家未评)RATE_UNBUYER_SELLER(买家未评，卖家已评)RATE_BUYER_SELLER(买家已评,卖家已评)
        """
        self._rate_status = rate_status
        """
            卖家对交易的自定义分组标签，目前可选值为：time_card（点卡软件代充），fee_card（话费软件代充）
        """
        self._tag = tag
        """
            页码。默认值:1，可填整数，通过传入page_no来控制获取的页数，总页数=total_results÷page_size
        """
        self._page_no = page_no
        """
            每页条数。 默认值:40;最大值:100，可填整数。通过page_no和page_size组合多次调用实现翻页获取全量数据。
        """
        self._page_size = page_size
        """
            是否启用has_next的分页方式，如果指定true,则返回的结果中不包含总记录数，但是会新增一个是否存在下一页的的字段，通过此种方式获取增量交易，接口调用成功率在原有的基础上有所提升。
        """
        self._use_has_next = use_has_next

    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, buyer_open_id):
        if isinstance(buyer_open_id, str):
            self._buyer_open_id = buyer_open_id
        else:
            raise TypeError("buyer_open_id must be str")

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
    def start_created(self):
        return self._start_created

    @start_created.setter
    def start_created(self, start_created):
        if isinstance(start_created, datetime):
            self._start_created = start_created
        else:
            raise TypeError("start_created must be datetime")

    @property
    def end_created(self):
        return self._end_created

    @end_created.setter
    def end_created(self, end_created):
        if isinstance(end_created, datetime):
            self._end_created = end_created
        else:
            raise TypeError("end_created must be datetime")

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
    def buyer_nick(self):
        return self._buyer_nick

    @buyer_nick.setter
    def buyer_nick(self, buyer_nick):
        if isinstance(buyer_nick, str):
            self._buyer_nick = buyer_nick
        else:
            raise TypeError("buyer_nick must be str")

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
    def ext_type(self):
        return self._ext_type

    @ext_type.setter
    def ext_type(self, ext_type):
        if isinstance(ext_type, str):
            self._ext_type = ext_type
        else:
            raise TypeError("ext_type must be str")

    @property
    def rate_status(self):
        return self._rate_status

    @rate_status.setter
    def rate_status(self, rate_status):
        if isinstance(rate_status, str):
            self._rate_status = rate_status
        else:
            raise TypeError("rate_status must be str")

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, tag):
        if isinstance(tag, str):
            self._tag = tag
        else:
            raise TypeError("tag must be str")

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

    @property
    def use_has_next(self):
        return self._use_has_next

    @use_has_next.setter
    def use_has_next(self, use_has_next):
        if isinstance(use_has_next, bool):
            self._use_has_next = use_has_next
        else:
            raise TypeError("use_has_next must be bool")


    def get_api_name(self):
        return "taobao.trades.sold.get"

    def to_dict(self):
        request_dict = {}
        if self._buyer_open_id is not None:
            request_dict["buyer_open_id"] = convert_basic(self._buyer_open_id)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._start_created is not None:
            request_dict["start_created"] = convert_basic(self._start_created)

        if self._end_created is not None:
            request_dict["end_created"] = convert_basic(self._end_created)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._buyer_nick is not None:
            request_dict["buyer_nick"] = convert_basic(self._buyer_nick)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._ext_type is not None:
            request_dict["ext_type"] = convert_basic(self._ext_type)

        if self._rate_status is not None:
            request_dict["rate_status"] = convert_basic(self._rate_status)

        if self._tag is not None:
            request_dict["tag"] = convert_basic(self._tag)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._use_has_next is not None:
            request_dict["use_has_next"] = convert_basic(self._use_has_next)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


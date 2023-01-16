from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradesSoldIncrementvGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        start_create: datetime = None,
        end_create: datetime = None,
        status: str = None,
        type: str = None,
        ext_type: str = None,
        tag: str = None,
        page_no: int = None,
        page_size: int = None,
        use_has_next: bool = None
    ):
        """
            需要返回的字段列表，多个字段用半角逗号分隔，可选值为返回示例中能看到的所有字段。
        """
        self._fields = fields
        """
            查询入库开始时间(修改时间跨度不能大于一天)。格式:yyyy-MM-dd HH:mm:ss
        """
        self._start_create = start_create
        """
            查询入库结束时间，必须大于入库开始时间(修改时间跨度不能大于一天)，格式:yyyy-MM-dd HH:mm:ss。<span style="color:red;font-weight: bold;">建议使用30分钟以内的时间跨度，能大大提高响应速度和成功率</span>。
        """
        self._end_create = end_create
        """
            交易状态（<a href="http://open.taobao.com/doc/detail.htm?id=102856" target="_blank">查看可选值</a>），默认查询所有交易状态的数据，除了默认值外每次只能查询一种状态。
        """
        self._status = status
        """
            交易类型列表（<a href="http://open.taobao.com/doc/detail.htm?id=102855" target="_blank">查看可选值</a>），一次查询多种类型可用半角逗号分隔，默认同时查询guarantee_trade,auto_delivery,ec,cod,step这5种类型的数据。
        """
        self._type = type
        """
            可选值有ershou(二手市场的订单）,service（商城服务子订单）mark（双十一大促活动异常订单）作为扩展类型筛选只能做单个ext_type查询，不能全部查询所有的ext_type类型
        """
        self._ext_type = ext_type
        """
            卖家对交易的自定义分组标签，目前可选值为：time_card（点卡软件代充），fee_card（话费软件代充）
        """
        self._tag = tag
        """
            页码。取值范围:大于零的整数;默认值:1。<span style="color:red;font-weight: bold;">注：必须采用倒序的分页方式（从最后一页往回取）才能避免漏单问题。</span>
        """
        self._page_no = page_no
        """
            每页条数。取值范围：1~100，默认值：40。<span style="color:red;font-weight: bold;">建议使用40~50，可以提高成功率，减少超时数量</span>。
        """
        self._page_size = page_size
        """
            是否启用has_next的分页方式，如果指定true,则返回的结果中不包含总记录数，但是会新增一个是否存在下一页的的字段，<span style="color:red;font-weight: bold;">通过此种方式获取增量交易，效率在原有的基础上有80%的提升</span>。
        """
        self._use_has_next = use_has_next

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
    def start_create(self):
        return self._start_create

    @start_create.setter
    def start_create(self, start_create):
        if isinstance(start_create, datetime):
            self._start_create = start_create
        else:
            raise TypeError("start_create must be datetime")

    @property
    def end_create(self):
        return self._end_create

    @end_create.setter
    def end_create(self, end_create):
        if isinstance(end_create, datetime):
            self._end_create = end_create
        else:
            raise TypeError("end_create must be datetime")

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
    def ext_type(self):
        return self._ext_type

    @ext_type.setter
    def ext_type(self, ext_type):
        if isinstance(ext_type, str):
            self._ext_type = ext_type
        else:
            raise TypeError("ext_type must be str")

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
        return "taobao.trades.sold.incrementv.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._start_create is not None:
            request_dict["start_create"] = convert_basic(self._start_create)

        if self._end_create is not None:
            request_dict["end_create"] = convert_basic(self._end_create)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._ext_type is not None:
            request_dict["ext_type"] = convert_basic(self._ext_type)

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


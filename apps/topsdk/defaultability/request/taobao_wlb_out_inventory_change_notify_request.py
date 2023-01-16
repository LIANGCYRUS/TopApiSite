from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbOutInventoryChangeNotifyRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        type: str = None,
        change_count: int = None,
        result_count: int = None,
        op_type: str = None,
        source: str = None,
        order_source_code: str = None,
        out_biz_code: str = None,
        store_code: str = None
    ):
        """
            物流宝商品id或前台宝贝id（由type类型决定）
        """
        self._item_id = item_id
        """
            WLB_ITEM--物流宝商品 IC_ITEM--淘宝商品 IC_SKU--淘宝sku
        """
        self._type = type
        """
            库存变化数量
        """
        self._change_count = change_count
        """
            本次库存变化后库存余额
        """
        self._result_count = result_count
        """
            OUT--出库 IN--入库
        """
        self._op_type = op_type
        """
            （1）OTHER： 其他 （2）TAOBAO_TRADE： 淘宝交易 （3）OTHER_TRADE：其他交易 （4）ALLCOATE： 调拨 （5）CHECK:盘点 （6）PURCHASE:采购
        """
        self._source = source
        """
            订单号，如果source为TAOBAO_TRADE,order_source_code必须为淘宝交易号
        """
        self._order_source_code = order_source_code
        """
            库存变化唯一标识，用于去重，一个外部唯一编码唯一标识一次库存变化。
        """
        self._out_biz_code = out_biz_code
        """
            目前非必须，系统会选择默认值
        """
        self._store_code = store_code

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, int):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be int")

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
    def change_count(self):
        return self._change_count

    @change_count.setter
    def change_count(self, change_count):
        if isinstance(change_count, int):
            self._change_count = change_count
        else:
            raise TypeError("change_count must be int")

    @property
    def result_count(self):
        return self._result_count

    @result_count.setter
    def result_count(self, result_count):
        if isinstance(result_count, int):
            self._result_count = result_count
        else:
            raise TypeError("result_count must be int")

    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        if isinstance(op_type, str):
            self._op_type = op_type
        else:
            raise TypeError("op_type must be str")

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        if isinstance(source, str):
            self._source = source
        else:
            raise TypeError("source must be str")

    @property
    def order_source_code(self):
        return self._order_source_code

    @order_source_code.setter
    def order_source_code(self, order_source_code):
        if isinstance(order_source_code, str):
            self._order_source_code = order_source_code
        else:
            raise TypeError("order_source_code must be str")

    @property
    def out_biz_code(self):
        return self._out_biz_code

    @out_biz_code.setter
    def out_biz_code(self, out_biz_code):
        if isinstance(out_biz_code, str):
            self._out_biz_code = out_biz_code
        else:
            raise TypeError("out_biz_code must be str")

    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, store_code):
        if isinstance(store_code, str):
            self._store_code = store_code
        else:
            raise TypeError("store_code must be str")


    def get_api_name(self):
        return "taobao.wlb.out.inventory.change.notify"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._change_count is not None:
            request_dict["change_count"] = convert_basic(self._change_count)

        if self._result_count is not None:
            request_dict["result_count"] = convert_basic(self._result_count)

        if self._op_type is not None:
            request_dict["op_type"] = convert_basic(self._op_type)

        if self._source is not None:
            request_dict["source"] = convert_basic(self._source)

        if self._order_source_code is not None:
            request_dict["order_source_code"] = convert_basic(self._order_source_code)

        if self._out_biz_code is not None:
            request_dict["out_biz_code"] = convert_basic(self._out_biz_code)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


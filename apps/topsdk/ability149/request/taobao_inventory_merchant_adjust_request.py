from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoInventoryMerchantAdjustRequest(BaseRequest):

    def __init__(
        self,
        inventory_check: object = None
    ):
        """
            调整库存对象
        """
        self._inventory_check = inventory_check

    @property
    def inventory_check(self):
        return self._inventory_check

    @inventory_check.setter
    def inventory_check(self, inventory_check):
        if isinstance(inventory_check, object):
            self._inventory_check = inventory_check
        else:
            raise TypeError("inventory_check must be object")


    def get_api_name(self):
        return "taobao.inventory.merchant.adjust"

    def to_dict(self):
        request_dict = {}
        if self._inventory_check is not None:
            request_dict["inventory_check"] = convert_struct(self._inventory_check)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoInventoryMerchantAdjustInventoryCheckDetailDto:
    def __init__(
        self,
        inv_biz_code: str = None,
        quantity: int = None,
        sc_item_id: int = None,
        sub_order_id: str = None,
        sku_id: int = None
    ):
        """
            如果是门店类型,则为必填。 ONLINE_INVENTORY  线上可售库存，  SHARE_INVENTORY 线下可售库存
        """
        self.inv_biz_code = inv_biz_code
        """
            调整数量，正数盘盈，负数盘亏
        """
        self.quantity = quantity
        """
            若为货品仓库存，则此处是货品ID 若为商品直接设置仓库存，则此处是商品ID， 若商品带SKU，还需要补充skuId
        """
        self.sc_item_id = sc_item_id
        """
            每个货品的调整子单据号，作为业务调整依据，处理时会根据此单据号作幂
        """
        self.sub_order_id = sub_order_id
        """
            调整商品对应的SKUID，如果商品为货品，则为0
        """
        self.sku_id = sku_id

class TaobaoInventoryMerchantAdjustInventoryCheckDto:
    def __init__(
        self,
        check_mode: int = None,
        inv_store_type: int = None,
        detail_list: list = None,
        store_code: str = None,
        order_id: str = None
    ):
        """
            1:全量更新   2: 出入库盘盈盘亏
        """
        self.check_mode = check_mode
        """
            2： 仓库类型   6：门店类型
        """
        self.inv_store_type = inv_store_type
        """
            调整明细
        """
        self.detail_list = detail_list
        """
            仓库code或者门店id
        """
        self.store_code = store_code
        """
            调整单据号
        """
        self.order_id = order_id


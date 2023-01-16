from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemBarcodeUpdateRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        item_barcode: str = None,
        sku_ids: str = None,
        sku_barcodes: str = None,
        isforce: bool = None,
        src: str = None
    ):
        """
            被更新商品的ID
        """
        self._item_id = item_id
        """
            商品条形码，如果不用更新，可选择不填
        """
        self._item_barcode = item_barcode
        """
            被更新SKU的ID列表，中间以英文逗号进行分隔。如果没有SKU或者不需要更新SKU的条形码，不需要设置
        """
        self._sku_ids = sku_ids
        """
            SKU维度的条形码，和sku_ids字段一一对应，中间以英文逗号分隔
        """
        self._sku_barcodes = sku_barcodes
        """
            是否强制保存商品条码。true：强制保存false ：需要执行条码库校验
        """
        self._isforce = isforce
        """
            访问来源，这字段提供给千牛扫码枪用，其他调用方，不需要填写
        """
        self._src = src

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
    def item_barcode(self):
        return self._item_barcode

    @item_barcode.setter
    def item_barcode(self, item_barcode):
        if isinstance(item_barcode, str):
            self._item_barcode = item_barcode
        else:
            raise TypeError("item_barcode must be str")

    @property
    def sku_ids(self):
        return self._sku_ids

    @sku_ids.setter
    def sku_ids(self, sku_ids):
        if isinstance(sku_ids, str):
            self._sku_ids = sku_ids
        else:
            raise TypeError("sku_ids must be str")

    @property
    def sku_barcodes(self):
        return self._sku_barcodes

    @sku_barcodes.setter
    def sku_barcodes(self, sku_barcodes):
        if isinstance(sku_barcodes, str):
            self._sku_barcodes = sku_barcodes
        else:
            raise TypeError("sku_barcodes must be str")

    @property
    def isforce(self):
        return self._isforce

    @isforce.setter
    def isforce(self, isforce):
        if isinstance(isforce, bool):
            self._isforce = isforce
        else:
            raise TypeError("isforce must be bool")

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, src):
        if isinstance(src, str):
            self._src = src
        else:
            raise TypeError("src must be str")


    def get_api_name(self):
        return "taobao.item.barcode.update"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._item_barcode is not None:
            request_dict["item_barcode"] = convert_basic(self._item_barcode)

        if self._sku_ids is not None:
            request_dict["sku_ids"] = convert_basic(self._sku_ids)

        if self._sku_barcodes is not None:
            request_dict["sku_barcodes"] = convert_basic(self._sku_barcodes)

        if self._isforce is not None:
            request_dict["isforce"] = convert_basic(self._isforce)

        if self._src is not None:
            request_dict["src"] = convert_basic(self._src)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


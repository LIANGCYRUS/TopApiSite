from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoSkusQuantityUpdateRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        skuid_quantities: str = None,
        outerid_quantities: str = None,
        type: int = None
    ):
        """
            商品数字ID，必填参数
        """
        self._num_iid = num_iid
        """
            sku库存批量修改入参，用于指定一批sku和每个sku的库存修改值，特殊可填。格式为skuId:库存修改值;skuId:库存修改值。最多支持20个SKU同时修改。
        """
        self._skuid_quantities = skuid_quantities
        """
            特殊可选，skuIdQuantities为空的时候用该字段通过outerId来指定sku和其库存修改值。格式为outerId:库存修改值;outerId:库存修改值。当skuIdQuantities不为空的时候该字段失效。当一个outerId对应多个sku时，所有匹配到的sku都会被修改库存。最多支持20个SKU同时修改。
        """
        self._outerid_quantities = outerid_quantities
        """
            库存更新方式，可选。1为全量更新，2为增量更新。如果不填，默认为全量更新。当选择全量更新时，如果库存更新值传入的是负数，会出错并返回错误码；当选择增量更新时，如果库存更新值为负数且绝对值大于当前库存，则sku库存会设置为0.
        """
        self._type = type

    @property
    def num_iid(self):
        return self._num_iid

    @num_iid.setter
    def num_iid(self, num_iid):
        if isinstance(num_iid, int):
            self._num_iid = num_iid
        else:
            raise TypeError("num_iid must be int")

    @property
    def skuid_quantities(self):
        return self._skuid_quantities

    @skuid_quantities.setter
    def skuid_quantities(self, skuid_quantities):
        if isinstance(skuid_quantities, str):
            self._skuid_quantities = skuid_quantities
        else:
            raise TypeError("skuid_quantities must be str")

    @property
    def outerid_quantities(self):
        return self._outerid_quantities

    @outerid_quantities.setter
    def outerid_quantities(self, outerid_quantities):
        if isinstance(outerid_quantities, str):
            self._outerid_quantities = outerid_quantities
        else:
            raise TypeError("outerid_quantities must be str")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")


    def get_api_name(self):
        return "taobao.skus.quantity.update"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._skuid_quantities is not None:
            request_dict["skuid_quantities"] = convert_basic(self._skuid_quantities)

        if self._outerid_quantities is not None:
            request_dict["outerid_quantities"] = convert_basic(self._outerid_quantities)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


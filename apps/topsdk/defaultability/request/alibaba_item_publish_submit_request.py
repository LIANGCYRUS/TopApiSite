from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaItemPublishSubmitRequest(BaseRequest):

    def __init__(
        self,
        biz_type: str = None,
        market: str = None,
        cat_id: int = None,
        spu_id: int = None,
        barcode: str = None,
        schema: str = None
    ):
        """
            业务扩展参数，需与平台约定好
        """
        self._biz_type = biz_type
        """
            商品发布的市场。taobao:淘宝,tmall:天猫,litetao:淘宝特价版
        """
        self._market = market
        """
            商品类目ID
        """
        self._cat_id = cat_id
        """
            产品ID，天猫市场(market=tmall)时必填
        """
        self._spu_id = spu_id
        """
            商品条码
        """
        self._barcode = barcode
        """
            商品schema信息，通过alibaba.item.publish.props.get获取并补全后提交
        """
        self._schema = schema

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, str):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be str")

    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, market):
        if isinstance(market, str):
            self._market = market
        else:
            raise TypeError("market must be str")

    @property
    def cat_id(self):
        return self._cat_id

    @cat_id.setter
    def cat_id(self, cat_id):
        if isinstance(cat_id, int):
            self._cat_id = cat_id
        else:
            raise TypeError("cat_id must be int")

    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, spu_id):
        if isinstance(spu_id, int):
            self._spu_id = spu_id
        else:
            raise TypeError("spu_id must be int")

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        if isinstance(barcode, str):
            self._barcode = barcode
        else:
            raise TypeError("barcode must be str")

    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, schema):
        if isinstance(schema, str):
            self._schema = schema
        else:
            raise TypeError("schema must be str")


    def get_api_name(self):
        return "alibaba.item.publish.submit"

    def to_dict(self):
        request_dict = {}
        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._market is not None:
            request_dict["market"] = convert_basic(self._market)

        if self._cat_id is not None:
            request_dict["cat_id"] = convert_basic(self._cat_id)

        if self._spu_id is not None:
            request_dict["spu_id"] = convert_basic(self._spu_id)

        if self._barcode is not None:
            request_dict["barcode"] = convert_basic(self._barcode)

        if self._schema is not None:
            request_dict["schema"] = convert_basic(self._schema)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


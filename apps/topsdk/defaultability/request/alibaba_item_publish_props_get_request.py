from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaItemPublishPropsGetRequest(BaseRequest):

    def __init__(
        self,
        market: str = None,
        cat_id: int = None,
        barcode: str = None,
        schema: str = None,
        prop_id: int = None
    ):
        """
            商品发布的市场。taobao:淘宝,tmall:天猫,litetao:淘宝特价版
        """
        self._market = market
        """
            商品类目ID
        """
        self._cat_id = cat_id
        """
            商品条码
        """
        self._barcode = barcode
        """
            类目属性渲染schema
        """
        self._schema = schema
        """
            属性ID
        """
        self._prop_id = prop_id

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

    @property
    def prop_id(self):
        return self._prop_id

    @prop_id.setter
    def prop_id(self, prop_id):
        if isinstance(prop_id, int):
            self._prop_id = prop_id
        else:
            raise TypeError("prop_id must be int")


    def get_api_name(self):
        return "alibaba.item.publish.props.get"

    def to_dict(self):
        request_dict = {}
        if self._market is not None:
            request_dict["market"] = convert_basic(self._market)

        if self._cat_id is not None:
            request_dict["cat_id"] = convert_basic(self._cat_id)

        if self._barcode is not None:
            request_dict["barcode"] = convert_basic(self._barcode)

        if self._schema is not None:
            request_dict["schema"] = convert_basic(self._schema)

        if self._prop_id is not None:
            request_dict["prop_id"] = convert_basic(self._prop_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


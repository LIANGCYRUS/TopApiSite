from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaItemEditSubmitRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        biz_type: str = None,
        cat_id: int = None,
        spu_id: int = None,
        schema: str = None
    ):
        """
            商品ID
        """
        self._item_id = item_id
        """
            业务扩展参数，需与平台约定好
        """
        self._biz_type = biz_type
        """
            商品类目ID。若不需要修改商品类目，则不用填写
        """
        self._cat_id = cat_id
        """
            产品ID，若不需要修改关联的产品信息，则不需要填写
        """
        self._spu_id = spu_id
        """
            编辑后的schema信息，通过alibaba.item.edit.schema.get获取
        """
        self._schema = schema

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
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, str):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be str")

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
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, schema):
        if isinstance(schema, str):
            self._schema = schema
        else:
            raise TypeError("schema must be str")


    def get_api_name(self):
        return "alibaba.item.edit.submit"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._cat_id is not None:
            request_dict["cat_id"] = convert_basic(self._cat_id)

        if self._spu_id is not None:
            request_dict["spu_id"] = convert_basic(self._spu_id)

        if self._schema is not None:
            request_dict["schema"] = convert_basic(self._schema)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


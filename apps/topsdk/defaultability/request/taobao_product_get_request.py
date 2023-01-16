from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoProductGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        product_id: int = None,
        cid: int = None,
        props: str = None
    ):
        """
            需返回的字段列表.可选值:Product数据结构中的所有字段;多个字段之间用","分隔.
        """
        self._fields = fields
        """
            Product的id.两种方式来查看一个产品:1.传入product_id来查询 2.传入cid和props来查询
        """
        self._product_id = product_id
        """
            商品类目id.调用taobao.itemcats.get获取;必须是叶子类目id,如果没有传product_id,那么cid和props必须要传.
        """
        self._cid = cid
        """
            比如:诺基亚N73这个产品的关键属性列表就是:品牌:诺基亚;型号:N73,对应的PV值就是10005:10027;10006:29729.
        """
        self._props = props

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
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self._product_id = product_id
        else:
            raise TypeError("product_id must be int")

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, cid):
        if isinstance(cid, int):
            self._cid = cid
        else:
            raise TypeError("cid must be int")

    @property
    def props(self):
        return self._props

    @props.setter
    def props(self, props):
        if isinstance(props, str):
            self._props = props
        else:
            raise TypeError("props must be str")


    def get_api_name(self):
        return "taobao.product.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._props is not None:
            request_dict["props"] = convert_basic(self._props)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


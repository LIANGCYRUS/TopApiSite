from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemcatsGetRequest(BaseRequest):

    def __init__(
        self,
        cids: list = None,
        datetime: datetime = None,
        fields: list = None,
        parent_cid: int = None
    ):
        """
            商品所属类目ID列表，用半角逗号(,)分隔 例如:(18957,19562,) (cids、parent_cid至少传一个)
        """
        self._cids = cids
        """
            无效字段，暂无法使用。时间戳（格式:yyyy-MM-dd HH:mm:ss）如果该字段没有传，则取当前所有的类目信息,如果传了parent_cid或者cids，则忽略datetime，如果该字段传了，那么可以查询到该时间到现在为止的增量变化
        """
        self._datetime = datetime
        """
            需要返回的字段列表，见ItemCat，默认返回：cid,parent_cid,name,is_parent；增量类目信息,根据fields传入的参数返回相应的结果。 features字段： 1、如果存在attr_key=freeze表示该类目被冻结了，attr_value=0,5，value可能存在2个值（也可能只有1个），用逗号分割，0表示禁编辑，5表示禁止发布
        """
        self._fields = fields
        """
            父商品类目 id，0表示根节点, 传输该参数返回所有子类目。 (cids、parent_cid至少传一个)
        """
        self._parent_cid = parent_cid

    @property
    def cids(self):
        return self._cids

    @cids.setter
    def cids(self, cids):
        if isinstance(cids, list):
            self._cids = cids
        else:
            raise TypeError("cids must be list")

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        if isinstance(datetime, datetime):
            self._datetime = datetime
        else:
            raise TypeError("datetime must be datetime")

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
    def parent_cid(self):
        return self._parent_cid

    @parent_cid.setter
    def parent_cid(self, parent_cid):
        if isinstance(parent_cid, int):
            self._parent_cid = parent_cid
        else:
            raise TypeError("parent_cid must be int")


    def get_api_name(self):
        return "taobao.itemcats.get"

    def to_dict(self):
        request_dict = {}
        if self._cids is not None:
            request_dict["cids"] = convert_basic_list(self._cids)

        if self._datetime is not None:
            request_dict["datetime"] = convert_basic(self._datetime)

        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._parent_cid is not None:
            request_dict["parent_cid"] = convert_basic(self._parent_cid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


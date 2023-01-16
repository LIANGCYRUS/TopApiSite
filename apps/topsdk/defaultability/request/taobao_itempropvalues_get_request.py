from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItempropvaluesGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        pvs: str = None,
        cid: int = None,
        datetime: datetime = None,
        type: int = None,
        attr_keys: list = None
    ):
        """
            需要返回的字段。目前支持有：cid,pid,prop_name,vid,name,name_alias,status,sort_order
        """
        self._fields = fields
        """
            属性和属性值 id串，格式例如(pid1;pid2)或(pid1:vid1;pid2:vid2)或(pid1;pid2:vid2)
        """
        self._pvs = pvs
        """
            叶子类目ID ,通过taobao.itemcats.get获得叶子类目ID
        """
        self._cid = cid
        """
            假如传2005-01-01 00:00:00，则取所有的属性和子属性(状态为删除的属性值不返回prop_name)
        """
        self._datetime = datetime
        """
            获取类目的类型：1代表集市、2代表天猫
        """
        self._type = type
        """
            属性的Key，支持多条，以“,”分隔
        """
        self._attr_keys = attr_keys

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
    def pvs(self):
        return self._pvs

    @pvs.setter
    def pvs(self, pvs):
        if isinstance(pvs, str):
            self._pvs = pvs
        else:
            raise TypeError("pvs must be str")

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
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        if isinstance(datetime, datetime):
            self._datetime = datetime
        else:
            raise TypeError("datetime must be datetime")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")

    @property
    def attr_keys(self):
        return self._attr_keys

    @attr_keys.setter
    def attr_keys(self, attr_keys):
        if isinstance(attr_keys, list):
            self._attr_keys = attr_keys
        else:
            raise TypeError("attr_keys must be list")


    def get_api_name(self):
        return "taobao.itempropvalues.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._pvs is not None:
            request_dict["pvs"] = convert_basic(self._pvs)

        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._datetime is not None:
            request_dict["datetime"] = convert_basic(self._datetime)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._attr_keys is not None:
            request_dict["attr_keys"] = convert_basic_list(self._attr_keys)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


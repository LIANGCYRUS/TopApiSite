from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItempropsGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        cid: int = None,
        pid: int = None,
        parent_pid: int = None,
        is_key_prop: bool = None,
        is_sale_prop: bool = None,
        is_color_prop: bool = None,
        is_enum_prop: bool = None,
        is_input_prop: bool = None,
        is_item_prop: bool = None,
        datetime: datetime = None,
        child_path: str = None,
        type: int = None,
        attr_keys: list = None
    ):
        """
            需要返回的字段列表，见：ItemProp，默认返回：pid, name, must, multi, prop_values
        """
        self._fields = fields
        """
            叶子类目ID，如果只传cid，则只返回一级属性,通过taobao.itemcats.get获得叶子类目ID
        """
        self._cid = cid
        """
            属性id (取类目属性时，传pid，不用同时传PID和parent_pid)
        """
        self._pid = pid
        """
            父属性ID
        """
        self._parent_pid = parent_pid
        """
            是否关键属性。可选值:true(是),false(否)
        """
        self._is_key_prop = is_key_prop
        """
            是否销售属性。可选值:true(是),false(否)
        """
        self._is_sale_prop = is_sale_prop
        """
            是否颜色属性。可选值:true(是),false(否) (删除的属性不会匹配和返回这个条件)
        """
        self._is_color_prop = is_color_prop
        """
            是否枚举属性。可选值:true(是),false(否) (删除的属性不会匹配和返回这个条件)。如果返回true，属性值是下拉框选择输入，如果返回false，属性值是用户自行手工输入。
        """
        self._is_enum_prop = is_enum_prop
        """
            在is_enum_prop是true的前提下，是否是卖家可以自行输入的属性（注：如果is_enum_prop返回false，该参数统一返回false）。可选值:true(是),false(否) (删除的属性不会匹配和返回这个条件)
        """
        self._is_input_prop = is_input_prop
        """
            是否商品属性，这个属性只能放于发布商品时使用。可选值:true(是),false(否)
        """
        self._is_item_prop = is_item_prop
        """
            增量时间戳。格式:yyyy-MM-dd HH:mm:ss假如传2005-01-01 00:00:00，则取所有的属性和子属性ID(如果传了pid会忽略datetime)
        """
        self._datetime = datetime
        """
            类目子属性路径,由该子属性上层的类目属性和类目属性值组成,格式pid:vid;pid:vid.取类目子属性需要传child_path,cid
        """
        self._child_path = child_path
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
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, cid):
        if isinstance(cid, int):
            self._cid = cid
        else:
            raise TypeError("cid must be int")

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, pid):
        if isinstance(pid, int):
            self._pid = pid
        else:
            raise TypeError("pid must be int")

    @property
    def parent_pid(self):
        return self._parent_pid

    @parent_pid.setter
    def parent_pid(self, parent_pid):
        if isinstance(parent_pid, int):
            self._parent_pid = parent_pid
        else:
            raise TypeError("parent_pid must be int")

    @property
    def is_key_prop(self):
        return self._is_key_prop

    @is_key_prop.setter
    def is_key_prop(self, is_key_prop):
        if isinstance(is_key_prop, bool):
            self._is_key_prop = is_key_prop
        else:
            raise TypeError("is_key_prop must be bool")

    @property
    def is_sale_prop(self):
        return self._is_sale_prop

    @is_sale_prop.setter
    def is_sale_prop(self, is_sale_prop):
        if isinstance(is_sale_prop, bool):
            self._is_sale_prop = is_sale_prop
        else:
            raise TypeError("is_sale_prop must be bool")

    @property
    def is_color_prop(self):
        return self._is_color_prop

    @is_color_prop.setter
    def is_color_prop(self, is_color_prop):
        if isinstance(is_color_prop, bool):
            self._is_color_prop = is_color_prop
        else:
            raise TypeError("is_color_prop must be bool")

    @property
    def is_enum_prop(self):
        return self._is_enum_prop

    @is_enum_prop.setter
    def is_enum_prop(self, is_enum_prop):
        if isinstance(is_enum_prop, bool):
            self._is_enum_prop = is_enum_prop
        else:
            raise TypeError("is_enum_prop must be bool")

    @property
    def is_input_prop(self):
        return self._is_input_prop

    @is_input_prop.setter
    def is_input_prop(self, is_input_prop):
        if isinstance(is_input_prop, bool):
            self._is_input_prop = is_input_prop
        else:
            raise TypeError("is_input_prop must be bool")

    @property
    def is_item_prop(self):
        return self._is_item_prop

    @is_item_prop.setter
    def is_item_prop(self, is_item_prop):
        if isinstance(is_item_prop, bool):
            self._is_item_prop = is_item_prop
        else:
            raise TypeError("is_item_prop must be bool")

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
    def child_path(self):
        return self._child_path

    @child_path.setter
    def child_path(self, child_path):
        if isinstance(child_path, str):
            self._child_path = child_path
        else:
            raise TypeError("child_path must be str")

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
        return "taobao.itemprops.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._pid is not None:
            request_dict["pid"] = convert_basic(self._pid)

        if self._parent_pid is not None:
            request_dict["parent_pid"] = convert_basic(self._parent_pid)

        if self._is_key_prop is not None:
            request_dict["is_key_prop"] = convert_basic(self._is_key_prop)

        if self._is_sale_prop is not None:
            request_dict["is_sale_prop"] = convert_basic(self._is_sale_prop)

        if self._is_color_prop is not None:
            request_dict["is_color_prop"] = convert_basic(self._is_color_prop)

        if self._is_enum_prop is not None:
            request_dict["is_enum_prop"] = convert_basic(self._is_enum_prop)

        if self._is_input_prop is not None:
            request_dict["is_input_prop"] = convert_basic(self._is_input_prop)

        if self._is_item_prop is not None:
            request_dict["is_item_prop"] = convert_basic(self._is_item_prop)

        if self._datetime is not None:
            request_dict["datetime"] = convert_basic(self._datetime)

        if self._child_path is not None:
            request_dict["child_path"] = convert_basic(self._child_path)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._attr_keys is not None:
            request_dict["attr_keys"] = convert_basic_list(self._attr_keys)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


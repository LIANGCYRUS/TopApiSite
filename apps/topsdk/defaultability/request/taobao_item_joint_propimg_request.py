from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemJointPropimgRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        properties: str = None,
        id: int = None,
        position: int = None,
        pic_path: str = None
    ):
        """
            商品数字ID，必选
        """
        self._num_iid = num_iid
        """
            属性列表。调用taobao.itemprops.get获取，属性必须是颜色属性，格式:pid:vid。
        """
        self._properties = properties
        """
            属性图片ID。如果是新增不需要填写
        """
        self._id = id
        """
            图片序号
        """
        self._position = position
        """
            图片地址(传入图片相对地址即可,即不需包含 http://img02.taobao.net/bao/uploaded )
        """
        self._pic_path = pic_path

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
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, properties):
        if isinstance(properties, str):
            self._properties = properties
        else:
            raise TypeError("properties must be str")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise TypeError("id must be int")

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, int):
            self._position = position
        else:
            raise TypeError("position must be int")

    @property
    def pic_path(self):
        return self._pic_path

    @pic_path.setter
    def pic_path(self, pic_path):
        if isinstance(pic_path, str):
            self._pic_path = pic_path
        else:
            raise TypeError("pic_path must be str")


    def get_api_name(self):
        return "taobao.item.joint.propimg"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        if self._id is not None:
            request_dict["id"] = convert_basic(self._id)

        if self._position is not None:
            request_dict["position"] = convert_basic(self._position)

        if self._pic_path is not None:
            request_dict["pic_path"] = convert_basic(self._pic_path)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


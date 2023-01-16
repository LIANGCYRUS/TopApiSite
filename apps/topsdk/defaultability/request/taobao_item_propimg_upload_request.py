from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemPropimgUploadRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        id: int = None,
        properties: str = None,
        position: int = None,
        image: bytes = None
    ):
        """
            商品数字ID，必选
        """
        self._num_iid = num_iid
        """
            属性图片ID。如果是新增不需要填写
        """
        self._id = id
        """
            属性列表。调用taobao.itemprops.get获取类目属性，属性必须是颜色属性，再用taobao.itempropvalues.get取得vid。格式:pid:vid。
        """
        self._properties = properties
        """
            图片位置
        """
        self._position = position
        """
            属性图片内容。类型:JPG,GIF;图片大小不超过:3M
        """
        self._image = image

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
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
        else:
            raise TypeError("id must be int")

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
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if isinstance(position, int):
            self._position = position
        else:
            raise TypeError("position must be int")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        if isinstance(image, bytes):
            self._image = image
        else:
            raise TypeError("image must be bytes")


    def get_api_name(self):
        return "taobao.item.propimg.upload"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._id is not None:
            request_dict["id"] = convert_basic(self._id)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        if self._position is not None:
            request_dict["position"] = convert_basic(self._position)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


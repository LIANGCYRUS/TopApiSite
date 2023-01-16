from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemJointImgRequest(BaseRequest):

    def __init__(
        self,
        num_iid: int = None,
        id: int = None,
        position: int = None,
        pic_path: str = None,
        is_major: bool = None,
        is_rectangle: bool = None
    ):
        """
            商品数字ID，必选
        """
        self._num_iid = num_iid
        """
            商品图片id(如果是更新图片，则需要传该参数)
        """
        self._id = id
        """
            图片序号
        """
        self._position = position
        """
            图片URL,图片空间图片的相对地址，支持的文件类型：jpg,jpeg,png
        """
        self._pic_path = pic_path
        """
            上传的图片是否关联为商品主图
        """
        self._is_major = is_major
        """
            是否3:4长方形图片，绑定3:4主图视频时用于上传3:4商品主图
        """
        self._is_rectangle = is_rectangle

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

    @property
    def is_major(self):
        return self._is_major

    @is_major.setter
    def is_major(self, is_major):
        if isinstance(is_major, bool):
            self._is_major = is_major
        else:
            raise TypeError("is_major must be bool")

    @property
    def is_rectangle(self):
        return self._is_rectangle

    @is_rectangle.setter
    def is_rectangle(self, is_rectangle):
        if isinstance(is_rectangle, bool):
            self._is_rectangle = is_rectangle
        else:
            raise TypeError("is_rectangle must be bool")


    def get_api_name(self):
        return "taobao.item.joint.img"

    def to_dict(self):
        request_dict = {}
        if self._num_iid is not None:
            request_dict["num_iid"] = convert_basic(self._num_iid)

        if self._id is not None:
            request_dict["id"] = convert_basic(self._id)

        if self._position is not None:
            request_dict["position"] = convert_basic(self._position)

        if self._pic_path is not None:
            request_dict["pic_path"] = convert_basic(self._pic_path)

        if self._is_major is not None:
            request_dict["is_major"] = convert_basic(self._is_major)

        if self._is_rectangle is not None:
            request_dict["is_rectangle"] = convert_basic(self._is_rectangle)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


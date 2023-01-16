from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoProductImgUploadRequest(BaseRequest):

    def __init__(
        self,
        id: int = None,
        product_id: int = None,
        image: bytes = None,
        position: int = None,
        is_major: bool = None
    ):
        """
            产品图片ID.修改图片时需要传入
        """
        self._id = id
        """
            产品ID.Product的id
        """
        self._product_id = product_id
        """
            图片内容.图片最大为500K,只支持JPG,GIF格式.
        """
        self._image = image
        """
            图片序号
        """
        self._position = position
        """
            是否将该图片设为主图.可选值:true,false;默认值:false.
        """
        self._is_major = is_major

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
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self._product_id = product_id
        else:
            raise TypeError("product_id must be int")

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        if isinstance(image, bytes):
            self._image = image
        else:
            raise TypeError("image must be bytes")

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
    def is_major(self):
        return self._is_major

    @is_major.setter
    def is_major(self, is_major):
        if isinstance(is_major, bool):
            self._is_major = is_major
        else:
            raise TypeError("is_major must be bool")


    def get_api_name(self):
        return "taobao.product.img.upload"

    def to_dict(self):
        request_dict = {}
        if self._id is not None:
            request_dict["id"] = convert_basic(self._id)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._position is not None:
            request_dict["position"] = convert_basic(self._position)

        if self._is_major is not None:
            request_dict["is_major"] = convert_basic(self._is_major)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoProductPropimgUploadRequest(BaseRequest):

    def __init__(
        self,
        id: int = None,
        product_id: int = None,
        props: str = None,
        image: bytes = None,
        position: int = None
    ):
        """
            产品属性图片ID
        """
        self._id = id
        """
            产品ID.Product的id
        """
        self._product_id = product_id
        """
            属性串.目前仅支持颜色属性.调用taobao.itemprops.get获取类目属性,取得颜色属性pid,再用taobao.itempropvalues.get取得vid;格式:pid:vid,只能传入一个颜色pid:vid串;
        """
        self._props = props
        """
            图片内容.图片最大为2M,只支持JPG,GIF.
        """
        self._image = image
        """
            图片序号
        """
        self._position = position

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
    def props(self):
        return self._props

    @props.setter
    def props(self, props):
        if isinstance(props, str):
            self._props = props
        else:
            raise TypeError("props must be str")

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


    def get_api_name(self):
        return "taobao.product.propimg.upload"

    def to_dict(self):
        request_dict = {}
        if self._id is not None:
            request_dict["id"] = convert_basic(self._id)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._props is not None:
            request_dict["props"] = convert_basic(self._props)

        if self._position is not None:
            request_dict["position"] = convert_basic(self._position)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


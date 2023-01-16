from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoProductUpdateRequest(BaseRequest):

    def __init__(
        self,
        product_id: int = None,
        outer_id: str = None,
        binds: str = None,
        sale_props: str = None,
        name: str = None,
        price: str = None,
        desc: str = None,
        major: bool = None,
        native_unkeyprops: str = None,
        image: bytes = None
    ):
        """
            产品ID
        """
        self._product_id = product_id
        """
            外部产品ID
        """
        self._outer_id = outer_id
        """
            非关键属性.调用taobao.itemprops.get获取pid,调用taobao.itempropvalues.get获取vid;格式:pid:vid;pid:vid
        """
        self._binds = binds
        """
            销售属性.调用taobao.itemprops.get获取pid,调用taobao.itempropvalues.get获取vid;格式:pid:vid;pid:vid
        """
        self._sale_props = sale_props
        """
            产品名称.最大不超过30个字符
        """
        self._name = name
        """
            产品市场价.精确到2位小数;单位为元.如:200.07
        """
        self._price = price
        """
            产品描述.最大不超过25000个字符
        """
        self._desc = desc
        """
            是否是主图
        """
        self._major = major
        """
            自定义非关键属性
        """
        self._native_unkeyprops = native_unkeyprops
        """
            产品主图.最大500K,目前仅支持GIF,JPG
        """
        self._image = image

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
    def outer_id(self):
        return self._outer_id

    @outer_id.setter
    def outer_id(self, outer_id):
        if isinstance(outer_id, str):
            self._outer_id = outer_id
        else:
            raise TypeError("outer_id must be str")

    @property
    def binds(self):
        return self._binds

    @binds.setter
    def binds(self, binds):
        if isinstance(binds, str):
            self._binds = binds
        else:
            raise TypeError("binds must be str")

    @property
    def sale_props(self):
        return self._sale_props

    @sale_props.setter
    def sale_props(self, sale_props):
        if isinstance(sale_props, str):
            self._sale_props = sale_props
        else:
            raise TypeError("sale_props must be str")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, str):
            self._price = price
        else:
            raise TypeError("price must be str")

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, desc):
        if isinstance(desc, str):
            self._desc = desc
        else:
            raise TypeError("desc must be str")

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        if isinstance(major, bool):
            self._major = major
        else:
            raise TypeError("major must be bool")

    @property
    def native_unkeyprops(self):
        return self._native_unkeyprops

    @native_unkeyprops.setter
    def native_unkeyprops(self, native_unkeyprops):
        if isinstance(native_unkeyprops, str):
            self._native_unkeyprops = native_unkeyprops
        else:
            raise TypeError("native_unkeyprops must be str")

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
        return "taobao.product.update"

    def to_dict(self):
        request_dict = {}
        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._binds is not None:
            request_dict["binds"] = convert_basic(self._binds)

        if self._sale_props is not None:
            request_dict["sale_props"] = convert_basic(self._sale_props)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._price is not None:
            request_dict["price"] = convert_basic(self._price)

        if self._desc is not None:
            request_dict["desc"] = convert_basic(self._desc)

        if self._major is not None:
            request_dict["major"] = convert_basic(self._major)

        if self._native_unkeyprops is not None:
            request_dict["native_unkeyprops"] = convert_basic(self._native_unkeyprops)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


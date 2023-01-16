from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbItemUpdateRequest(BaseRequest):

    def __init__(
        self,
        id: int = None,
        name: str = None,
        title: str = None,
        remark: str = None,
        update_property_key_list: list = None,
        update_property_value_list: list = None,
        delete_property_key_list: list = None,
        is_friable: bool = None,
        is_dangerous: bool = None,
        color: str = None,
        weight: int = None,
        length: int = None,
        width: int = None,
        height: int = None,
        volume: int = None,
        goods_cat: str = None,
        pricing_cat: str = None,
        package_material: str = None
    ):
        """
            要修改的商品id
        """
        self._id = id
        """
            要修改的商品名称
        """
        self._name = name
        """
            要修改的商品标题
        """
        self._title = title
        """
            要修改的商品备注
        """
        self._remark = remark
        """
            需要修改的商品属性值的列表，如果属性不存在，则新增属性
        """
        self._update_property_key_list = update_property_key_list
        """
            需要修改的属性值的列表
        """
        self._update_property_value_list = update_property_value_list
        """
            需要删除的商品属性key列表
        """
        self._delete_property_key_list = delete_property_key_list
        """
            是否易碎品
        """
        self._is_friable = is_friable
        """
            是否危险品
        """
        self._is_dangerous = is_dangerous
        """
            商品颜色
        """
        self._color = color
        """
            商品重量，单位G
        """
        self._weight = weight
        """
            商品长度，单位厘米
        """
        self._length = length
        """
            商品宽度，单位厘米
        """
        self._width = width
        """
            商品高度，单位厘米
        """
        self._height = height
        """
            商品体积，单位立方厘米
        """
        self._volume = volume
        """
            商品货类
        """
        self._goods_cat = goods_cat
        """
            商品计价货类
        """
        self._pricing_cat = pricing_cat
        """
            商品包装材料类型
        """
        self._package_material = package_material

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise TypeError("title must be str")

    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, remark):
        if isinstance(remark, str):
            self._remark = remark
        else:
            raise TypeError("remark must be str")

    @property
    def update_property_key_list(self):
        return self._update_property_key_list

    @update_property_key_list.setter
    def update_property_key_list(self, update_property_key_list):
        if isinstance(update_property_key_list, list):
            self._update_property_key_list = update_property_key_list
        else:
            raise TypeError("update_property_key_list must be list")

    @property
    def update_property_value_list(self):
        return self._update_property_value_list

    @update_property_value_list.setter
    def update_property_value_list(self, update_property_value_list):
        if isinstance(update_property_value_list, list):
            self._update_property_value_list = update_property_value_list
        else:
            raise TypeError("update_property_value_list must be list")

    @property
    def delete_property_key_list(self):
        return self._delete_property_key_list

    @delete_property_key_list.setter
    def delete_property_key_list(self, delete_property_key_list):
        if isinstance(delete_property_key_list, list):
            self._delete_property_key_list = delete_property_key_list
        else:
            raise TypeError("delete_property_key_list must be list")

    @property
    def is_friable(self):
        return self._is_friable

    @is_friable.setter
    def is_friable(self, is_friable):
        if isinstance(is_friable, bool):
            self._is_friable = is_friable
        else:
            raise TypeError("is_friable must be bool")

    @property
    def is_dangerous(self):
        return self._is_dangerous

    @is_dangerous.setter
    def is_dangerous(self, is_dangerous):
        if isinstance(is_dangerous, bool):
            self._is_dangerous = is_dangerous
        else:
            raise TypeError("is_dangerous must be bool")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            raise TypeError("color must be str")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, int):
            self._weight = weight
        else:
            raise TypeError("weight must be int")

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if isinstance(length, int):
            self._length = length
        else:
            raise TypeError("length must be int")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if isinstance(width, int):
            self._width = width
        else:
            raise TypeError("width must be int")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            self._height = height
        else:
            raise TypeError("height must be int")

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if isinstance(volume, int):
            self._volume = volume
        else:
            raise TypeError("volume must be int")

    @property
    def goods_cat(self):
        return self._goods_cat

    @goods_cat.setter
    def goods_cat(self, goods_cat):
        if isinstance(goods_cat, str):
            self._goods_cat = goods_cat
        else:
            raise TypeError("goods_cat must be str")

    @property
    def pricing_cat(self):
        return self._pricing_cat

    @pricing_cat.setter
    def pricing_cat(self, pricing_cat):
        if isinstance(pricing_cat, str):
            self._pricing_cat = pricing_cat
        else:
            raise TypeError("pricing_cat must be str")

    @property
    def package_material(self):
        return self._package_material

    @package_material.setter
    def package_material(self, package_material):
        if isinstance(package_material, str):
            self._package_material = package_material
        else:
            raise TypeError("package_material must be str")


    def get_api_name(self):
        return "taobao.wlb.item.update"

    def to_dict(self):
        request_dict = {}
        if self._id is not None:
            request_dict["id"] = convert_basic(self._id)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._title is not None:
            request_dict["title"] = convert_basic(self._title)

        if self._remark is not None:
            request_dict["remark"] = convert_basic(self._remark)

        if self._update_property_key_list is not None:
            request_dict["update_property_key_list"] = convert_basic_list(self._update_property_key_list)

        if self._update_property_value_list is not None:
            request_dict["update_property_value_list"] = convert_basic_list(self._update_property_value_list)

        if self._delete_property_key_list is not None:
            request_dict["delete_property_key_list"] = convert_basic_list(self._delete_property_key_list)

        if self._is_friable is not None:
            request_dict["is_friable"] = convert_basic(self._is_friable)

        if self._is_dangerous is not None:
            request_dict["is_dangerous"] = convert_basic(self._is_dangerous)

        if self._color is not None:
            request_dict["color"] = convert_basic(self._color)

        if self._weight is not None:
            request_dict["weight"] = convert_basic(self._weight)

        if self._length is not None:
            request_dict["length"] = convert_basic(self._length)

        if self._width is not None:
            request_dict["width"] = convert_basic(self._width)

        if self._height is not None:
            request_dict["height"] = convert_basic(self._height)

        if self._volume is not None:
            request_dict["volume"] = convert_basic(self._volume)

        if self._goods_cat is not None:
            request_dict["goods_cat"] = convert_basic(self._goods_cat)

        if self._pricing_cat is not None:
            request_dict["pricing_cat"] = convert_basic(self._pricing_cat)

        if self._package_material is not None:
            request_dict["package_material"] = convert_basic(self._package_material)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoScitemAddRequest(BaseRequest):

    def __init__(
        self,
        item_name: str = None,
        outer_code: str = None,
        item_type: int = None,
        properties: str = None,
        bar_code: str = None,
        wms_code: str = None,
        is_friable: int = None,
        is_dangerous: int = None,
        is_costly: int = None,
        is_warranty: int = None,
        weight: int = None,
        length: int = None,
        width: int = None,
        height: int = None,
        volume: int = None,
        price: int = None,
        remark: str = None,
        matter_status: int = None,
        brand_id: int = None,
        brand_name: str = None,
        spu_id: int = None,
        is_area_sale: int = None
    ):
        """
            商品名称
        """
        self._item_name = item_name
        """
            商家编码
        """
        self._outer_code = outer_code
        """
            0.普通供应链商品 1.供应链组合主商品
        """
        self._item_type = item_type
        """
            商品属性格式是  p1:v1,p2:v2,p3:v3
        """
        self._properties = properties
        """
            条形码
        """
        self._bar_code = bar_code
        """
            仓储商编码
        """
        self._wms_code = wms_code
        """
            是否易碎 0：不是  1：是
        """
        self._is_friable = is_friable
        """
            是否危险 0：不是  1：是
        """
        self._is_dangerous = is_dangerous
        """
            是否是贵重品 0:不是 1：是
        """
        self._is_costly = is_costly
        """
            是否保质期：0:不是 1：是
        """
        self._is_warranty = is_warranty
        """
            重量 单位：g
        """
        self._weight = weight
        """
            长度 单位：mm
        """
        self._length = length
        """
            宽 单位：mm
        """
        self._width = width
        """
            高 单位：mm
        """
        self._height = height
        """
            体积：立方厘米
        """
        self._volume = volume
        """
            价格 单位：分
        """
        self._price = price
        """
            remark
        """
        self._remark = remark
        """
            0:液体，1：粉体，2：固体
        """
        self._matter_status = matter_status
        """
            品牌id
        """
        self._brand_id = brand_id
        """
            brand_Name
        """
        self._brand_name = brand_name
        """
            spuId或是cspuid
        """
        self._spu_id = spu_id
        """
            1表示区域销售，0或是空是非区域销售
        """
        self._is_area_sale = is_area_sale

    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, item_name):
        if isinstance(item_name, str):
            self._item_name = item_name
        else:
            raise TypeError("item_name must be str")

    @property
    def outer_code(self):
        return self._outer_code

    @outer_code.setter
    def outer_code(self, outer_code):
        if isinstance(outer_code, str):
            self._outer_code = outer_code
        else:
            raise TypeError("outer_code must be str")

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        if isinstance(item_type, int):
            self._item_type = item_type
        else:
            raise TypeError("item_type must be int")

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
    def bar_code(self):
        return self._bar_code

    @bar_code.setter
    def bar_code(self, bar_code):
        if isinstance(bar_code, str):
            self._bar_code = bar_code
        else:
            raise TypeError("bar_code must be str")

    @property
    def wms_code(self):
        return self._wms_code

    @wms_code.setter
    def wms_code(self, wms_code):
        if isinstance(wms_code, str):
            self._wms_code = wms_code
        else:
            raise TypeError("wms_code must be str")

    @property
    def is_friable(self):
        return self._is_friable

    @is_friable.setter
    def is_friable(self, is_friable):
        if isinstance(is_friable, int):
            self._is_friable = is_friable
        else:
            raise TypeError("is_friable must be int")

    @property
    def is_dangerous(self):
        return self._is_dangerous

    @is_dangerous.setter
    def is_dangerous(self, is_dangerous):
        if isinstance(is_dangerous, int):
            self._is_dangerous = is_dangerous
        else:
            raise TypeError("is_dangerous must be int")

    @property
    def is_costly(self):
        return self._is_costly

    @is_costly.setter
    def is_costly(self, is_costly):
        if isinstance(is_costly, int):
            self._is_costly = is_costly
        else:
            raise TypeError("is_costly must be int")

    @property
    def is_warranty(self):
        return self._is_warranty

    @is_warranty.setter
    def is_warranty(self, is_warranty):
        if isinstance(is_warranty, int):
            self._is_warranty = is_warranty
        else:
            raise TypeError("is_warranty must be int")

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
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int):
            self._price = price
        else:
            raise TypeError("price must be int")

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
    def matter_status(self):
        return self._matter_status

    @matter_status.setter
    def matter_status(self, matter_status):
        if isinstance(matter_status, int):
            self._matter_status = matter_status
        else:
            raise TypeError("matter_status must be int")

    @property
    def brand_id(self):
        return self._brand_id

    @brand_id.setter
    def brand_id(self, brand_id):
        if isinstance(brand_id, int):
            self._brand_id = brand_id
        else:
            raise TypeError("brand_id must be int")

    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        if isinstance(brand_name, str):
            self._brand_name = brand_name
        else:
            raise TypeError("brand_name must be str")

    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, spu_id):
        if isinstance(spu_id, int):
            self._spu_id = spu_id
        else:
            raise TypeError("spu_id must be int")

    @property
    def is_area_sale(self):
        return self._is_area_sale

    @is_area_sale.setter
    def is_area_sale(self, is_area_sale):
        if isinstance(is_area_sale, int):
            self._is_area_sale = is_area_sale
        else:
            raise TypeError("is_area_sale must be int")


    def get_api_name(self):
        return "taobao.scitem.add"

    def to_dict(self):
        request_dict = {}
        if self._item_name is not None:
            request_dict["item_name"] = convert_basic(self._item_name)

        if self._outer_code is not None:
            request_dict["outer_code"] = convert_basic(self._outer_code)

        if self._item_type is not None:
            request_dict["item_type"] = convert_basic(self._item_type)

        if self._properties is not None:
            request_dict["properties"] = convert_basic(self._properties)

        if self._bar_code is not None:
            request_dict["bar_code"] = convert_basic(self._bar_code)

        if self._wms_code is not None:
            request_dict["wms_code"] = convert_basic(self._wms_code)

        if self._is_friable is not None:
            request_dict["is_friable"] = convert_basic(self._is_friable)

        if self._is_dangerous is not None:
            request_dict["is_dangerous"] = convert_basic(self._is_dangerous)

        if self._is_costly is not None:
            request_dict["is_costly"] = convert_basic(self._is_costly)

        if self._is_warranty is not None:
            request_dict["is_warranty"] = convert_basic(self._is_warranty)

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

        if self._price is not None:
            request_dict["price"] = convert_basic(self._price)

        if self._remark is not None:
            request_dict["remark"] = convert_basic(self._remark)

        if self._matter_status is not None:
            request_dict["matter_status"] = convert_basic(self._matter_status)

        if self._brand_id is not None:
            request_dict["brand_id"] = convert_basic(self._brand_id)

        if self._brand_name is not None:
            request_dict["brand_name"] = convert_basic(self._brand_name)

        if self._spu_id is not None:
            request_dict["spu_id"] = convert_basic(self._spu_id)

        if self._is_area_sale is not None:
            request_dict["is_area_sale"] = convert_basic(self._is_area_sale)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


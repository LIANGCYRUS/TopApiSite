from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoWlbWmsSkuCreateRequest(BaseRequest):

    def __init__(
        self,
        is_sn_mgt: bool = None,
        lifecycle: int = None,
        is_shelflife: bool = None,
        approval_number: str = None,
        origin_address: int = None,
        gross_weight: int = None,
        size: str = None,
        color: str = None,
        specification: str = None,
        brand_name: str = None,
        brand: str = None,
        category_name: str = None,
        category: str = None,
        type: str = None,
        title: str = None,
        name: str = None,
        bar_code: str = None,
        item_code: str = None,
        pcs: int = None,
        volume: int = None,
        height: int = None,
        extend_fields: str = None,
        use_yn: bool = None,
        is_batch_mgt: bool = None,
        cost_price: int = None,
        item_price: int = None,
        tag_price: int = None,
        is_danger: bool = None,
        is_hygroscopic: bool = None,
        width: int = None,
        length: int = None,
        net_weight: int = None,
        store_code: str = None,
        advent_lifecycle: int = None,
        reject_lifecycle: int = None,
        lockup_lifecycle: int = None,
        item_id: str = None,
        is_area_sale: bool = None
    ):
        """
            是否启用序列号管理
        """
        self._is_sn_mgt = is_sn_mgt
        """
            商品保质期天数
        """
        self._lifecycle = lifecycle
        """
            是否启用保质期管理
        """
        self._is_shelflife = is_shelflife
        """
            批准文号
        """
        self._approval_number = approval_number
        """
            产地
        """
        self._origin_address = origin_address
        """
            毛重，单位克
        """
        self._gross_weight = gross_weight
        """
            尺码
        """
        self._size = size
        """
            颜色
        """
        self._color = color
        """
            规格
        """
        self._specification = specification
        """
            品牌名称
        """
        self._brand_name = brand_name
        """
            品牌编码
        """
        self._brand = brand
        """
            商品类别名称
        """
        self._category_name = category_name
        """
            商品类别编码（外部系统类别）
        """
        self._category = category
        """
            商品类别NORMAL：普通商品、COMBINE：组合商品、DISTRIBUTION：分销商品、HAOCAI耗材、FUSHUPIN附属品、BAOCAI 包材、XUNI虚拟商品、QITA其他)
        """
        self._type = type
        """
            商品标题
        """
        self._title = title
        """
            商品名称
        """
        self._name = name
        """
            条形码，多条码请用”；”分隔；
        """
        self._bar_code = bar_code
        """
            商家商品编码
        """
        self._item_code = item_code
        """
            箱规
        """
        self._pcs = pcs
        """
            体积，单位立方厘米
        """
        self._volume = volume
        """
            高度，单位毫米
        """
        self._height = height
        """
            拓展属性
        """
        self._extend_fields = extend_fields
        """
            启用标识
        """
        self._use_yn = use_yn
        """
            是否启用批次管理
        """
        self._is_batch_mgt = is_batch_mgt
        """
            成本价，单位分
        """
        self._cost_price = cost_price
        """
            零售价，单位分
        """
        self._item_price = item_price
        """
            吊牌价，单位分
        """
        self._tag_price = tag_price
        """
            是否危险品
        """
        self._is_danger = is_danger
        """
            是否易碎品
        """
        self._is_hygroscopic = is_hygroscopic
        """
            宽度，单位毫米
        """
        self._width = width
        """
            长度，单位毫米
        """
        self._length = length
        """
            净重，单位克
        """
        self._net_weight = net_weight
        """
            仓库编码
        """
        self._store_code = store_code
        """
            保质期预警天数
        """
        self._advent_lifecycle = advent_lifecycle
        """
            保质期禁收天数
        """
        self._reject_lifecycle = reject_lifecycle
        """
            保质期禁售天数
        """
        self._lockup_lifecycle = lockup_lifecycle
        """
            商家商品ID
        """
        self._item_id = item_id
        """
            是否区域销售
        """
        self._is_area_sale = is_area_sale

    @property
    def is_sn_mgt(self):
        return self._is_sn_mgt

    @is_sn_mgt.setter
    def is_sn_mgt(self, is_sn_mgt):
        if isinstance(is_sn_mgt, bool):
            self._is_sn_mgt = is_sn_mgt
        else:
            raise TypeError("is_sn_mgt must be bool")

    @property
    def lifecycle(self):
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        if isinstance(lifecycle, int):
            self._lifecycle = lifecycle
        else:
            raise TypeError("lifecycle must be int")

    @property
    def is_shelflife(self):
        return self._is_shelflife

    @is_shelflife.setter
    def is_shelflife(self, is_shelflife):
        if isinstance(is_shelflife, bool):
            self._is_shelflife = is_shelflife
        else:
            raise TypeError("is_shelflife must be bool")

    @property
    def approval_number(self):
        return self._approval_number

    @approval_number.setter
    def approval_number(self, approval_number):
        if isinstance(approval_number, str):
            self._approval_number = approval_number
        else:
            raise TypeError("approval_number must be str")

    @property
    def origin_address(self):
        return self._origin_address

    @origin_address.setter
    def origin_address(self, origin_address):
        if isinstance(origin_address, int):
            self._origin_address = origin_address
        else:
            raise TypeError("origin_address must be int")

    @property
    def gross_weight(self):
        return self._gross_weight

    @gross_weight.setter
    def gross_weight(self, gross_weight):
        if isinstance(gross_weight, int):
            self._gross_weight = gross_weight
        else:
            raise TypeError("gross_weight must be int")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, str):
            self._size = size
        else:
            raise TypeError("size must be str")

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
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, specification):
        if isinstance(specification, str):
            self._specification = specification
        else:
            raise TypeError("specification must be str")

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
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise TypeError("brand must be str")

    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        if isinstance(category_name, str):
            self._category_name = category_name
        else:
            raise TypeError("category_name must be str")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str):
            self._category = category
        else:
            raise TypeError("category must be str")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, str):
            self._type = type
        else:
            raise TypeError("type must be str")

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
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name must be str")

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
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, item_code):
        if isinstance(item_code, str):
            self._item_code = item_code
        else:
            raise TypeError("item_code must be str")

    @property
    def pcs(self):
        return self._pcs

    @pcs.setter
    def pcs(self, pcs):
        if isinstance(pcs, int):
            self._pcs = pcs
        else:
            raise TypeError("pcs must be int")

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
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, int):
            self._height = height
        else:
            raise TypeError("height must be int")

    @property
    def extend_fields(self):
        return self._extend_fields

    @extend_fields.setter
    def extend_fields(self, extend_fields):
        if isinstance(extend_fields, str):
            self._extend_fields = extend_fields
        else:
            raise TypeError("extend_fields must be str")

    @property
    def use_yn(self):
        return self._use_yn

    @use_yn.setter
    def use_yn(self, use_yn):
        if isinstance(use_yn, bool):
            self._use_yn = use_yn
        else:
            raise TypeError("use_yn must be bool")

    @property
    def is_batch_mgt(self):
        return self._is_batch_mgt

    @is_batch_mgt.setter
    def is_batch_mgt(self, is_batch_mgt):
        if isinstance(is_batch_mgt, bool):
            self._is_batch_mgt = is_batch_mgt
        else:
            raise TypeError("is_batch_mgt must be bool")

    @property
    def cost_price(self):
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        if isinstance(cost_price, int):
            self._cost_price = cost_price
        else:
            raise TypeError("cost_price must be int")

    @property
    def item_price(self):
        return self._item_price

    @item_price.setter
    def item_price(self, item_price):
        if isinstance(item_price, int):
            self._item_price = item_price
        else:
            raise TypeError("item_price must be int")

    @property
    def tag_price(self):
        return self._tag_price

    @tag_price.setter
    def tag_price(self, tag_price):
        if isinstance(tag_price, int):
            self._tag_price = tag_price
        else:
            raise TypeError("tag_price must be int")

    @property
    def is_danger(self):
        return self._is_danger

    @is_danger.setter
    def is_danger(self, is_danger):
        if isinstance(is_danger, bool):
            self._is_danger = is_danger
        else:
            raise TypeError("is_danger must be bool")

    @property
    def is_hygroscopic(self):
        return self._is_hygroscopic

    @is_hygroscopic.setter
    def is_hygroscopic(self, is_hygroscopic):
        if isinstance(is_hygroscopic, bool):
            self._is_hygroscopic = is_hygroscopic
        else:
            raise TypeError("is_hygroscopic must be bool")

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
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if isinstance(length, int):
            self._length = length
        else:
            raise TypeError("length must be int")

    @property
    def net_weight(self):
        return self._net_weight

    @net_weight.setter
    def net_weight(self, net_weight):
        if isinstance(net_weight, int):
            self._net_weight = net_weight
        else:
            raise TypeError("net_weight must be int")

    @property
    def store_code(self):
        return self._store_code

    @store_code.setter
    def store_code(self, store_code):
        if isinstance(store_code, str):
            self._store_code = store_code
        else:
            raise TypeError("store_code must be str")

    @property
    def advent_lifecycle(self):
        return self._advent_lifecycle

    @advent_lifecycle.setter
    def advent_lifecycle(self, advent_lifecycle):
        if isinstance(advent_lifecycle, int):
            self._advent_lifecycle = advent_lifecycle
        else:
            raise TypeError("advent_lifecycle must be int")

    @property
    def reject_lifecycle(self):
        return self._reject_lifecycle

    @reject_lifecycle.setter
    def reject_lifecycle(self, reject_lifecycle):
        if isinstance(reject_lifecycle, int):
            self._reject_lifecycle = reject_lifecycle
        else:
            raise TypeError("reject_lifecycle must be int")

    @property
    def lockup_lifecycle(self):
        return self._lockup_lifecycle

    @lockup_lifecycle.setter
    def lockup_lifecycle(self, lockup_lifecycle):
        if isinstance(lockup_lifecycle, int):
            self._lockup_lifecycle = lockup_lifecycle
        else:
            raise TypeError("lockup_lifecycle must be int")

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, str):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be str")

    @property
    def is_area_sale(self):
        return self._is_area_sale

    @is_area_sale.setter
    def is_area_sale(self, is_area_sale):
        if isinstance(is_area_sale, bool):
            self._is_area_sale = is_area_sale
        else:
            raise TypeError("is_area_sale must be bool")


    def get_api_name(self):
        return "taobao.wlb.wms.sku.create"

    def to_dict(self):
        request_dict = {}
        if self._is_sn_mgt is not None:
            request_dict["is_sn_mgt"] = convert_basic(self._is_sn_mgt)

        if self._lifecycle is not None:
            request_dict["lifecycle"] = convert_basic(self._lifecycle)

        if self._is_shelflife is not None:
            request_dict["is_shelflife"] = convert_basic(self._is_shelflife)

        if self._approval_number is not None:
            request_dict["approval_number"] = convert_basic(self._approval_number)

        if self._origin_address is not None:
            request_dict["origin_address"] = convert_basic(self._origin_address)

        if self._gross_weight is not None:
            request_dict["gross_weight"] = convert_basic(self._gross_weight)

        if self._size is not None:
            request_dict["size"] = convert_basic(self._size)

        if self._color is not None:
            request_dict["color"] = convert_basic(self._color)

        if self._specification is not None:
            request_dict["specification"] = convert_basic(self._specification)

        if self._brand_name is not None:
            request_dict["brand_name"] = convert_basic(self._brand_name)

        if self._brand is not None:
            request_dict["brand"] = convert_basic(self._brand)

        if self._category_name is not None:
            request_dict["category_name"] = convert_basic(self._category_name)

        if self._category is not None:
            request_dict["category"] = convert_basic(self._category)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._title is not None:
            request_dict["title"] = convert_basic(self._title)

        if self._name is not None:
            request_dict["name"] = convert_basic(self._name)

        if self._bar_code is not None:
            request_dict["bar_code"] = convert_basic(self._bar_code)

        if self._item_code is not None:
            request_dict["item_code"] = convert_basic(self._item_code)

        if self._pcs is not None:
            request_dict["pcs"] = convert_basic(self._pcs)

        if self._volume is not None:
            request_dict["volume"] = convert_basic(self._volume)

        if self._height is not None:
            request_dict["height"] = convert_basic(self._height)

        if self._extend_fields is not None:
            request_dict["extend_fields"] = convert_basic(self._extend_fields)

        if self._use_yn is not None:
            request_dict["use_yn"] = convert_basic(self._use_yn)

        if self._is_batch_mgt is not None:
            request_dict["is_batch_mgt"] = convert_basic(self._is_batch_mgt)

        if self._cost_price is not None:
            request_dict["cost_price"] = convert_basic(self._cost_price)

        if self._item_price is not None:
            request_dict["item_price"] = convert_basic(self._item_price)

        if self._tag_price is not None:
            request_dict["tag_price"] = convert_basic(self._tag_price)

        if self._is_danger is not None:
            request_dict["is_danger"] = convert_basic(self._is_danger)

        if self._is_hygroscopic is not None:
            request_dict["is_hygroscopic"] = convert_basic(self._is_hygroscopic)

        if self._width is not None:
            request_dict["width"] = convert_basic(self._width)

        if self._length is not None:
            request_dict["length"] = convert_basic(self._length)

        if self._net_weight is not None:
            request_dict["net_weight"] = convert_basic(self._net_weight)

        if self._store_code is not None:
            request_dict["store_code"] = convert_basic(self._store_code)

        if self._advent_lifecycle is not None:
            request_dict["advent_lifecycle"] = convert_basic(self._advent_lifecycle)

        if self._reject_lifecycle is not None:
            request_dict["reject_lifecycle"] = convert_basic(self._reject_lifecycle)

        if self._lockup_lifecycle is not None:
            request_dict["lockup_lifecycle"] = convert_basic(self._lockup_lifecycle)

        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._is_area_sale is not None:
            request_dict["is_area_sale"] = convert_basic(self._is_area_sale)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


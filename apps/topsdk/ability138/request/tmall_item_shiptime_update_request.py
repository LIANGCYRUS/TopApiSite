from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemShiptimeUpdateRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        ship_time: str = None,
        sku_ship_times: list = None,
        option: object = None
    ):
        """
            商品ID
        """
        self._item_id = item_id
        """
            被更新发货时间（商品级）；格式和具体设置的发货时间格式相关。绝对发货时间填写yyyy-MM-dd;相对发货时间填写数字。发货时间必须在当前时间后三天。如果设置的绝对时间小于当前时间的三天后，会清除该商品的发货时间设置。如果是相对时间小于3，则会提示出错。如果shiptimeType为0，要清除商品上的发货时间，该字段可以填任意字符,也可以不填。
        """
        self._ship_time = ship_time
        """
            被更新SKU的发货时间，后台会根据三个子属性去查找匹配的sku，如果找到就默认对sku进行更新，当无匹配sku且更新类型针对sku，会报错。
        """
        self._sku_ship_times = sku_ship_times
        """
            批量更新商品/SKU发货时间的备选项
        """
        self._option = option

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, int):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be int")

    @property
    def ship_time(self):
        return self._ship_time

    @ship_time.setter
    def ship_time(self, ship_time):
        if isinstance(ship_time, str):
            self._ship_time = ship_time
        else:
            raise TypeError("ship_time must be str")

    @property
    def sku_ship_times(self):
        return self._sku_ship_times

    @sku_ship_times.setter
    def sku_ship_times(self, sku_ship_times):
        if isinstance(sku_ship_times, list):
            self._sku_ship_times = sku_ship_times
        else:
            raise TypeError("sku_ship_times must be list")

    @property
    def option(self):
        return self._option

    @option.setter
    def option(self, option):
        if isinstance(option, object):
            self._option = option
        else:
            raise TypeError("option must be object")


    def get_api_name(self):
        return "tmall.item.shiptime.update"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._ship_time is not None:
            request_dict["ship_time"] = convert_basic(self._ship_time)

        if self._sku_ship_times is not None:
            request_dict["sku_ship_times"] = convert_struct_list(self._sku_ship_times)

        if self._option is not None:
            request_dict["option"] = convert_struct(self._option)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TmallItemShiptimeUpdateUpdateSkuShipTime:
    def __init__(
        self,
        ship_time: str = None,
        sku_id: int = None,
        properties: str = None,
        outer_id: str = None
    ):
        """
            被更新发货时间；格式和具体设置的发货时间格式相关。绝对发货时间填写yyyy-MM-dd;相对发货时间填写数字。
        """
        self.ship_time = ship_time
        """
            SKU的ID
        """
        self.sku_id = sku_id
        """
            Sku属性串。格式:pid:vid;pid:vid,如: 1627207:3232483;1630696:3284570,表示机身颜色:军绿色;手机套餐:一电一充
        """
        self.properties = properties
        """
            Sku的商家外部id；如：2015_07_23_D_123
        """
        self.outer_id = outer_id

class TmallItemShiptimeUpdateUpdateItemShipTimeOption:
    def __init__(
        self,
        ship_time_type: int = None,
        update_type: int = None
    ):
        """
            0代表清空匹配的SKU发货时间数据或者商品发货时间数据；1代表：固定发货时间；2代表：相对发货时间
        """
        self.ship_time_type = ship_time_type
        """
            更新类型，默认不填时更新sku，0表示更新sku，1表示更新商品维度，其他值均非法
        """
        self.update_type = update_type


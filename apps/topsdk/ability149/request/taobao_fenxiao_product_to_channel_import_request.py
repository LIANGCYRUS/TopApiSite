from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoProductToChannelImportRequest(BaseRequest):

    def __init__(
        self,
        channel: int = None,
        product_id: int = None
    ):
        """
            要导入的渠道[21 零售PLUS]目前仅支持此渠道
        """
        self._channel = channel
        """
            要导入的产品id
        """
        self._product_id = product_id

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        if isinstance(channel, int):
            self._channel = channel
        else:
            raise TypeError("channel must be int")

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self._product_id = product_id
        else:
            raise TypeError("product_id must be int")


    def get_api_name(self):
        return "taobao.fenxiao.product.to.channel.import"

    def to_dict(self):
        request_dict = {}
        if self._channel is not None:
            request_dict["channel"] = convert_basic(self._channel)

        if self._product_id is not None:
            request_dict["product_id"] = convert_basic(self._product_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


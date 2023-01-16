from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoEticketMerchantImgUploadRequest(BaseRequest):

    def __init__(
        self,
        img_bytes: bytes = None
    ):
        """
            二维码图片
        """
        self._img_bytes = img_bytes

    @property
    def img_bytes(self):
        return self._img_bytes

    @img_bytes.setter
    def img_bytes(self, img_bytes):
        if isinstance(img_bytes, bytes):
            self._img_bytes = img_bytes
        else:
            raise TypeError("img_bytes must be bytes")


    def get_api_name(self):
        return "taobao.eticket.merchant.img.upload"

    def to_dict(self):
        request_dict = {}
        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._img_bytes is not None:
            file_param_dict["img_bytes"] = convert_basic(self._img_bytes)
        return file_param_dict


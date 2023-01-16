from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketQrcodeUploadRequest(BaseRequest):

    def __init__(
        self,
        img_bytes: bytes = None,
        code_merchant_id: int = None
    ):
        """
            上传的图片byte[]  小于300K，图片尺寸400*400以内
        """
        self._img_bytes = img_bytes
        """
            码商ID
        """
        self._code_merchant_id = code_merchant_id

    @property
    def img_bytes(self):
        return self._img_bytes

    @img_bytes.setter
    def img_bytes(self, img_bytes):
        if isinstance(img_bytes, bytes):
            self._img_bytes = img_bytes
        else:
            raise TypeError("img_bytes must be bytes")

    @property
    def code_merchant_id(self):
        return self._code_merchant_id

    @code_merchant_id.setter
    def code_merchant_id(self, code_merchant_id):
        if isinstance(code_merchant_id, int):
            self._code_merchant_id = code_merchant_id
        else:
            raise TypeError("code_merchant_id must be int")


    def get_api_name(self):
        return "taobao.vmarket.eticket.qrcode.upload"

    def to_dict(self):
        request_dict = {}
        if self._code_merchant_id is not None:
            request_dict["code_merchant_id"] = convert_basic(self._code_merchant_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._img_bytes is not None:
            file_param_dict["img_bytes"] = convert_basic(self._img_bytes)
        return file_param_dict


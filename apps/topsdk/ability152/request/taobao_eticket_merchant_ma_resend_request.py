from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoEticketMerchantMaResendRequest(BaseRequest):

    def __init__(
        self,
        biz_type: int = None,
        isv_ma_list: list = None,
        outer_id: str = None,
        token: str = None
    ):
        """
            业务类型
        """
        self._biz_type = biz_type
        """
            待重发的码列表
        """
        self._isv_ma_list = isv_ma_list
        """
            业务id（订单号）
        """
        self._outer_id = outer_id
        """
            需要跟发码通知获取到的参数一致
        """
        self._token = token

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        if isinstance(biz_type, int):
            self._biz_type = biz_type
        else:
            raise TypeError("biz_type must be int")

    @property
    def isv_ma_list(self):
        return self._isv_ma_list

    @isv_ma_list.setter
    def isv_ma_list(self, isv_ma_list):
        if isinstance(isv_ma_list, list):
            self._isv_ma_list = isv_ma_list
        else:
            raise TypeError("isv_ma_list must be list")

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
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        if isinstance(token, str):
            self._token = token
        else:
            raise TypeError("token must be str")


    def get_api_name(self):
        return "taobao.eticket.merchant.ma.resend"

    def to_dict(self):
        request_dict = {}
        if self._biz_type is not None:
            request_dict["biz_type"] = convert_basic(self._biz_type)

        if self._isv_ma_list is not None:
            request_dict["isv_ma_list"] = convert_struct_list(self._isv_ma_list)

        if self._outer_id is not None:
            request_dict["outer_id"] = convert_basic(self._outer_id)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoEticketMerchantMaResendIsvMa:
    def __init__(
        self,
        code: str = None,
        num: int = None,
        qr_image: str = None
    ):
        """
            串码码值
        """
        self.code = code
        """
            码的可核销份数
        """
        self.num = num
        """
            二维码图片文件名。已经申请了上传二维码的码商必填，其它码商无需关心。这个值是taobao.eticket.merchant.img.upload调用后的file_name
        """
        self.qr_image = qr_image


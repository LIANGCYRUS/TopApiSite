from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketSendRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        verify_codes: str = None,
        token: str = None,
        codemerchant_id: int = None,
        qr_images: str = None
    ):
        """
            订单编号
        """
        self._order_id = order_id
        """
            发送成功的验证码及可验证次数的列表，码和可验证次数用英文冒号分隔，多个码之间用英文逗号分隔，所有字符都为英文半角
        """
        self._verify_codes = verify_codes
        """
            安全验证token，需要和发码通知中的token一致
        """
        self._token = token
        """
            码商ID,是码商的话必须传递,如果是信任卖家,不需要传
        """
        self._codemerchant_id = codemerchant_id
        """
            不需要上传二维码图片的码商请不要传，需要传入二维码的码商请先调用taobao.vmarket.eticket.qrcode.upload接口，将返回的img_filename文件名称作为参数，多个文件名用逗号隔开且与参数verify_codes按从左到有的顺序一一对应。
        """
        self._qr_images = qr_images

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        if isinstance(order_id, int):
            self._order_id = order_id
        else:
            raise TypeError("order_id must be int")

    @property
    def verify_codes(self):
        return self._verify_codes

    @verify_codes.setter
    def verify_codes(self, verify_codes):
        if isinstance(verify_codes, str):
            self._verify_codes = verify_codes
        else:
            raise TypeError("verify_codes must be str")

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        if isinstance(token, str):
            self._token = token
        else:
            raise TypeError("token must be str")

    @property
    def codemerchant_id(self):
        return self._codemerchant_id

    @codemerchant_id.setter
    def codemerchant_id(self, codemerchant_id):
        if isinstance(codemerchant_id, int):
            self._codemerchant_id = codemerchant_id
        else:
            raise TypeError("codemerchant_id must be int")

    @property
    def qr_images(self):
        return self._qr_images

    @qr_images.setter
    def qr_images(self, qr_images):
        if isinstance(qr_images, str):
            self._qr_images = qr_images
        else:
            raise TypeError("qr_images must be str")


    def get_api_name(self):
        return "taobao.vmarket.eticket.send"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._verify_codes is not None:
            request_dict["verify_codes"] = convert_basic(self._verify_codes)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        if self._qr_images is not None:
            request_dict["qr_images"] = convert_basic(self._qr_images)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


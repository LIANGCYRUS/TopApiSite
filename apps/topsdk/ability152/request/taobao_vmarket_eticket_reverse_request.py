from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketReverseRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        reverse_code: str = None,
        reverse_num: int = None,
        consume_secial_num: str = None,
        verify_codes: str = None,
        token: str = None,
        codemerchant_id: int = None,
        posid: str = None,
        qr_images: str = None
    ):
        """
            进行验码的电子凭证订单的订单ID
        """
        self._order_id = order_id
        """
            冲正的码，只支持单个码
        """
        self._reverse_code = reverse_code
        """
            冲正份数（必须是和被冲正的核销记录的份数一致）
        """
        self._reverse_num = reverse_num
        """
            需要冲正的核销记录对应核销流水号（对应的核销操作时候传递的自定义流水号）
        """
        self._consume_secial_num = consume_secial_num
        """
            所有冲正后需要重新生成的码和对应的次数。码和次数之间用英文冒号分隔，多个码之间用英文逗号分隔。如果冲正后不需要重新生成码，留空
        """
        self._verify_codes = verify_codes
        """
            安全验证token，需要和该订单发码通知中的token一致
        """
        self._token = token
        """
            码商ID，是码商的话必须传递，如果是信任卖家不要传
        """
        self._codemerchant_id = codemerchant_id
        """
            机具id，如果是码商必须传，如果是信任卖家不要传
        """
        self._posid = posid
        """
            不需要上传二维码图片或者冲正后不需要变更码的请不要传，需要传入二维码的码商请先调用taobao.vmarket.eticket.qrcode.upload接口，将返回的img_filename文件名称作为参数，多个文件名用逗号隔开且与参数verify_codes按从左到有的顺序一一对应。
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
    def reverse_code(self):
        return self._reverse_code

    @reverse_code.setter
    def reverse_code(self, reverse_code):
        if isinstance(reverse_code, str):
            self._reverse_code = reverse_code
        else:
            raise TypeError("reverse_code must be str")

    @property
    def reverse_num(self):
        return self._reverse_num

    @reverse_num.setter
    def reverse_num(self, reverse_num):
        if isinstance(reverse_num, int):
            self._reverse_num = reverse_num
        else:
            raise TypeError("reverse_num must be int")

    @property
    def consume_secial_num(self):
        return self._consume_secial_num

    @consume_secial_num.setter
    def consume_secial_num(self, consume_secial_num):
        if isinstance(consume_secial_num, str):
            self._consume_secial_num = consume_secial_num
        else:
            raise TypeError("consume_secial_num must be str")

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
    def posid(self):
        return self._posid

    @posid.setter
    def posid(self, posid):
        if isinstance(posid, str):
            self._posid = posid
        else:
            raise TypeError("posid must be str")

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
        return "taobao.vmarket.eticket.reverse"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._reverse_code is not None:
            request_dict["reverse_code"] = convert_basic(self._reverse_code)

        if self._reverse_num is not None:
            request_dict["reverse_num"] = convert_basic(self._reverse_num)

        if self._consume_secial_num is not None:
            request_dict["consume_secial_num"] = convert_basic(self._consume_secial_num)

        if self._verify_codes is not None:
            request_dict["verify_codes"] = convert_basic(self._verify_codes)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        if self._posid is not None:
            request_dict["posid"] = convert_basic(self._posid)

        if self._qr_images is not None:
            request_dict["qr_images"] = convert_basic(self._qr_images)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


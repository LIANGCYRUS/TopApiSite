from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketConsumeRequest(BaseRequest):

    def __init__(
        self,
        order_id: int = None,
        verify_code: str = None,
        consume_num: int = None,
        token: str = None,
        codemerchant_id: int = None,
        posid: str = None,
        mobile: str = None,
        new_code: str = None,
        serial_num: str = None,
        qr_images: str = None
    ):
        """
            进行验码的电子凭证订单的订单ID
        """
        self._order_id = order_id
        """
            核销的码，只支持单个码，多个码核销需要多次调用
        """
        self._verify_code = verify_code
        """
            核销份数
        """
        self._consume_num = consume_num
        """
            安全验证token,需要和发码通知中的token一致
        """
        self._token = token
        """
            码商ID,是码商的话必须传递,如果是信任卖家不需要传
        """
        self._codemerchant_id = codemerchant_id
        """
            机具ID(此参数信任卖家可不传递，码商必须传递)
        """
        self._posid = posid
        """
            手机后四位(没有特殊说明请不要传该参数)
        """
        self._mobile = mobile
        """
            核销后需要重新生成的码，如果不需要重新生成码，不要传该参数
        """
        self._new_code = new_code
        """
            自定义核销流水号，如果核销调用失败，可以用该核销流水号进行冲正操作，需要小于等于100个字符(a-zA-Z0-9_)；每次核销都是唯一的流水号
        """
        self._serial_num = serial_num
        """
            不需要上传二维码图片或者核销后不需重新生成码码商请不要传，需要传入二维码的码商请先调用taobao.vmarket.eticket.qrcode.upload接口，将返回的img_filename文件名称作为参数（如果二维码不变的话，也可将将发码时传入二维码文件名作为参数传入），文件名与参数new_code必须相互对应。
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
    def verify_code(self):
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        if isinstance(verify_code, str):
            self._verify_code = verify_code
        else:
            raise TypeError("verify_code must be str")

    @property
    def consume_num(self):
        return self._consume_num

    @consume_num.setter
    def consume_num(self, consume_num):
        if isinstance(consume_num, int):
            self._consume_num = consume_num
        else:
            raise TypeError("consume_num must be int")

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
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        if isinstance(mobile, str):
            self._mobile = mobile
        else:
            raise TypeError("mobile must be str")

    @property
    def new_code(self):
        return self._new_code

    @new_code.setter
    def new_code(self, new_code):
        if isinstance(new_code, str):
            self._new_code = new_code
        else:
            raise TypeError("new_code must be str")

    @property
    def serial_num(self):
        return self._serial_num

    @serial_num.setter
    def serial_num(self, serial_num):
        if isinstance(serial_num, str):
            self._serial_num = serial_num
        else:
            raise TypeError("serial_num must be str")

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
        return "taobao.vmarket.eticket.consume"

    def to_dict(self):
        request_dict = {}
        if self._order_id is not None:
            request_dict["order_id"] = convert_basic(self._order_id)

        if self._verify_code is not None:
            request_dict["verify_code"] = convert_basic(self._verify_code)

        if self._consume_num is not None:
            request_dict["consume_num"] = convert_basic(self._consume_num)

        if self._token is not None:
            request_dict["token"] = convert_basic(self._token)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        if self._posid is not None:
            request_dict["posid"] = convert_basic(self._posid)

        if self._mobile is not None:
            request_dict["mobile"] = convert_basic(self._mobile)

        if self._new_code is not None:
            request_dict["new_code"] = convert_basic(self._new_code)

        if self._serial_num is not None:
            request_dict["serial_num"] = convert_basic(self._serial_num)

        if self._qr_images is not None:
            request_dict["qr_images"] = convert_basic(self._qr_images)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


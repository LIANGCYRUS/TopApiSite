from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoRefundMessageAddRequest(BaseRequest):

    def __init__(
        self,
        image: bytes = None,
        refund_id: int = None,
        content: str = None
    ):
        """
            图片（凭证）。类型: JPG,GIF,PNG;最大为: 500K
        """
        self._image = image
        """
            退款编号。
        """
        self._refund_id = refund_id
        """
            留言内容。最大长度: 400个字节
        """
        self._content = content

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        if isinstance(image, bytes):
            self._image = image
        else:
            raise TypeError("image must be bytes")

    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        if isinstance(refund_id, int):
            self._refund_id = refund_id
        else:
            raise TypeError("refund_id must be int")

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if isinstance(content, str):
            self._content = content
        else:
            raise TypeError("content must be str")


    def get_api_name(self):
        return "taobao.refund.message.add"

    def to_dict(self):
        request_dict = {}
        if self._refund_id is not None:
            request_dict["refund_id"] = convert_basic(self._refund_id)

        if self._content is not None:
            request_dict["content"] = convert_basic(self._content)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._image is not None:
            file_param_dict["image"] = convert_basic(self._image)
        return file_param_dict


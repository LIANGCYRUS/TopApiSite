from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureTokenRequest(BaseRequest):

    def __init__(
        self,
        generate_token_request: object = None
    ):
        """
            请求参数
        """
        self._generate_token_request = generate_token_request

    @property
    def generate_token_request(self):
        return self._generate_token_request

    @generate_token_request.setter
    def generate_token_request(self, generate_token_request):
        if isinstance(generate_token_request, object):
            self._generate_token_request = generate_token_request
        else:
            raise TypeError("generate_token_request must be object")


    def get_api_name(self):
        return "taobao.picture.token"

    def to_dict(self):
        request_dict = {}
        if self._generate_token_request is not None:
            request_dict["generate_token_request"] = convert_struct(self._generate_token_request)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoPictureTokenUploadPolicy:
    def __init__(
        self,
        size_limit: int = None,
        mime_limit: str = None,
        dir_id: int = None,
        expired_time: int = None
    ):
        """
            限制用户上传文件的大小。 若用户上传文件大小超过size_limit，无法上传成功。
        """
        self.size_limit = size_limit
        """
            限制用户上传文件的类型，多个值用；分隔。 可设置的值为：image/jpeg,image/png,image/webp等。 若用户上传文件的mime类型不在mime_limit范围内，无法上传成功。
        """
        self.mime_limit = mime_limit
        """
            图片分类ID，可通过taobao.picture.category.get获取。根目录值为0。
        """
        self.dir_id = dir_id
        """
            token有效期的截止时间，值为自1970年1月1日0时起的毫秒数。若当前时间晚于expired_time，token失效，上传文件失败。
        """
        self.expired_time = expired_time

class TaobaoPictureTokenGenerateTokenRequest:
    def __init__(
        self,
        upload_policy: object = None
    ):
        """
            请求策略
        """
        self.upload_policy = upload_policy


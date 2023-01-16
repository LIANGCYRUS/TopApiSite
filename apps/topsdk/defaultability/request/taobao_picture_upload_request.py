from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureUploadRequest(BaseRequest):

    def __init__(
        self,
        picture_id: int = None,
        picture_category_id: int = None,
        img: bytes = None,
        image_input_title: str = None,
        title: str = None,
        client_type: str = None,
        is_https: bool = None
    ):
        """
            如果此参数大于0，而且在后台能查到对应的图片，则此次上传为原图替换
        """
        self._picture_id = picture_id
        """
            图片分类ID，设置具体某个分类ID或设置0上传到默认分类，只能传入一个分类
        """
        self._picture_category_id = picture_category_id
        """
            图片二进制文件流,不能为空,允许png、jpg、gif图片格式,3M以内。
        """
        self._img = img
        """
            包括后缀名的图片标题,不能为空，如Bule.jpg,有些卖家希望图片上传后取图片文件的默认名
        """
        self._image_input_title = image_input_title
        """
            图片标题,如果为空,传的图片标题就取去掉后缀名的image_input_title,超过50字符长度会截取50字符,重名会在标题末尾加"(1)";标题末尾已经有"(数字)"了，则数字加1
        """
        self._title = title
        """
            图片上传的来源，有电脑版本宝贝发布，手机版本宝贝发布client:computer电脑版本宝贝使用，client:phone手机版本宝贝使用。注意：当client:phone时，图片限制为宽度在480-620之间，长度不能超过960，否则会报错。
        """
        self._client_type = client_type
        """
            是否获取https连接
        """
        self._is_https = is_https

    @property
    def picture_id(self):
        return self._picture_id

    @picture_id.setter
    def picture_id(self, picture_id):
        if isinstance(picture_id, int):
            self._picture_id = picture_id
        else:
            raise TypeError("picture_id must be int")

    @property
    def picture_category_id(self):
        return self._picture_category_id

    @picture_category_id.setter
    def picture_category_id(self, picture_category_id):
        if isinstance(picture_category_id, int):
            self._picture_category_id = picture_category_id
        else:
            raise TypeError("picture_category_id must be int")

    @property
    def img(self):
        return self._img

    @img.setter
    def img(self, img):
        if isinstance(img, bytes):
            self._img = img
        else:
            raise TypeError("img must be bytes")

    @property
    def image_input_title(self):
        return self._image_input_title

    @image_input_title.setter
    def image_input_title(self, image_input_title):
        if isinstance(image_input_title, str):
            self._image_input_title = image_input_title
        else:
            raise TypeError("image_input_title must be str")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise TypeError("title must be str")

    @property
    def client_type(self):
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        if isinstance(client_type, str):
            self._client_type = client_type
        else:
            raise TypeError("client_type must be str")

    @property
    def is_https(self):
        return self._is_https

    @is_https.setter
    def is_https(self, is_https):
        if isinstance(is_https, bool):
            self._is_https = is_https
        else:
            raise TypeError("is_https must be bool")


    def get_api_name(self):
        return "taobao.picture.upload"

    def to_dict(self):
        request_dict = {}
        if self._picture_id is not None:
            request_dict["picture_id"] = convert_basic(self._picture_id)

        if self._picture_category_id is not None:
            request_dict["picture_category_id"] = convert_basic(self._picture_category_id)

        if self._image_input_title is not None:
            request_dict["image_input_title"] = convert_basic(self._image_input_title)

        if self._title is not None:
            request_dict["title"] = convert_basic(self._title)

        if self._client_type is not None:
            request_dict["client_type"] = convert_basic(self._client_type)

        if self._is_https is not None:
            request_dict["is_https"] = convert_basic(self._is_https)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        if self._img is not None:
            file_param_dict["img"] = convert_basic(self._img)
        return file_param_dict


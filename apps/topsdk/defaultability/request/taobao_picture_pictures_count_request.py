from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPicturePicturesCountRequest(BaseRequest):

    def __init__(
        self,
        picture_id: int = None,
        picture_category_id: int = None,
        deleted: str = None,
        start_modified_date: datetime = None,
        start_date: datetime = None,
        end_date: datetime = None,
        client_type: str = None,
        title: str = None
    ):
        """
            图片ID
        """
        self._picture_id = picture_id
        """
            图片分类
        """
        self._picture_category_id = picture_category_id
        """
            是否删除,undeleted代表没有删除,deleted表示删除
        """
        self._deleted = deleted
        """
            图片被修改的时间点，格式:yyyy-MM-dd HH:mm:ss。查询此修改时间点之后到目前的图片。
        """
        self._start_modified_date = start_modified_date
        """
            查询上传开始时间点,格式:yyyy-MM-dd HH:mm:ss
        """
        self._start_date = start_date
        """
            查询上传结束时间点,格式:yyyy-MM-dd HH:mm:ss
        """
        self._end_date = end_date
        """
            图片使用，如果是pc宝贝detail使用，设置为client:computer，查询出来的图片是符合pc的宝贝detail显示的如果是手机宝贝detail使用，设置为client:phone，查询出来的图片是符合手机的宝贝detail显示的,默认值是全部
        """
        self._client_type = client_type
        """
            文件名
        """
        self._title = title

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
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        if isinstance(deleted, str):
            self._deleted = deleted
        else:
            raise TypeError("deleted must be str")

    @property
    def start_modified_date(self):
        return self._start_modified_date

    @start_modified_date.setter
    def start_modified_date(self, start_modified_date):
        if isinstance(start_modified_date, datetime):
            self._start_modified_date = start_modified_date
        else:
            raise TypeError("start_modified_date must be datetime")

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, datetime):
            self._start_date = start_date
        else:
            raise TypeError("start_date must be datetime")

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, datetime):
            self._end_date = end_date
        else:
            raise TypeError("end_date must be datetime")

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
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
        else:
            raise TypeError("title must be str")


    def get_api_name(self):
        return "taobao.picture.pictures.count"

    def to_dict(self):
        request_dict = {}
        if self._picture_id is not None:
            request_dict["picture_id"] = convert_basic(self._picture_id)

        if self._picture_category_id is not None:
            request_dict["picture_category_id"] = convert_basic(self._picture_category_id)

        if self._deleted is not None:
            request_dict["deleted"] = convert_basic(self._deleted)

        if self._start_modified_date is not None:
            request_dict["start_modified_date"] = convert_basic(self._start_modified_date)

        if self._start_date is not None:
            request_dict["start_date"] = convert_basic(self._start_date)

        if self._end_date is not None:
            request_dict["end_date"] = convert_basic(self._end_date)

        if self._client_type is not None:
            request_dict["client_type"] = convert_basic(self._client_type)

        if self._title is not None:
            request_dict["title"] = convert_basic(self._title)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


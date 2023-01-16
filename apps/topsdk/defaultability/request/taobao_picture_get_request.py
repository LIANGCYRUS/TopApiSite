from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoPictureGetRequest(BaseRequest):

    def __init__(
        self,
        urls: str = None,
        is_https: bool = None,
        picture_id: int = None,
        picture_category_id: int = None,
        deleted: str = None,
        modified_time: datetime = None,
        title: str = None,
        start_date: datetime = None,
        end_date: datetime = None,
        page_no: int = None,
        page_size: int = None,
        client_type: str = None,
        order_by: str = None
    ):
        """
            图片url查询接口
        """
        self._urls = urls
        """
            是否获取https的链接
        """
        self._is_https = is_https
        """
            图片ID
        """
        self._picture_id = picture_id
        """
            图片分类ID
        """
        self._picture_category_id = picture_category_id
        """
            是否删除,unfroze代表没有删除
        """
        self._deleted = deleted
        """
            图片被修改的时间点，格式:yyyy-MM-dd HH:mm:ss。查询此修改时间点之后到目前的图片。
        """
        self._modified_time = modified_time
        """
            图片标题,最大长度50字符,中英文都算一字符
        """
        self._title = title
        """
            查询上传开始时间点,格式:yyyy-MM-dd HH:mm:ss
        """
        self._start_date = start_date
        """
            查询上传结束时间点,格式:yyyy-MM-dd HH:mm:ss
        """
        self._end_date = end_date
        """
            页码.传入值为1代表第一页,传入值为2代表第二页,依此类推,默认值为1
        """
        self._page_no = page_no
        """
            每页条数.每页返回最多返回100条,默认值40
        """
        self._page_size = page_size
        """
            图片使用，如果是pc宝贝detail使用，设置为client:computer，查询出来的图片是符合pc的宝贝detail显示的如果是手机宝贝detail使用，设置为client:phone，查询出来的图片是符合手机的宝贝detail显示的,默认值是全部
        """
        self._client_type = client_type
        """
            图片查询结果排序,time:desc按上传时间从晚到早(默认), time:asc按上传时间从早到晚,sizes:desc按图片从大到小，sizes:asc按图片从小到大,默认time:desc
        """
        self._order_by = order_by

    @property
    def urls(self):
        return self._urls

    @urls.setter
    def urls(self, urls):
        if isinstance(urls, str):
            self._urls = urls
        else:
            raise TypeError("urls must be str")

    @property
    def is_https(self):
        return self._is_https

    @is_https.setter
    def is_https(self, is_https):
        if isinstance(is_https, bool):
            self._is_https = is_https
        else:
            raise TypeError("is_https must be bool")

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
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        if isinstance(modified_time, datetime):
            self._modified_time = modified_time
        else:
            raise TypeError("modified_time must be datetime")

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
    def page_no(self):
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        if isinstance(page_no, int):
            self._page_no = page_no
        else:
            raise TypeError("page_no must be int")

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        if isinstance(page_size, int):
            self._page_size = page_size
        else:
            raise TypeError("page_size must be int")

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
    def order_by(self):
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        if isinstance(order_by, str):
            self._order_by = order_by
        else:
            raise TypeError("order_by must be str")


    def get_api_name(self):
        return "taobao.picture.get"

    def to_dict(self):
        request_dict = {}
        if self._urls is not None:
            request_dict["urls"] = convert_basic(self._urls)

        if self._is_https is not None:
            request_dict["is_https"] = convert_basic(self._is_https)

        if self._picture_id is not None:
            request_dict["picture_id"] = convert_basic(self._picture_id)

        if self._picture_category_id is not None:
            request_dict["picture_category_id"] = convert_basic(self._picture_category_id)

        if self._deleted is not None:
            request_dict["deleted"] = convert_basic(self._deleted)

        if self._modified_time is not None:
            request_dict["modified_time"] = convert_basic(self._modified_time)

        if self._title is not None:
            request_dict["title"] = convert_basic(self._title)

        if self._start_date is not None:
            request_dict["start_date"] = convert_basic(self._start_date)

        if self._end_date is not None:
            request_dict["end_date"] = convert_basic(self._end_date)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._client_type is not None:
            request_dict["client_type"] = convert_basic(self._client_type)

        if self._order_by is not None:
            request_dict["order_by"] = convert_basic(self._order_by)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


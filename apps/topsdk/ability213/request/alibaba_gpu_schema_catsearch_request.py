from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class AlibabaGpuSchemaCatsearchRequest(BaseRequest):

    def __init__(
        self,
        leaf_cat_id: int = None,
        current_page: int = None,
        page_size: int = None,
        provider_id: int = None
    ):
        """
            叶子类目ID
        """
        self._leaf_cat_id = leaf_cat_id
        """
            当前页
        """
        self._current_page = current_page
        """
            每页大小
        """
        self._page_size = page_size
        """
            渠道Id，如0代表天猫，8代表淘宝
        """
        self._provider_id = provider_id

    @property
    def leaf_cat_id(self):
        return self._leaf_cat_id

    @leaf_cat_id.setter
    def leaf_cat_id(self, leaf_cat_id):
        if isinstance(leaf_cat_id, int):
            self._leaf_cat_id = leaf_cat_id
        else:
            raise TypeError("leaf_cat_id must be int")

    @property
    def current_page(self):
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        if isinstance(current_page, int):
            self._current_page = current_page
        else:
            raise TypeError("current_page must be int")

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
    def provider_id(self):
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        if isinstance(provider_id, int):
            self._provider_id = provider_id
        else:
            raise TypeError("provider_id must be int")


    def get_api_name(self):
        return "alibaba.gpu.schema.catsearch"

    def to_dict(self):
        request_dict = {}
        if self._leaf_cat_id is not None:
            request_dict["leaf_cat_id"] = convert_basic(self._leaf_cat_id)

        if self._current_page is not None:
            request_dict["current_page"] = convert_basic(self._current_page)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._provider_id is not None:
            request_dict["provider_id"] = convert_basic(self._provider_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


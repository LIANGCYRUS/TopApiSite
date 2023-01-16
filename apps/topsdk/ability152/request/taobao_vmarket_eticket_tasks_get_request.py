from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoVmarketEticketTasksGetRequest(BaseRequest):

    def __init__(
        self,
        seller_id: int = None,
        type: int = None,
        page_no: int = None,
        page_size: int = None,
        codemerchant_id: int = None
    ):
        """
            卖家家ID(信任卖家不必传，码商可选)
        """
        self._seller_id = seller_id
        """
            返回结果类型:
1:返回通知失败的订单
2.返回通知成功回调失败的订单
        """
        self._type = type
        """
            页码。取值范围:大于零的整数; 默认值:1
        """
        self._page_no = page_no
        """
            每页获取条数。默认值40，最小值1，最大值100。
        """
        self._page_size = page_size
        """
            码商ID，如果是码商，必须传，如果是信任卖家，不需要传
        """
        self._codemerchant_id = codemerchant_id

    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, seller_id):
        if isinstance(seller_id, int):
            self._seller_id = seller_id
        else:
            raise TypeError("seller_id must be int")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if isinstance(type, int):
            self._type = type
        else:
            raise TypeError("type must be int")

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
    def codemerchant_id(self):
        return self._codemerchant_id

    @codemerchant_id.setter
    def codemerchant_id(self, codemerchant_id):
        if isinstance(codemerchant_id, int):
            self._codemerchant_id = codemerchant_id
        else:
            raise TypeError("codemerchant_id must be int")


    def get_api_name(self):
        return "taobao.vmarket.eticket.tasks.get"

    def to_dict(self):
        request_dict = {}
        if self._seller_id is not None:
            request_dict["seller_id"] = convert_basic(self._seller_id)

        if self._type is not None:
            request_dict["type"] = convert_basic(self._type)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._codemerchant_id is not None:
            request_dict["codemerchant_id"] = convert_basic(self._codemerchant_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


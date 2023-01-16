from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsAddressRemoveRequest(BaseRequest):

    def __init__(
        self,
        contact_id: int = None
    ):
        """
            地址库ID
        """
        self._contact_id = contact_id

    @property
    def contact_id(self):
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        if isinstance(contact_id, int):
            self._contact_id = contact_id
        else:
            raise TypeError("contact_id must be int")


    def get_api_name(self):
        return "taobao.logistics.address.remove"

    def to_dict(self):
        request_dict = {}
        if self._contact_id is not None:
            request_dict["contact_id"] = convert_basic(self._contact_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


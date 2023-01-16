from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TmallItemIncrementUpdateSchemaGetRequest(BaseRequest):

    def __init__(
        self,
        item_id: int = None,
        xml_data: str = None
    ):
        """
            需要编辑的商品ID
        """
        self._item_id = item_id
        """
            如果入参xml_data指定了更新的字段，则只返回指定字段的规则（ISV如果功能性很强，如明确更新Title，请拼装好此字段以提升API整体性能）
        """
        self._xml_data = xml_data

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        if isinstance(item_id, int):
            self._item_id = item_id
        else:
            raise TypeError("item_id must be int")

    @property
    def xml_data(self):
        return self._xml_data

    @xml_data.setter
    def xml_data(self, xml_data):
        if isinstance(xml_data, str):
            self._xml_data = xml_data
        else:
            raise TypeError("xml_data must be str")


    def get_api_name(self):
        return "tmall.item.increment.update.schema.get"

    def to_dict(self):
        request_dict = {}
        if self._item_id is not None:
            request_dict["item_id"] = convert_basic(self._item_id)

        if self._xml_data is not None:
            request_dict["xml_data"] = convert_basic(self._xml_data)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


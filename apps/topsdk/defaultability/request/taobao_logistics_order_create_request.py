from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoLogisticsOrderCreateRequest(BaseRequest):

    def __init__(
        self,
        mail_no: str = None,
        seller_wangwang_id: str = None,
        order_type: int = None,
        logis_company_code: str = None,
        trade_id: int = None,
        is_consign: bool = None,
        logis_type: str = None,
        shipping: int = None,
        item_values: str = None,
        goods_names: str = None,
        goods_quantities: str = None
    ):
        """
            发货的物流公司运单号。在logis_type=OFFLINE且is_consign=true时，此项必填。
        """
        self._mail_no = mail_no
        """
            卖家旺旺号
        """
        self._seller_wangwang_id = seller_wangwang_id
        """
            物流发货类型：1-普通订单
不填为默认类型 1-普通订单
        """
        self._order_type = order_type
        """
            发货的物流公司代码，如申通=STO，圆通=YTO。is_consign=true时，此项必填。
        """
        self._logis_company_code = logis_company_code
        """
            订单的交易号码
        """
        self._trade_id = trade_id
        """
            创建订单同时是否进行发货，默认发货。
        """
        self._is_consign = is_consign
        """
            发货方式,默认为自己联系发货。可选值:ONLINE(在线下单)、OFFLINE(自己联系)。
        """
        self._logis_type = logis_type
        """
            运费承担方式。1为买家承担运费，2为卖家承担运费，其他值为错误参数。
        """
        self._shipping = shipping
        """
            运送货物的单价列表(注意：单位为分），用|号隔开
        """
        self._item_values = item_values
        """
            运送的货物名称列表，用|号隔开
        """
        self._goods_names = goods_names
        """
            运送货物的数量列表，用|号隔开
        """
        self._goods_quantities = goods_quantities

    @property
    def mail_no(self):
        return self._mail_no

    @mail_no.setter
    def mail_no(self, mail_no):
        if isinstance(mail_no, str):
            self._mail_no = mail_no
        else:
            raise TypeError("mail_no must be str")

    @property
    def seller_wangwang_id(self):
        return self._seller_wangwang_id

    @seller_wangwang_id.setter
    def seller_wangwang_id(self, seller_wangwang_id):
        if isinstance(seller_wangwang_id, str):
            self._seller_wangwang_id = seller_wangwang_id
        else:
            raise TypeError("seller_wangwang_id must be str")

    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        if isinstance(order_type, int):
            self._order_type = order_type
        else:
            raise TypeError("order_type must be int")

    @property
    def logis_company_code(self):
        return self._logis_company_code

    @logis_company_code.setter
    def logis_company_code(self, logis_company_code):
        if isinstance(logis_company_code, str):
            self._logis_company_code = logis_company_code
        else:
            raise TypeError("logis_company_code must be str")

    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        if isinstance(trade_id, int):
            self._trade_id = trade_id
        else:
            raise TypeError("trade_id must be int")

    @property
    def is_consign(self):
        return self._is_consign

    @is_consign.setter
    def is_consign(self, is_consign):
        if isinstance(is_consign, bool):
            self._is_consign = is_consign
        else:
            raise TypeError("is_consign must be bool")

    @property
    def logis_type(self):
        return self._logis_type

    @logis_type.setter
    def logis_type(self, logis_type):
        if isinstance(logis_type, str):
            self._logis_type = logis_type
        else:
            raise TypeError("logis_type must be str")

    @property
    def shipping(self):
        return self._shipping

    @shipping.setter
    def shipping(self, shipping):
        if isinstance(shipping, int):
            self._shipping = shipping
        else:
            raise TypeError("shipping must be int")

    @property
    def item_values(self):
        return self._item_values

    @item_values.setter
    def item_values(self, item_values):
        if isinstance(item_values, str):
            self._item_values = item_values
        else:
            raise TypeError("item_values must be str")

    @property
    def goods_names(self):
        return self._goods_names

    @goods_names.setter
    def goods_names(self, goods_names):
        if isinstance(goods_names, str):
            self._goods_names = goods_names
        else:
            raise TypeError("goods_names must be str")

    @property
    def goods_quantities(self):
        return self._goods_quantities

    @goods_quantities.setter
    def goods_quantities(self, goods_quantities):
        if isinstance(goods_quantities, str):
            self._goods_quantities = goods_quantities
        else:
            raise TypeError("goods_quantities must be str")


    def get_api_name(self):
        return "taobao.logistics.order.create"

    def to_dict(self):
        request_dict = {}
        if self._mail_no is not None:
            request_dict["mail_no"] = convert_basic(self._mail_no)

        if self._seller_wangwang_id is not None:
            request_dict["seller_wangwang_id"] = convert_basic(self._seller_wangwang_id)

        if self._order_type is not None:
            request_dict["order_type"] = convert_basic(self._order_type)

        if self._logis_company_code is not None:
            request_dict["logis_company_code"] = convert_basic(self._logis_company_code)

        if self._trade_id is not None:
            request_dict["trade_id"] = convert_basic(self._trade_id)

        if self._is_consign is not None:
            request_dict["is_consign"] = convert_basic(self._is_consign)

        if self._logis_type is not None:
            request_dict["logis_type"] = convert_basic(self._logis_type)

        if self._shipping is not None:
            request_dict["shipping"] = convert_basic(self._shipping)

        if self._item_values is not None:
            request_dict["item_values"] = convert_basic(self._item_values)

        if self._goods_names is not None:
            request_dict["goods_names"] = convert_basic(self._goods_names)

        if self._goods_quantities is not None:
            request_dict["goods_quantities"] = convert_basic(self._goods_quantities)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


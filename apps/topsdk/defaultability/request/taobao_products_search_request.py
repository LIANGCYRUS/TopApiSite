from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoProductsSearchRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        q: str = None,
        cid: int = None,
        props: str = None,
        status: str = None,
        page_no: int = None,
        page_size: int = None,
        vertical_market: int = None,
        customer_props: str = None,
        suite_items_str: str = None,
        barcode_str: str = None,
        market_id: str = None
    ):
        """
            需返回的字段列表.可选值:Product数据结构中的以下字段:product_id,name,pic_url,cid,props,price,tsc;多个字段之间用","分隔.新增字段status(product的当前状态)
        """
        self._fields = fields
        """
            搜索的关键词是用来搜索产品的title.　注:q,cid和props至少传入一个
        """
        self._q = q
        """
            商品类目ID.调用taobao.itemcats.get获取.
        """
        self._cid = cid
        """
            属性,属性值的组合.格式:pid:vid;pid:vid;调用taobao.itemprops.get获取类目属性pid 
,再用taobao.itempropvalues.get取得vid.
        """
        self._props = props
        """
            想要获取的产品的状态列表，支持多个状态并列获取，多个状态之间用","分隔，最多同时指定5种状态。例如，只获取小二确认的spu传入"3",只要商家确认的传入"0"，既要小二确认又要商家确认的传入"0,3"。目前只支持者两种类型的状态搜索，输入其他状态无效。
        """
        self._status = status
        """
            页码.传入值为1代表第一页,传入值为2代表第二页,依此类推.默认返回的数据是从第一页开始.
        """
        self._page_no = page_no
        """
            每页条数.每页返回最多返回100条,默认值为40.
        """
        self._page_size = page_size
        """
            传入值为：3表示3C表示3C垂直市场产品，4表示鞋城垂直市场产品，8表示网游垂直市场产品。一次只能指定一种垂直市场类型
        """
        self._vertical_market = vertical_market
        """
            用户自定义关键属性,结构：pid1:value1;pid2:value2，如果有型号，系列等子属性用: 隔开 例如：“20000:优衣库:型号:001;632501:1234”，表示“品牌:优衣库:型号:001;货号:1234”
        """
        self._customer_props = customer_props
        """
            按关联产品规格specs搜索套装产品
        """
        self._suite_items_str = suite_items_str
        """
            按条码搜索产品信息,多个逗号隔开，不支持条码为全零的方式
        """
        self._barcode_str = barcode_str
        """
            市场ID，1为取C2C市场的产品信息， 2为取B2C市场的产品信息。  不填写此值则默认取C2C的产品信息。
        """
        self._market_id = market_id

    @property
    def fields(self):
        return self._fields

    @fields.setter
    def fields(self, fields):
        if isinstance(fields, list):
            self._fields = fields
        else:
            raise TypeError("fields must be list")

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, q):
        if isinstance(q, str):
            self._q = q
        else:
            raise TypeError("q must be str")

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, cid):
        if isinstance(cid, int):
            self._cid = cid
        else:
            raise TypeError("cid must be int")

    @property
    def props(self):
        return self._props

    @props.setter
    def props(self, props):
        if isinstance(props, str):
            self._props = props
        else:
            raise TypeError("props must be str")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self._status = status
        else:
            raise TypeError("status must be str")

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
    def vertical_market(self):
        return self._vertical_market

    @vertical_market.setter
    def vertical_market(self, vertical_market):
        if isinstance(vertical_market, int):
            self._vertical_market = vertical_market
        else:
            raise TypeError("vertical_market must be int")

    @property
    def customer_props(self):
        return self._customer_props

    @customer_props.setter
    def customer_props(self, customer_props):
        if isinstance(customer_props, str):
            self._customer_props = customer_props
        else:
            raise TypeError("customer_props must be str")

    @property
    def suite_items_str(self):
        return self._suite_items_str

    @suite_items_str.setter
    def suite_items_str(self, suite_items_str):
        if isinstance(suite_items_str, str):
            self._suite_items_str = suite_items_str
        else:
            raise TypeError("suite_items_str must be str")

    @property
    def barcode_str(self):
        return self._barcode_str

    @barcode_str.setter
    def barcode_str(self, barcode_str):
        if isinstance(barcode_str, str):
            self._barcode_str = barcode_str
        else:
            raise TypeError("barcode_str must be str")

    @property
    def market_id(self):
        return self._market_id

    @market_id.setter
    def market_id(self, market_id):
        if isinstance(market_id, str):
            self._market_id = market_id
        else:
            raise TypeError("market_id must be str")


    def get_api_name(self):
        return "taobao.products.search"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._q is not None:
            request_dict["q"] = convert_basic(self._q)

        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._props is not None:
            request_dict["props"] = convert_basic(self._props)

        if self._status is not None:
            request_dict["status"] = convert_basic(self._status)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._vertical_market is not None:
            request_dict["vertical_market"] = convert_basic(self._vertical_market)

        if self._customer_props is not None:
            request_dict["customer_props"] = convert_basic(self._customer_props)

        if self._suite_items_str is not None:
            request_dict["suite_items_str"] = convert_basic(self._suite_items_str)

        if self._barcode_str is not None:
            request_dict["barcode_str"] = convert_basic(self._barcode_str)

        if self._market_id is not None:
            request_dict["market_id"] = convert_basic(self._market_id)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


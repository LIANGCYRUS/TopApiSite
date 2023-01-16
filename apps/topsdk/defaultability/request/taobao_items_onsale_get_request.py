from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoItemsOnsaleGetRequest(BaseRequest):

    def __init__(
        self,
        fields: list = None,
        q: str = None,
        cid: int = None,
        seller_cids: str = None,
        page_no: int = None,
        page_size: int = None,
        order_by: str = None,
        has_discount: bool = None,
        has_showcase: bool = None,
        is_taobao: bool = None,
        is_ex: bool = None,
        start_modified: datetime = None,
        end_modified: datetime = None,
        is_cspu: bool = None,
        is_combine: bool = None,
        auction_type: str = None
    ):
        """
            需返回的字段列表。可选值：Item商品结构体中的以下字段： approve_status,num_iid,title,nick,type,cid,pic_url,num,props,valid_thru,list_time,price,has_discount,has_invoice,has_warranty,has_showcase,modified,delist_time,postage_id,seller_cids,outer_id,sold_quantity ；字段之间用“,”分隔。不支持其他字段，如果需要获取其他字段数据，调用taobao.item.seller.get 获取。
        """
        self._fields = fields
        """
            搜索字段。搜索商品的title。
        """
        self._q = q
        """
            商品类目ID。ItemCat中的cid字段。可以通过taobao.itemcats.get取到
        """
        self._cid = cid
        """
            卖家店铺内自定义类目ID。多个之间用“,”分隔。可以根据taobao.sellercats.list.get获得.(<font color="red">注：目前最多支持32个ID号传入</font>)
        """
        self._seller_cids = seller_cids
        """
            页码。取值范围:大于零的整数。默认值为1,即默认返回第一页数据。用此接口获取数据时，当翻页获取的条数（page_no*page_size）超过10万,为了保护后台搜索引擎，接口将报错。所以请大家尽可能的细化自己的搜索条件，例如根据修改时间分段获取商品
        """
        self._page_no = page_no
        """
            每页条数。取值范围:大于零的整数;最大值：200；默认值：40。用此接口获取数据时，当翻页获取的条数（page_no*page_size）超过2万,为了保护后台搜索引擎，接口将报错。所以请大家尽可能的细化自己的搜索条件，例如根据修改时间分段获取商品
        """
        self._page_size = page_size
        """
            排序方式。格式为column:asc/desc ，column可选值:list_time(上架时间),delist_time(下架时间),num(商品数量)，modified(最近修改时间)，sold_quantity（商品销量）,;默认上架时间降序(即最新上架排在前面)。如按照上架时间降序排序方式为list_time:desc
        """
        self._order_by = order_by
        """
            是否参与会员折扣。可选值：true，false。默认不过滤该条件
        """
        self._has_discount = has_discount
        """
            是否橱窗推荐。 可选值：true，false。默认不过滤该条件
        """
        self._has_showcase = has_showcase
        """
            商品是否在淘宝显示
        """
        self._is_taobao = is_taobao
        """
            商品是否在外部网店显示
        """
        self._is_ex = is_ex
        """
            起始的修改时间
        """
        self._start_modified = start_modified
        """
            结束的修改时间
        """
        self._end_modified = end_modified
        """
            是否挂接了达尔文标准产品体系
        """
        self._is_cspu = is_cspu
        """
            组合商品
        """
        self._is_combine = is_combine
        """
            商品类型：a-拍卖,b-一口价
        """
        self._auction_type = auction_type

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
    def seller_cids(self):
        return self._seller_cids

    @seller_cids.setter
    def seller_cids(self, seller_cids):
        if isinstance(seller_cids, str):
            self._seller_cids = seller_cids
        else:
            raise TypeError("seller_cids must be str")

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
    def order_by(self):
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        if isinstance(order_by, str):
            self._order_by = order_by
        else:
            raise TypeError("order_by must be str")

    @property
    def has_discount(self):
        return self._has_discount

    @has_discount.setter
    def has_discount(self, has_discount):
        if isinstance(has_discount, bool):
            self._has_discount = has_discount
        else:
            raise TypeError("has_discount must be bool")

    @property
    def has_showcase(self):
        return self._has_showcase

    @has_showcase.setter
    def has_showcase(self, has_showcase):
        if isinstance(has_showcase, bool):
            self._has_showcase = has_showcase
        else:
            raise TypeError("has_showcase must be bool")

    @property
    def is_taobao(self):
        return self._is_taobao

    @is_taobao.setter
    def is_taobao(self, is_taobao):
        if isinstance(is_taobao, bool):
            self._is_taobao = is_taobao
        else:
            raise TypeError("is_taobao must be bool")

    @property
    def is_ex(self):
        return self._is_ex

    @is_ex.setter
    def is_ex(self, is_ex):
        if isinstance(is_ex, bool):
            self._is_ex = is_ex
        else:
            raise TypeError("is_ex must be bool")

    @property
    def start_modified(self):
        return self._start_modified

    @start_modified.setter
    def start_modified(self, start_modified):
        if isinstance(start_modified, datetime):
            self._start_modified = start_modified
        else:
            raise TypeError("start_modified must be datetime")

    @property
    def end_modified(self):
        return self._end_modified

    @end_modified.setter
    def end_modified(self, end_modified):
        if isinstance(end_modified, datetime):
            self._end_modified = end_modified
        else:
            raise TypeError("end_modified must be datetime")

    @property
    def is_cspu(self):
        return self._is_cspu

    @is_cspu.setter
    def is_cspu(self, is_cspu):
        if isinstance(is_cspu, bool):
            self._is_cspu = is_cspu
        else:
            raise TypeError("is_cspu must be bool")

    @property
    def is_combine(self):
        return self._is_combine

    @is_combine.setter
    def is_combine(self, is_combine):
        if isinstance(is_combine, bool):
            self._is_combine = is_combine
        else:
            raise TypeError("is_combine must be bool")

    @property
    def auction_type(self):
        return self._auction_type

    @auction_type.setter
    def auction_type(self, auction_type):
        if isinstance(auction_type, str):
            self._auction_type = auction_type
        else:
            raise TypeError("auction_type must be str")


    def get_api_name(self):
        return "taobao.items.onsale.get"

    def to_dict(self):
        request_dict = {}
        if self._fields is not None:
            request_dict["fields"] = convert_basic_list(self._fields)

        if self._q is not None:
            request_dict["q"] = convert_basic(self._q)

        if self._cid is not None:
            request_dict["cid"] = convert_basic(self._cid)

        if self._seller_cids is not None:
            request_dict["seller_cids"] = convert_basic(self._seller_cids)

        if self._page_no is not None:
            request_dict["page_no"] = convert_basic(self._page_no)

        if self._page_size is not None:
            request_dict["page_size"] = convert_basic(self._page_size)

        if self._order_by is not None:
            request_dict["order_by"] = convert_basic(self._order_by)

        if self._has_discount is not None:
            request_dict["has_discount"] = convert_basic(self._has_discount)

        if self._has_showcase is not None:
            request_dict["has_showcase"] = convert_basic(self._has_showcase)

        if self._is_taobao is not None:
            request_dict["is_taobao"] = convert_basic(self._is_taobao)

        if self._is_ex is not None:
            request_dict["is_ex"] = convert_basic(self._is_ex)

        if self._start_modified is not None:
            request_dict["start_modified"] = convert_basic(self._start_modified)

        if self._end_modified is not None:
            request_dict["end_modified"] = convert_basic(self._end_modified)

        if self._is_cspu is not None:
            request_dict["is_cspu"] = convert_basic(self._is_cspu)

        if self._is_combine is not None:
            request_dict["is_combine"] = convert_basic(self._is_combine)

        if self._auction_type is not None:
            request_dict["auction_type"] = convert_basic(self._auction_type)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


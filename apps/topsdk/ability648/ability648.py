from topsdk.client import TopApiClient, BaseRequest

class Ability648:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        更新商品信息
    """
    def taobao_item_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        添加SKU
    """
    def taobao_item_sku_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新SKU信息
    """
    def taobao_item_sku_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询卖家已卖出的交易数据（根据创建时间）
    """
    def taobao_trades_sold_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取单笔交易的部分信息(性能高)
    """
    def taobao_trade_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        对一笔交易添加备注
    """
    def taobao_trade_memo_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改交易备注
    """
    def taobao_trade_memo_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取单笔交易的详细信息
    """
    def taobao_trade_fullinfo_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询地址区域
    """
    def taobao_areas_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取交易确认收货费用
    """
    def taobao_trade_confirmfee_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        物流流转信息查询
    """
    def taobao_logistics_trace_search(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询物流公司信息
    """
    def taobao_logistics_companies_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        批量查询物流订单,返回详细信息
    """
    def taobao_logistics_orders_detail_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        批量查询物流订单
    """
    def taobao_logistics_orders_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新交易的销售属性
    """
    def taobao_trade_ordersku_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        交易帐务查询
    """
    def taobao_trade_amount_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更改交易的收货地址
    """
    def taobao_trade_shippingaddress_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询支持起始地到目的地范围的物流公司
    """
    def taobao_logistics_partners_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        延长交易收货时间
    """
    def taobao_trade_receivetime_delay(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询卖家地址库
    """
    def taobao_logistics_address_search(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        删除卖家地址库
    """
    def taobao_logistics_address_remove(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        卖家地址库修改
    """
    def taobao_logistics_address_modify(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        卖家地址库新增接口
    """
    def taobao_logistics_address_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        取消物流订单接口
    """
    def taobao_logistics_online_cancel(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        无需物流（虚拟）发货处理
    """
    def taobao_logistics_dummy_send(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        限时打折详情查询
    """
    def taobao_promotion_limitdiscount_detail_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        定向优惠活动名称与描述违禁词检查
    """
    def taobao_marketing_promotion_kfc(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改交易邮费价格
    """
    def taobao_trade_postage_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取用户指定运费模板信息
    """
    def taobao_delivery_template_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取用户下所有模板
    """
    def taobao_delivery_templates_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        删除运费模板
    """
    def taobao_delivery_template_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        新增运费模板
    """
    def taobao_delivery_template_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改运费模板
    """
    def taobao_delivery_template_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新商品价格
    """
    def taobao_item_price_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新商品SKU的价格
    """
    def taobao_item_sku_price_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

from topsdk.client import TopApiClient, BaseRequest

class Ability149:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        渠道中心-查询产品列表
    """
    def tmall_channel_products_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品库存修改
    """
    def taobao_fenxiao_product_quantity_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据outerCode查询商品
    """
    def taobao_scitem_outercode_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据id查询商品
    """
    def taobao_scitem_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询后端商品
    """
    def taobao_scitem_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        发布后端商品
    """
    def taobao_scitem_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        失效指定用户的商品与后端商品的映射关系
    """
    def taobao_scitem_map_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查找IC商品或分销商品与后端商品的关联信息
    """
    def taobao_scitem_map_query(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        创建IC商品与后端商品的映射关系
    """
    def taobao_scitem_map_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        交易库存调整单
    """
    def taobao_inventory_adjust_trade(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        非交易库存调整单
    """
    def taobao_inventory_adjust_external(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        库存初始化
    """
    def taobao_inventory_initial(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询商品库存信息
    """
    def taobao_inventory_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        合作申请查询
    """
    def taobao_fenxiao_requisitions_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        等级折扣查询
    """
    def taobao_fenxiao_product_gradeprice_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        删除产品线
    """
    def taobao_fenxiao_productcat_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改产品线
    """
    def taobao_fenxiao_productcat_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        新增产品线
    """
    def taobao_fenxiao_productcat_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        导入商品生成产品
    """
    def taobao_fenxiao_product_import_from_auction(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品库存初始化
    """
    def taobao_inventory_initial_item(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品导入到渠道
    """
    def taobao_fenxiao_product_to_channel_import(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询供应商的产品数据
    """
    def tmall_channel_products_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        创建经销采购申请
    """
    def taobao_fenxiao_dealer_requisitionorder_create(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        地点关联关系增量编辑
    """
    def taobao_location_relation_edit(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        地点关联关系查询
    """
    def taobao_location_relation_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        货品库存商家端调整
    """
    def taobao_inventory_merchant_adjust(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询采购单退款信息
    """
    def taobao_fenxiao_refund_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分销商查询产品信息
    """
    def taobao_fenxiao_distributor_products_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        批量查询采购退款
    """
    def taobao_fenxiao_refund_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        供应商/分销商关闭采购申请/经销采购单
    """
    def taobao_fenxiao_dealer_requisitionorder_close(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        供应商/分销商通过采购申请/经销采购单申请
    """
    def taobao_fenxiao_dealer_requisitionorder_agree(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        批量查询采购申请/经销采购单
    """
    def taobao_fenxiao_dealer_requisitionorder_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        按编号查询采购申请/经销采购单
    """
    def taobao_fenxiao_dealer_requisitionorder_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分页查询商家仓信息
    """
    def taobao_inventory_warehouse_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        创建商家仓或者更新商家仓信息
    """
    def taobao_inventory_warehouse_manage(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询商品销售区域
    """
    def taobao_region_sale_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        创建渠道分销单
    """
    def tmall_channel_trade_order_create(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        线下预存款流水增加
    """
    def taobao_fenxiao_trade_prepay_offline_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        渠道分销供应商上传线下流水预存款（减少）
    """
    def taobao_fenxiao_trade_prepay_offline_reduce(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据sku设置折扣价
    """
    def taobao_fenxiao_product_gradeprice_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分销商查询产品库存
    """
    def taobao_fenxiao_distributor_product_quantity_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改经销采购单备注
    """
    def taobao_fenxiao_dealer_requisitionorder_remark_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

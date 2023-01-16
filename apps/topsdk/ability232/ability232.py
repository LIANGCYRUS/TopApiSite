from topsdk.client import TopApiClient, BaseRequest

class Ability232:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        查询单据列表
    """
    def taobao_wlb_wms_cainiao_bill_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取销售订单发货信息
    """
    def taobao_wlb_wms_consign_bill_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        通过订单列表批量获取库存损益单信息
    """
    def taobao_wlb_wms_inventory_profitloss_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询组合商品的组合关系
    """
    def taobao_wlb_wms_item_combination_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        菜鸟商品库存查询
    """
    def taobao_wlb_wms_inventory_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询家装服务商列表
    """
    def taobao_wlb_order_jzpartner_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        驱动保税交易订单发货
    """
    def cainiao_bim_tradeorder_consign(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品信息查询
    """
    def taobao_wlb_wms_sku_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        按照日期范围查询物流订单详情
    """
    def taobao_wlb_orderdetail_date_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询单据序列号信息
    """
    def taobao_wlb_wms_sn_info_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        入库通知单
    """
    def taobao_wlb_wms_stock_in_order_notify(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        发货订单通知
    """
    def taobao_wlb_wms_consign_order_notify(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        单据取消接口
    """
    def taobao_wlb_wms_order_cancel_notify(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品同步
    """
    def taobao_wlb_wms_sku_create(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

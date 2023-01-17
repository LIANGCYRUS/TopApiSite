from topsdk.client import TopApiClient, BaseRequest

class Ability448:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        一般进口发货
    """
    def taobao_wlb_imports_general_consign(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        一般进口取消物流订单
    """
    def taobao_wlb_imports_order_cancel(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        集货鉴定结果
    """
    def taobao_wlb_imports_vas_identity_result(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取所有服务列表
    """
    def taobao_wlb_imports_resource_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据指定的资源获取所有中转仓列表
    """
    def taobao_wlb_imports_resource_transferstore_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取运单信息
    """
    def taobao_wlb_imports_waybill_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        集货商家pdf和云打印面单获取，pdf需要配置白名单
    """
    def taobao_wlb_crossborder_waybill_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        物流订单获取
    """
    def taobao_wlb_imports_order_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

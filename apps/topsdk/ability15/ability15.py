from topsdk.client import TopApiClient, BaseRequest

class Ability15:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        商家按照仓的类型获取仓库接口
    """
    def taobao_wlb_stores_baseinfo_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        创建订单并发货
    """
    def taobao_logistics_consign_order_createandsend(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())

from topsdk.client import TopApiClient, BaseRequest

class Ability236:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        ToB仓储发货
    """
    def taobao_uop_tob_order_create(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        云打印客户端更新配置服务
    """
    def cainiao_waybillprint_clientupdate_getconfig(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        自定义区内容更新
    """
    def cainiao_cloudprint_customarea_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商家库存调整
    """
    def cainiao_merchant_inventory_adjust(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        快递改约api
    """
    def taobao_logistics_express_modify_appoint(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

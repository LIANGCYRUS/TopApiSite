from topsdk.client import TopApiClient, BaseRequest

class Ability447:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        3PL直邮获取资源列表
    """
    def taobao_wlb_import_threepl_resource_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        3PL直邮线下发货
    """
    def taobao_wlb_import_threepl_offline_consign(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

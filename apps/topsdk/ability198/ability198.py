from topsdk.client import TopApiClient, BaseRequest

class Ability198:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        物流详情查询
    """
    def taobao_logistics_instant_trace_search(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

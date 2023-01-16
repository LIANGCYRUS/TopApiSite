from topsdk.client import TopApiClient, BaseRequest

class Ability3087:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        网关一次性token获取
    """
    def taobao_top_once_token_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

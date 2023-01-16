from topsdk.client import TopApiClient, BaseRequest

class Ability306:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        根据子账号登录名后缀模糊搜索子账号列表
    """
    def taobao_subusers_subaccount_search(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

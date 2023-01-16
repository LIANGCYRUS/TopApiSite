from topsdk.client import TopApiClient, BaseRequest

class Ability314:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        删除数据推送用户
    """
    def taobao_jushita_jdp_user_delete(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        添加数据推送用户
    """
    def taobao_jushita_jdp_user_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取开通的订单同步服务的用户
    """
    def taobao_jushita_jdp_users_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())

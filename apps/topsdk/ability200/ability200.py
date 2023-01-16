from topsdk.client import TopApiClient, BaseRequest

class Ability200:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        查询退款状态
    """
    def taobao_refund_status_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        卖家发起拦截
    """
    def taobao_rp_refund_intercept(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        协商退货退款
    """
    def taobao_refund_negotiatereturn(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        协商退货退款渲染
    """
    def taobao_refund_negotiatereturn_render(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        退款详情页渲染
    """
    def taobao_refund_detail_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

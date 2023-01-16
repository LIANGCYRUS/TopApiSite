from topsdk.client import TopApiClient, BaseRequest

class Ability6:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        天猫逆向纠纷查询
    """
    def tmall_dispute_receive_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        审核退款单
    """
    def taobao_rp_refund_review(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        卖家回填物流信息
    """
    def taobao_rp_returngoods_refill(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        卖家拒绝退货
    """
    def taobao_rp_returngoods_refuse(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取拒绝原因列表
    """
    def taobao_refund_refusereason_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        特殊部分退纠纷单查询
    """
    def taobao_special_refund_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        特殊退款类型的纠纷单列表查询
    """
    def taobao_special_refunds_receive_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

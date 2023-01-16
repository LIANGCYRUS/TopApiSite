from topsdk.client import TopApiClient, BaseRequest

class Ability147:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        产品信息获取schema获取
    """
    def tmall_product_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品hscode信息审核状态查询接口
    """
    def tmall_item_hscode_audit_results_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫发布商品规则获取
    """
    def tmall_item_add_simpleschema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品更新规则获取接口
    """
    def tmall_product_update_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品更新接口
    """
    def tmall_product_schema_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        算法获取hscode
    """
    def tmall_item_calculate_hscode_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        通过hscode获取计量单位
    """
    def tmall_item_hscode_detail_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

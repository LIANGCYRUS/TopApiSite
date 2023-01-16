from topsdk.client import TopApiClient, BaseRequest

class Ability213:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        组合商品获取接口
    """
    def tmall_item_combine_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取产品发布规则接口
    """
    def alibaba_gpu_add_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        使用schema文件发布产品
    """
    def alibaba_gpu_schema_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取产品编辑schema规则的接口
    """
    def alibaba_gpu_update_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品更新接口
    """
    def alibaba_gpu_schema_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        按类目查询spu接口
    """
    def alibaba_gpu_schema_catsearch(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

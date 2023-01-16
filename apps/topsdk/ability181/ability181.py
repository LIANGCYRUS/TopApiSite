from topsdk.client import TopApiClient, BaseRequest

class Ability181:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        查询商品类目属性变更
    """
    def taobao_item_catprops_modification_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

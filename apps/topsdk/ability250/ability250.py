from topsdk.client import TopApiClient, BaseRequest

class Ability250:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        卖家店铺基础信息查询
    """
    def taobao_shop_seller_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

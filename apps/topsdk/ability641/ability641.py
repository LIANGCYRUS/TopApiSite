from topsdk.client import TopApiClient, BaseRequest

class Ability641:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        查询某个卖家的店铺优惠券领取活动
    """
    def taobao_promotion_activity_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询卖家优惠券
    """
    def taobao_promotion_coupons_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        搭配套餐查询
    """
    def taobao_promotion_meal_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

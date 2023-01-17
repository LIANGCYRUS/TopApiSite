from topsdk.client import TopApiClient, BaseRequest

class Ability193:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        获取订单应开票金额
    """
    def taobao_trade_invoice_amount_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

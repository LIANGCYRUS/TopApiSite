from topsdk.client import TopApiClient, BaseRequest

class Ability152:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        任务列表获取接口
    """
    def taobao_vmarket_eticket_tasks_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        主动发起通知接口
    """
    def taobao_vmarket_eticket_manage_notify(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取电子凭证预约门店信息
    """
    def taobao_vmarket_eticket_store_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        码商二维码图片上传
    """
    def taobao_vmarket_eticket_qrcode_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子凭证冲正接口
    """
    def taobao_eticket_merchant_ma_reverse(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        码商上传二维码图片
    """
    def taobao_eticket_merchant_img_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子凭证核销前校验接口
    """
    def taobao_eticket_merchant_ma_available(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子凭证核销接口
    """
    def taobao_eticket_merchant_ma_consume(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子凭证重发回调接口
    """
    def taobao_eticket_merchant_ma_resend(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        码商发码失败回调接口
    """
    def taobao_eticket_merchant_ma_failsend(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        码商发码成功回调接口
    """
    def taobao_eticket_merchant_ma_send(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        业务重新触发发码短信
    """
    def taobao_vmarket_eticket_flow_resend(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        无交易类凭证核销
    """
    def taobao_vmarket_eticket_flow_consume(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        核销放行的查询接口
    """
    def taobao_vmarket_eticket_auth_beforeconsume(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        核销放行的核销接口
    """
    def taobao_vmarket_eticket_auth_consume(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        无法发码回调
    """
    def taobao_vmarket_eticket_failsend(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        订单延时接口
    """
    def taobao_vmarket_eticket_time_expand(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        电子凭证验码前置确认
    """
    def taobao_vmarket_eticket_beforeconsume(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子票券消费通知
    """
    def taobao_vmarket_eticket_consume(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        外部合作商家重发电子凭证回调接口
    """
    def taobao_vmarket_eticket_resend(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商家电子凭证发码成功回调接口
    """
    def taobao_vmarket_eticket_send(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子凭证冲正接口
    """
    def taobao_vmarket_eticket_reverse(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子凭证码列表查询
    """
    def taobao_vmarket_eticket_codes_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        电子凭证操作日志查询
    """
    def taobao_vmarket_eticket_oplogs_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

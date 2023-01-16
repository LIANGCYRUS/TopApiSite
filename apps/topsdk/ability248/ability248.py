from topsdk.client import TopApiClient, BaseRequest

class Ability248:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        获取文件上传token
    """
    def taobao_picture_token(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

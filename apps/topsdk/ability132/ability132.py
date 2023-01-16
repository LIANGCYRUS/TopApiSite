from topsdk.client import TopApiClient, BaseRequest

class Ability132:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        TMC授权token
    """
    def taobao_tmc_auth_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        批量发送消息
    """
    def taobao_tmc_messages_produce(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取自定义用户分组列表
    """
    def taobao_tmc_groups_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        删除指定的分组或分组下的用户
    """
    def taobao_tmc_group_delete(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        为已开通用户添加用户分组
    """
    def taobao_tmc_group_add(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        确认消费消息的状态
    """
    def taobao_tmc_messages_confirm(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        消费多条消息
    """
    def taobao_tmc_messages_consume(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        删除消息topic分组路由
    """
    def taobao_tmc_topic_group_delete(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        topic分组路由
    """
    def taobao_tmc_topic_group_add(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())

from topsdk.client import TopApiClient, BaseRequest

class Ability138:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        taobao.item.update.delisting.tmall
    """
    def taobao_item_update_delisting_tmall(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫简化编辑商品
    """
    def tmall_item_simpleschema_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫商品/SKU库存更新接口
    """
    def tmall_item_quantity_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        taobao.item.update.listing天猫分流
    """
    def taobao_item_update_listing_tmall(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品描述模块信息获取
    """
    def tmall_item_desc_modules_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取天猫商品尺码表模板列表
    """
    def tmall_item_sizemapping_templates_list(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取天猫商品尺码表模板
    """
    def tmall_item_sizemapping_template_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        删除天猫商品尺码表模板
    """
    def tmall_item_sizemapping_template_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新天猫商品尺码表模板
    """
    def tmall_item_sizemapping_template_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        新增天猫商品尺码表模板
    """
    def tmall_item_sizemapping_template_create(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新商品发货时间
    """
    def tmall_item_shiptime_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫简化发布商品
    """
    def tmall_item_simpleschema_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        发品资质校验
    """
    def taobao_item_permit_check(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

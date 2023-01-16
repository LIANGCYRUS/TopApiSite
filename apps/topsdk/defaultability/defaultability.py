from topsdk.client import TopApiClient, BaseRequest

class Defaultability:

    def __init__(self, client: TopApiClient):
        self._client = client

    """
        获取一个产品的信息
    """
    def taobao_product_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        搜索产品信息
    """
    def taobao_products_search(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        上传一个产品，不包括产品非主图和属性图片
    """
    def taobao_product_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        上传单张产品非主图，如果需要传多张，可调多次
    """
    def taobao_product_img_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        上传单张产品属性图片，如果需要传多张，可调多次
    """
    def taobao_product_propimg_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改一个产品，可以修改主图，不能修改子图片
    """
    def taobao_product_update(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取产品列表
    """
    def taobao_products_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取标准类目属性值
    """
    def taobao_itempropvalues_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        批量判定服务是否可达
    """
    def taobao_logistics_address_reachablebatch_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取当前会话用户出售中的商品列表
    """
    def taobao_items_onsale_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        添加一个商品
    """
    def taobao_item_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        添加商品图片
    """
    def taobao_item_img_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        删除商品图片
    """
    def taobao_item_img_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        删除属性图片
    """
    def taobao_item_propimg_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取用户已开通消息
    """
    def taobao_tmc_user_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        添加或修改属性图片
    """
    def taobao_item_propimg_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取SKU
    """
    def taobao_item_sku_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据商品ID列表获取SKU信息
    """
    def taobao_item_skus_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取单个商品详细信息
    """
    def taobao_item_seller_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        批量获取商品详细信息
    """
    def taobao_items_seller_list_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询买家申请的退款列表
    """
    def taobao_refunds_apply_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取单笔退款详情
    """
    def taobao_refund_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取前台展示的店铺类目
    """
    def taobao_shopcats_list_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取前台展示的店铺内卖家自定义商品类目
    """
    def taobao_sellercats_list_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取标准商品类目属性
    """
    def taobao_itemprops_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取后台供卖家发布商品的标准商品类目
    """
    def taobao_itemcats_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        查询退款留言/凭证列表
    """
    def taobao_refund_messages_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        创建退款留言/凭证
    """
    def taobao_refund_message_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取图片分类信息
    """
    def taobao_picture_category_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        服务平台营销链接生成接口
    """
    def taobao_fuwu_sale_link_gen(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        获取图片信息
    """
    def taobao_picture_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        上传单张图片
    """
    def taobao_picture_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        关键词过滤匹配
    """
    def taobao_kfc_keyword_search(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品关联子图
    """
    def taobao_item_joint_img(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品关联属性图
    """
    def taobao_item_joint_propimg(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询商家被授权品牌列表和类目列表
    """
    def taobao_itemcats_authorize_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        得到当前会话用户库存中的商品列表
    """
    def taobao_items_inventory_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据外部ID取商品SKU
    """
    def taobao_skus_custom_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取指定账户的子账号简易信息列表
    """
    def taobao_subusers_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取指定账户子账号的详细信息
    """
    def taobao_subuser_fullinfo_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取指定账户的所有部门列表
    """
    def taobao_subuser_departments_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取指定账户的所有职务信息列表
    """
    def taobao_subuser_dutys_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改指定账户子账号的基本信息
    """
    def taobao_subuser_info_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        新增图片分类信息
    """
    def taobao_picture_category_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫增量更新商品规则获取
    """
    def tmall_item_increment_update_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫根据规则增量更新商品
    """
    def tmall_item_schema_increment_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品编辑增量更新
    """
    def alibaba_item_edit_fastupdate(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询appstore应用订购关系
    """
    def taobao_appstore_subscribe_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        删除SKU
    """
    def taobao_item_sku_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        添加产品
    """
    def taobao_fenxiao_product_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新产品
    """
    def taobao_fenxiao_product_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询产品线列表
    """
    def taobao_fenxiao_productcats_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询产品列表
    """
    def taobao_fenxiao_products_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新合作关系等级
    """
    def taobao_fenxiao_cooperation_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分销商等级查询
    """
    def taobao_fenxiao_grades_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取折扣信息
    """
    def taobao_fenxiao_discounts_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商家配送核销
    """
    def alibaba_ascp_logistics_seller_writeoff(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商家配送发货
    """
    def alibaba_ascp_logistics_seller_send(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商家配送核销订单列表查询
    """
    def alibaba_ascp_logistics_seller_orders_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        订购关系查询
    """
    def taobao_vas_subscribe_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        订单记录导出
    """
    def taobao_vas_order_search(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        订购记录导出
    """
    def taobao_vas_subsc_search(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        宝贝/SKU库存修改
    """
    def taobao_item_quantity_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        物流宝订单已发货通知接口
    """
    def taobao_wlb_order_consign(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        物流宝通知消息查询接口
    """
    def taobao_wlb_notify_message_page_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新商品条形码信息
    """
    def taobao_item_barcode_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        通过物流订单编号查询物流信息
    """
    def taobao_wlb_tmsorder_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据物流宝商品ID查询商品映射关系
    """
    def taobao_wlb_item_map_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据商品id查询商品组合关系
    """
    def taobao_wlb_item_combination_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据商品ID查询所有库存变更记录
    """
    def taobao_wlb_inventorylog_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        物流宝商品修改
    """
    def taobao_wlb_item_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询商家定购的所有服务
    """
    def taobao_wlb_subscription_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分页查询物流宝订单
    """
    def taobao_wlb_order_page_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分页查询物流宝订单商品详情
    """
    def taobao_wlb_orderitem_page_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        物流宝订单流转状态查询
    """
    def taobao_wlb_orderstatus_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        取消物流宝订单
    """
    def taobao_wlb_order_cancel(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据商品ID获取商品信息
    """
    def taobao_wlb_item_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据交易号获取物流宝订单
    """
    def taobao_wlb_tradeorder_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询库存详情
    """
    def taobao_wlb_inventory_detail_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        创建物流宝订单
    """
    def taobao_wlb_order_create(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分页查询商品
    """
    def taobao_wlb_item_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据物流宝订单编号查询物流宝订单概要信息
    """
    def taobao_wlb_wlborder_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        添加单个物流宝商品
    """
    def taobao_wlb_item_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        拆合单结果回传接口
    """
    def taobao_fulfillment_order_assemble(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        确认收款
    """
    def taobao_fenxiao_order_confirm_paid(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询商品下载记录
    """
    def taobao_fenxiao_distributor_items_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        供应商或分销商获取合作关系信息
    """
    def taobao_fenxiao_cooperation_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取用户宝贝详情页模板名称
    """
    def taobao_item_templates_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取商家可发布商品的市场信息
    """
    def alibaba_item_publish_market_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据收件人信息查询交易单号
    """
    def taobao_trades_sold_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        发布单条消息
    """
    def taobao_tmc_message_produce(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        取消用户的消息服务
    """
    def taobao_tmc_user_cancel(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        为已授权的用户开通消息服务
    """
    def taobao_tmc_user_permit(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫商品/SKU商家编码更新接口
    """
    def tmall_item_outerid_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询指定账户的子账号列表
    """
    def taobao_sellercenter_subusers_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取指定用户的权限集合
    """
    def taobao_sellercenter_user_permissions_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取商品已生效营销活动更新规则
    """
    def taobao_item_promotion_rule_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取分销用户登录信息
    """
    def taobao_fenxiao_login_user_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询指定的子账号的权限和角色信息
    """
    def taobao_sellercenter_subuser_permissions_roles_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取指定卖家的角色列表
    """
    def taobao_sellercenter_roles_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        子账号角色的新增（指定卖家）
    """
    def taobao_sellercenter_role_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        服务平台评价查询接口
    """
    def taobao_fuwu_scores_get(self, request: BaseRequest):
        return self._client.execute(request.get_api_name(), request.to_dict(), request.get_file_param_dict())
    """
        外部库存变化通知（企业物流用户使用）
    """
    def taobao_wlb_out_inventory_change_notify(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        自己联系物流发货
    """
    def alibaba_ascp_logistics_offline_send(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改物流公司和运单号
    """
    def alibaba_ascp_logistics_consign_resend(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        更新图片分类
    """
    def taobao_picture_category_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        替换图片
    """
    def taobao_picture_replace(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        修改图片名字
    """
    def taobao_picture_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询图片空间用户的信息
    """
    def taobao_picture_userinfo_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        图片是否被引用
    """
    def taobao_picture_isreferenced_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        SKU库存修改
    """
    def taobao_skus_quantity_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取商品发布规则信息
    """
    def alibaba_item_publish_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫商品/SKU价格更新接口
    """
    def tmall_item_price_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品SKU删除接口
    """
    def taobao_fenxiao_product_sku_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品sku添加接口
    """
    def taobao_fenxiao_product_sku_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品sku编辑接口
    """
    def taobao_fenxiao_product_sku_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        SKU查询接口
    """
    def taobao_fenxiao_product_skus_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品图片上传
    """
    def taobao_fenxiao_product_image_upload(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品图片删除
    """
    def taobao_fenxiao_product_image_delete(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品发布
    """
    def alibaba_item_publish_submit(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品编辑获取schema信息
    """
    def alibaba_item_edit_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品编辑提交schema信息
    """
    def alibaba_item_edit_submit(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品下架
    """
    def alibaba_item_operate_downshelf(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品上架
    """
    def alibaba_item_operate_upshelf(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        商品级联属性信息获取
    """
    def alibaba_item_publish_props_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫根据规则发布商品
    """
    def tmall_item_schema_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫发布商品规则获取
    """
    def tmall_item_add_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        产品发布规则获取接口
    """
    def tmall_product_add_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        批次库存查询接口
    """
    def taobao_wlb_item_batch_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取匹配产品规则
    """
    def tmall_product_match_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        product匹配接口
    """
    def tmall_product_schema_match(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        使用Schema文件发布一个产品
    """
    def tmall_product_schema_add(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        通过主账号登陆态分页查询子账号列表
    """
    def taobao_sellercenter_subusers_page(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        创建物流订单
    """
    def taobao_logistics_order_create(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        分页获取指定账户的子账号简易信息列表（新isv建议使用taobao.sellercenter.subusers.page接口）
    """
    def taobao_subusers_page(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫根据规则编辑商品
    """
    def tmall_item_schema_update(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        天猫编辑商品规则获取
    """
    def tmall_item_update_schema_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        根据当前子账号登陆态，获取该子账号基本信息
    """
    def taobao_subusers_info_query(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        获取可用宝贝描述规范化模块
    """
    def taobao_item_anchor_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        同意退款
    """
    def taobao_rp_refunds_agree(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        卖家同意退货
    """
    def taobao_rp_returngoods_agree(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        查询卖家已卖出的增量交易数据（根据入库时间）
    """
    def taobao_trades_sold_incrementv_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        图片获取
    """
    def taobao_picture_pictures_get(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)
    """
        图片总数查询
    """
    def taobao_picture_pictures_count(self, request: BaseRequest, session: str):
        return self._client.execute_with_session(request.get_api_name(), request.to_dict(), request.get_file_param_dict(), session)

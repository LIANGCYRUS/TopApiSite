from django.http import JsonResponse
from django.shortcuts import render
# ***** TIO API SDK 开始***** #
from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView

from topsdk.client import TopApiClient, TopException
from topsdk.ability648.ability648 import Ability648
from topsdk.ability648.request.taobao_trades_sold_get_request import *
from topsdk.ability648.request.taobao_logistics_trace_search_request import *

# ***** TIO API SDK 结束***** #


def wuliu(self, tid):
    APPKEY = '34254070'
    APP_SERCET = '04b84ea6492167a891f5ebff687153c9'
    API_URL = 'https://eco.taobao.com/router/rest'
    STORE_SESSION = '6100c2308ad14dff9b9ae7e8878e9a5100635a1b9a3602a2212314430335'

    # create Client
    client = TopApiClient(appkey=APPKEY, app_sercet=APP_SERCET, top_gateway_url=API_URL, verify_ssl=False)
    ability = Ability648(client=client)

    # create domain

    # create request
    request = TaobaoLogisticsTraceSearchRequest()
    request.tid = tid
    request.is_split = 1
    """
        1,2,3
    """
    request.sub_tid = []
    try:
        response = ability.taobao_logistics_trace_search(request, STORE_SESSION)
        return JsonResponse(response)
        print(response)
    except TopException as e:
        return JsonResponse(e)



def TmgAllOrderAPIview(self):
    # 淘宝开发平台的基本信息：
    APPKEY = '34254070'
    APP_SERCET = '04b84ea6492167a891f5ebff687153c9'
    API_URL = 'https://eco.taobao.com/router/rest'
    STORE_SESSION = '6100c2308ad14dff9b9ae7e8878e9a5100635a1b9a3602a2212314430335'

    # create Client
    client = TopApiClient(appkey=APPKEY, app_sercet=APP_SERCET, top_gateway_url=API_URL, verify_ssl=False)
    ability = Ability648(client=client)

    # create domain

    # create request
    request = TaobaoTradesSoldGetRequest()
    """
        tid,type,status,payment,orders,rx_audit_status
    """
    request.fields = ['tid', 'type', 'status', 'payment', 'orders','cod_status','end_time']
    request.type = 'tmall_i18n'
    # request.buyer_open_id = 'AAHm5d-EAAeGwJedwSHpg8bT'
    # request.start_created = datetime.now()
    # request.end_created = datetime.now()
    # request.status = 'ALL_WAIT_PAY'
    # request.buyer_nick = 'zhangsan'
    # request.ext_type = 'service'
    # request.rate_status = 'RATE_UNBUYER'
    # request.tag = 'time_card'
    # request.page_no = 1
    # request.page_size = 40
    # request.use_has_next = True
    try:
        response = ability.taobao_trades_sold_get(request, STORE_SESSION)
        return JsonResponse(response)

    except TopException as e:
        return JsonResponse(e)





if __name__ == '__main__':
    # create Client
    client = TopApiClient(appkey='34254070', app_sercet='04b84ea6492167a891f5ebff687153c9',
                          top_gateway_url='https://eco.taobao.com/router/rest', verify_ssl=False)
    ability = Ability648(client=client)

    # create domain

    # create request
    request = TaobaoTradesSoldGetRequest()
    """
        tid,type,status,payment,orders,rx_audit_status
    """
    request.fields = ['tid', 'type', 'status', 'payment', 'orders','cod_status','delivery_cps']
    request.type = 'tmall_i18n'
    # request.buyer_open_id = 'AAHm5d-EAAeGwJedwSHpg8bT'
    # request.start_created = datetime.now()
    # request.end_created = datetime.now()
    # request.status = 'ALL_WAIT_PAY'
    # request.buyer_nick = 'zhangsan'
    # request.ext_type = 'service'
    # request.rate_status = 'RATE_UNBUYER'
    # request.tag = 'time_card'
    # request.page_no = 1
    # request.page_size = 40
    # request.use_has_next = True
    try:
        response = ability.taobao_trades_sold_get(request,
                                                  '6100c2308ad14dff9b9ae7e8878e9a5100635a1b9a3602a2212314430335')
        print(response)
        print(type(response))
    except TopException as e:
        print(e)

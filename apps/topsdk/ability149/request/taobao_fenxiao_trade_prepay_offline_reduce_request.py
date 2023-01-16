from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoFenxiaoTradePrepayOfflineReduceRequest(BaseRequest):

    def __init__(
        self,
        offline_reduce_prepay_param: object = None
    ):
        """
            减少流水
        """
        self._offline_reduce_prepay_param = offline_reduce_prepay_param

    @property
    def offline_reduce_prepay_param(self):
        return self._offline_reduce_prepay_param

    @offline_reduce_prepay_param.setter
    def offline_reduce_prepay_param(self, offline_reduce_prepay_param):
        if isinstance(offline_reduce_prepay_param, object):
            self._offline_reduce_prepay_param = offline_reduce_prepay_param
        else:
            raise TypeError("offline_reduce_prepay_param must be object")


    def get_api_name(self):
        return "taobao.fenxiao.trade.prepay.offline.reduce"

    def to_dict(self):
        request_dict = {}
        if self._offline_reduce_prepay_param is not None:
            request_dict["offline_reduce_prepay_param"] = convert_struct(self._offline_reduce_prepay_param)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict

class TaobaoFenxiaoTradePrepayOfflineReduceTopOfflineReducePrepayDto:
    def __init__(
        self,
        flow_type: int = None,
        offline_prepay_detail_type: int = None,
        ticket_money: int = None,
        receiver_account_num: str = None,
        outer_pay_id: str = None,
        dist_nick: str = None,
        drawer_full_name: str = None,
        pay_bank_num: str = None,
        drawer_account_num: str = None,
        pay_time: datetime = None,
        ticket_issue_date: datetime = None,
        receiver_bank_full_name: str = None,
        ticket_id: str = None,
        accept_date: datetime = None,
        receiver_full_name: str = None,
        pay_bank_full_name: str = None
    ):
        """
            资金流水类型：1.纸质承兑； 2.电子承兑；3.现金；4.优惠返点；5.奖励
        """
        self.flow_type = flow_type
        """
            线下流水类型 1票据作废 2线下使用
        """
        self.offline_prepay_detail_type = offline_prepay_detail_type
        """
            金额，单位分（必须为负数）
        """
        self.ticket_money = ticket_money
        """
            收款人账号
        """
        self.receiver_account_num = receiver_account_num
        """
            外部系统支付流水Id，用于商家上传流水时去重(外部保证唯一）
        """
        self.outer_pay_id = outer_pay_id
        """
            销商淘宝nick
        """
        self.dist_nick = dist_nick
        """
            出票人全称
        """
        self.drawer_full_name = drawer_full_name
        """
            付款行行号
        """
        self.pay_bank_num = pay_bank_num
        """
            出票人账号
        """
        self.drawer_account_num = drawer_account_num
        """
            支付时间
        """
        self.pay_time = pay_time
        """
            出票日期
        """
        self.ticket_issue_date = ticket_issue_date
        """
            收款开户银行
        """
        self.receiver_bank_full_name = receiver_bank_full_name
        """
            承兑票据号
        """
        self.ticket_id = ticket_id
        """
            汇票到期日期
        """
        self.accept_date = accept_date
        """
            收款人全称
        """
        self.receiver_full_name = receiver_full_name
        """
            付款行全称
        """
        self.pay_bank_full_name = pay_bank_full_name


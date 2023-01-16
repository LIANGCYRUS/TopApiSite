from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoJushitaJdpUserAddRequest(BaseRequest):

    def __init__(
        self,
        topics: list = None,
        history_days: int = None,
        host_ip: str = None,
        host_name: str = None,
        rds_name: str = None
    ):
        """
            已废弃，使用页面中应用的配置。用户同步的数据类型,多个用','号分割。可选值：trade,refund,item
        """
        self._topics = topics
        """
            推送历史数据天数，只能为90天内，包含90天。当此参数不填时，表示以页面中应用配置的历史天数为准；如果为0表示这个用户不推送历史数据；其它表示推送的历史天数。
        """
        self._history_days = history_days
        """
            已废弃，新版订单同步服务不要使用。同步用户数据的机器IP,必须是界面配置的IP。
        """
        self._host_ip = host_ip
        """
            已废弃，新版订单同步服务不要使用。绑定类型，用户数据同步的机器名称。
        """
        self._host_name = host_name
        """
            RDS实例名称
        """
        self._rds_name = rds_name

    @property
    def topics(self):
        return self._topics

    @topics.setter
    def topics(self, topics):
        if isinstance(topics, list):
            self._topics = topics
        else:
            raise TypeError("topics must be list")

    @property
    def history_days(self):
        return self._history_days

    @history_days.setter
    def history_days(self, history_days):
        if isinstance(history_days, int):
            self._history_days = history_days
        else:
            raise TypeError("history_days must be int")

    @property
    def host_ip(self):
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        if isinstance(host_ip, str):
            self._host_ip = host_ip
        else:
            raise TypeError("host_ip must be str")

    @property
    def host_name(self):
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        if isinstance(host_name, str):
            self._host_name = host_name
        else:
            raise TypeError("host_name must be str")

    @property
    def rds_name(self):
        return self._rds_name

    @rds_name.setter
    def rds_name(self, rds_name):
        if isinstance(rds_name, str):
            self._rds_name = rds_name
        else:
            raise TypeError("rds_name must be str")


    def get_api_name(self):
        return "taobao.jushita.jdp.user.add"

    def to_dict(self):
        request_dict = {}
        if self._topics is not None:
            request_dict["topics"] = convert_basic_list(self._topics)

        if self._history_days is not None:
            request_dict["history_days"] = convert_basic(self._history_days)

        if self._host_ip is not None:
            request_dict["host_ip"] = convert_basic(self._host_ip)

        if self._host_name is not None:
            request_dict["host_name"] = convert_basic(self._host_name)

        if self._rds_name is not None:
            request_dict["rds_name"] = convert_basic(self._rds_name)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


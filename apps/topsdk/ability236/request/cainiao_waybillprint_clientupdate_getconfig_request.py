from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class CainiaoWaybillprintClientupdateGetconfigRequest(BaseRequest):

    def __init__(
        self,
        mac: str = None,
        lan_ip: str = None,
        version: str = None,
        msgid: int = None
    ):
        """
            服务发起机器的物理地址
        """
        self._mac = mac
        """
            服务发起机器局域网ip
        """
        self._lan_ip = lan_ip
        """
            当前打印客户端版本
        """
        self._version = version
        """
            当前消息版本
        """
        self._msgid = msgid

    @property
    def mac(self):
        return self._mac

    @mac.setter
    def mac(self, mac):
        if isinstance(mac, str):
            self._mac = mac
        else:
            raise TypeError("mac must be str")

    @property
    def lan_ip(self):
        return self._lan_ip

    @lan_ip.setter
    def lan_ip(self, lan_ip):
        if isinstance(lan_ip, str):
            self._lan_ip = lan_ip
        else:
            raise TypeError("lan_ip must be str")

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        if isinstance(version, str):
            self._version = version
        else:
            raise TypeError("version must be str")

    @property
    def msgid(self):
        return self._msgid

    @msgid.setter
    def msgid(self, msgid):
        if isinstance(msgid, int):
            self._msgid = msgid
        else:
            raise TypeError("msgid must be int")


    def get_api_name(self):
        return "cainiao.waybillprint.clientupdate.getconfig"

    def to_dict(self):
        request_dict = {}
        if self._mac is not None:
            request_dict["mac"] = convert_basic(self._mac)

        if self._lan_ip is not None:
            request_dict["lan_ip"] = convert_basic(self._lan_ip)

        if self._version is not None:
            request_dict["version"] = convert_basic(self._version)

        if self._msgid is not None:
            request_dict["msgid"] = convert_basic(self._msgid)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


from typing import List
from topsdk.client import BaseRequest
from topsdk.util import convert_struct_list,convert_basic_list,convert_struct,convert_basic
from datetime import datetime


class TaobaoTradeMemoUpdateRequest(BaseRequest):

    def __init__(
        self,
        tid: int = None,
        memo: str = None,
        flag: int = None,
        reset: bool = None
    ):
        """
            交易编号
        """
        self._tid = tid
        """
            卖家交易备注。最大长度: 1000个字节
        """
        self._memo = memo
        """
            卖家交易备注旗帜，可选值为：0(灰色), 1(红色), 2(黄色), 3(绿色), 4(蓝色), 5(粉红色)，默认值为0
        """
        self._flag = flag
        """
            是否对memo的值置空若为true，则不管传入的memo字段的值是否为空，都将会对已有的memo值清空，慎用；若用false，则会根据memo是否为空来修改memo的值：若memo为空则忽略对已有memo字段的修改，若memo非空，则使用新传入的memo覆盖已有的memo的值
        """
        self._reset = reset

    @property
    def tid(self):
        return self._tid

    @tid.setter
    def tid(self, tid):
        if isinstance(tid, int):
            self._tid = tid
        else:
            raise TypeError("tid must be int")

    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, memo):
        if isinstance(memo, str):
            self._memo = memo
        else:
            raise TypeError("memo must be str")

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, flag):
        if isinstance(flag, int):
            self._flag = flag
        else:
            raise TypeError("flag must be int")

    @property
    def reset(self):
        return self._reset

    @reset.setter
    def reset(self, reset):
        if isinstance(reset, bool):
            self._reset = reset
        else:
            raise TypeError("reset must be bool")


    def get_api_name(self):
        return "taobao.trade.memo.update"

    def to_dict(self):
        request_dict = {}
        if self._tid is not None:
            request_dict["tid"] = convert_basic(self._tid)

        if self._memo is not None:
            request_dict["memo"] = convert_basic(self._memo)

        if self._flag is not None:
            request_dict["flag"] = convert_basic(self._flag)

        if self._reset is not None:
            request_dict["reset"] = convert_basic(self._reset)

        return request_dict

    def get_file_param_dict(self):
        file_param_dict = {}
        return file_param_dict


# -----------------------------------------------------------
# Filename: 联合注解
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------
from typing import Union

# 使用Union类型，必须先导入包

my_list: list[Union[int, str]] = [1, 2, "luk4s", "lukasy"]


def func(data: Union[int, str]) -> Union[int, str]:
    pass

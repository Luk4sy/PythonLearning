# -----------------------------------------------------------
# Filename: 类型注解
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------
import json

# 基础数据类型和容器的注解
var_1: int = 10
var_2: str = "apple"
var_3: bool = True

my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, bool] = (1, "huawei", True)
my_dict: dict[str, int] = {"huawei": 123}

var_1 = json.load('{"name":"zhanghsan"')  # type: dict[str,str]

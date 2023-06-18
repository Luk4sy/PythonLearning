# -----------------------------------------------------------
# Filename: None类型
# Author: Luk4sy
# Date: 2023/6/18
#
# Description: 
# -----------------------------------------------------------

# 无return语句的函数返回值
def say_hi():
    print("Hello!")
result = say_hi()
print(f"无返回值函数，返回内容是：{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")

# 主动返回None的函数
def say_hi2():
    print("Hello2!")
    return None
result = say_hi2()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是{type(result)}")

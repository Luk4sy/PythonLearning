# -----------------------------------------------------------
# Filename: lambda表达式
# Author: Luk4sy
# Date: 2023/7/10
#
# Description: 
# -----------------------------------------------------------

# 定义一个函数，接受其它函数输入
def test_func(compute):
    result = compute(1, 2)
    print(f"结果是：{result}")


# 通过lambda匿名函数的形式，将匿名函数作为参数传入
# 定义语法
# lambda 传入参数 : 函数体（一行代码）
test_func(lambda x, y: x + y)

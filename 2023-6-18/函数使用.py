# -----------------------------------------------------------
# Filename: 函数使用
# Author: Luk4sy
# Date: 2023/6/18
#
# Description: 
# -----------------------------------------------------------

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")

my_len("lukasy")
my_len("Manchester")

# 语法
# def function( param ):
#     function body
#     return value

# -----------------------------------------------------------
# Filename: 列表的遍历
# Author: Luk4sy
# Date: 2023/6/19
#
# Description: 
# -----------------------------------------------------------


# while
def list_while_func():
    my_list = [1, 2, 3, 4, 5, 6]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表元素：{element}")
        index += 1


# for
def list_for_func():
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表元素：{element}")


list_while_func()
list_for_func()

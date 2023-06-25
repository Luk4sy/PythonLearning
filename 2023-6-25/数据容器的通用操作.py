# -----------------------------------------------------------
# Filename: 数据容器的通用操作
# Author: Luk4sy
# Date: 2023/6/25
#
# Description: 
# -----------------------------------------------------------

# 五种数据容器
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3}
# len元素个数
print(f"my_list元素个数：{len(my_list)}")
print(f"my_tuple元素个数：{len(my_tuple)}")
print(f"my_str：{len(my_str)}")
print(f"my_set元素个数：{len(my_set)}")
print(f"my_dict元素个数：{len(my_dict)}")

# max最大元素
print(f"my_list最大值：{max(my_list)}")
print(f"my_tuple最大值：{max(my_tuple)}")
print(f"my_str最大值：{max(my_str)}")
print(f"my_set最大值：{max(my_set)}")
print(f"my_dict最大值：{max(my_dict)}")

# min最小元素
print(f"my_list最小值：{min(my_list)}")
print(f"my_tuple最小值：{min(my_tuple)}")
print(f"my_str最小值：{min(my_str)}")
print(f"my_set最小值：{min(my_set)}")
print(f"my_dict最小值：{min(my_dict)}")

# sorted 排序功能
my_list = [3, 10, 9, 23, 19, 23]
# 升序排序
print(f"列表对象升序的排序结果为：{sorted(my_list)}")
# 降序排序
print(f"列表对象降序的排序结果为：{sorted(my_list, reverse=True)}")

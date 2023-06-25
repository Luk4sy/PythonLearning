# -----------------------------------------------------------
# Filename: 集合
# Author: Luk4sy
# Date: 2023/6/25
#
# Description: 
# -----------------------------------------------------------

# 定义集合
my_set = {"WunderMinibar", "Whiskey", "Gin", "Brandy"}
my_set_empty = set()  # 定义空集合
print(f"my_set内容是：{my_set},类型是{type(my_set)}")
print(f"my_set_empty内容是：{my_set_empty},类型是{type(my_set_empty)}")

# 添加新元素
my_set.add("Gin Tonic")
my_set.add("Vodka")

# 移除元素
my_set.remove("Gin")
print(my_set)

# 随机取出一个元素
element = my_set.pop()
print(f"集合被取出的元素是：{element},取出元素后的my_set:{my_set}")

# 清空集合
my_set.clear()
print(f"集合已被清空，my_set:{my_set}")

# -----------------------------------------------------------
# Filename: 列表常用操作
# Author: Luk4sy
# Date: 2023/6/19
#
# Description: 
# -----------------------------------------------------------

my_list = ["Lukasy", "Tom", "Jack"]
# 1 查找某元素在列表内的下标索引
index = my_list.index("Tom")
print(index)

# 2 修改待定下标索引的值
my_list[0] = "Luk4sy"
print(f"列表被修改元素值后，结果是：{my_list}")

# 3 在指定下表位置插入新元素
my_list.insert(1, "good")
print(f"列表插入元素后，结果是：{my_list}")

# 4 在列表的尾部追加单个新元素
my_list.append("你好")
print(f"列表在追加了一个新元素的列表后，结果是：{my_list}")

# 5 在列表的尾部追加一组元素
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
print(f"列表在追加了一组元素的列表后，结果是：{my_list}")

# 6 删除指定下标索引的元素
my_list3 = [1, 2, 3, 4, 5, 6]

# 6.1 del 列表[下标]
del my_list3[2]
print(f"列表删除元素后的结果是 ：{my_list3}")

# 6.2 列表.pop[下标]
my_list3 = [1, 2, 3, 4, 5, 6]
element = my_list3.pop(2)
print(f"通过pop方法取出元素后，列表的结果是：{my_list3}，取出的元素是{element}")

# 7 删除某元素在列表中的第一个匹配项
my_list3 = [1, 2, 3, 3, 4, 5]
my_list3.remove(3)
print(f"通过remove方法移除元素后，列表的结果是：{my_list3}")

# 8 清空列表
my_list3.clear()
print(f"列表被清空了，结果是：{my_list3}")

# 9 统计列表内某元素的数量
my_list3 = [1, 2, 3, 3, 4, 5]
count = my_list3.count(3)
print(f"列表中3的数量是：{count}")

# 10 统计列表中全部的元素数量
count2 = len(my_list3)
print(f"列表元素的总数量为：{count2}")

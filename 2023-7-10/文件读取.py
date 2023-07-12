# -----------------------------------------------------------
# Filename: 文件读取
# Author: Luk4sy
# Date: 2023/7/10
#
# Description: 
# -----------------------------------------------------------
import time

# 打开文件
f = open("C:/Users/30259/Desktop/一个文本.txt", encoding="UTF-8")
print(type(f))
# 读取文件
# print(f"读取10个字节的结果:{f.read(10)}")
# print(f"read方法读取全部内容的结果是:{f.read()}")  # 多次调用read会在上一次调用read的内容后面继续读取

# 读取文件 - readlines()
# lines = f.readlines()  # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是:{lines}")

# 读取文件 - readline()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行的数据是{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")

# for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")

# 文件的关闭
f.close()
time.sleep(500000)

# with open 语法操作文件
with open("C:/Users/30259/Desktop/一个文本.txt", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")
time.sleep(500000)

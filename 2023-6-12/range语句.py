# -----------------------------------------------------------
# Filename: range语句
# Author: Luk4sy
# Date: 2023/6/12
#
# Description: 
# -----------------------------------------------------------

# range(start, stop, step)
"""
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
"""

r1 = range(10)  # 从 0 开始到 9
print(r1)
r2 = range(1, 11)  # 从 1 开始到 10
print(r2)
r3 = range(0, 30, 5)  # 步长为 5
print(r3)
r4 = range(0, 10, 3)  # 步长为 3
print(r4)
r5 = range(0, -10, -1)  # 负数
print(r5)
r6 = range(0)
print(r6)
r7 = range(1, 0)
print(r7)

# for循环中使用
x = "Luk4sy"
for i in range(len(x)):
    print(x[i])

# -----------------------------------------------------------
# Filename: 文件写入
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------

# 打开文件
f = open("C:/Users/30259/Desktop/另一个文本.txt", "w", encoding="UTF-8")  # w模式，如果再写入的话，会把之前的内容都清空，然后再写入新的内容 a模式是文件的追加写入操作
# write写入
f.write("Hello world!")
# flush刷新
f.flush()  # 将内存中积攒的内容，写入到硬盘的文件中
f.close()  # close方法，内置了flush的功能


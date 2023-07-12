# -----------------------------------------------------------
# Filename: 异常捕获
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------

# 基本捕获语法
# try:
#     f = open("C:/Users/30259/Desktop/文本.txt", "r", encoding="UTF-8")
# except:
#     print("出现异常了，因为文件不存在，我将用open的模式，改为w模式去打开")
#     f = open("C:/Users/30259/Desktop/文本.txt", "w", encoding="UTF-8")

# 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print("出现了变量为定义的异常")
#     print(e)

# 捕获多个异常
# try:
#     # 1 / 0
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("出现了变量未定义或者除以0的异常错误")

# 捕获所有异常
try:
    f = open("C:/Users/30259/Desktop/文本.txt", "r", encoding="UTF-8")
except Exception as e:
    print("出现异常了")
    f = open("C:/Users/30259/Desktop/文本.txt", "w", encoding="UTF-8")
else:
    print("没出现异常")
finally:
    print("是否有没有异常都要执行")
    f.close()

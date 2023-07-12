# -----------------------------------------------------------
# Filename: 类和对象
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------

# 设置一个闹钟类
class Clock:
    id = None  # 序列号
    price = None  # 价格

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


# 构造两个闹钟对象并让其工作而
clock1 = Clock()
clock1.id = "003032"
clock1.price = 19.99
print(f"闹钟ID：{clock1.id},价格：clock1.price")
clock1.ring()

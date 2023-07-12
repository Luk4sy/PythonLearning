# -----------------------------------------------------------
# Filename: 继承
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------

class Phone:
    IMEI = None  # 序列号
    producer = "HUAWEI"  # 厂商

    def call_by_5G(self):
        print("Use 5G")


# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "HONOR"

    def call_by_5G(self):
        print("开启CPU单核")
        Phone.call_by_5G(self)  # 调用父类方法1
        super().call_by_5G()  # 调用父类方法2

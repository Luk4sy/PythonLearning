# -----------------------------------------------------------
# Filename: 封装
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------
class Phone:
    __current_voltage = None  # 两个下划线表示私有成员

    def __keep_single_core(self): # 私有方法=
        print("让CPU以单核模式运行")


phone = Phone()

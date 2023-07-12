# -----------------------------------------------------------
# Filename: 多态
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------

# 一个例子
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


# 抽象类
class AC:
    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
make_cool(midea_ac)

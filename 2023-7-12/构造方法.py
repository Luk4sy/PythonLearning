# -----------------------------------------------------------
# Filename: 构造方法
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------

class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")


stu = Student("pjx", 20, 121313131)
print(stu.name)
print(stu.age)
print(stu.tel)

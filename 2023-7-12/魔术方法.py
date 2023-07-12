# -----------------------------------------------------------
# Filename: 魔术方法
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # __str__
    def __str__(self):
        return f"Student类对象，name:{self.name},age:{self.age}"

    # __lt__
    def __lt__(self, other):
        return self.age < other.age  # 返回布尔值

    # __le__
    def __le__(self, other):
        return self.age <= other.age  # 返回布尔值

    # __eq__
    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("周杰伦", 31)
stu2 = Student("周杰伦", 32)

print(stu1)
print(str(stu1))

print(stu1 == stu2)  # 不用eq默认比较内存地址

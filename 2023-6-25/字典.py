# -----------------------------------------------------------
# Filename: 字典
# Author: Luk4sy
# Date: 2023/6/25
#
# Description: 
# -----------------------------------------------------------


# 字典定义
# Key-Value 键值对的形式
my_dict1 = {"Luk4sy": 18, "Lukasy": 17}
print(my_dict1)

# 从字典中基于key获取value
page = my_dict1["Lukasy"]
print(f"Lukasy所在的页数：{page}")

# 字典嵌套字典
stu_score_dict = {
    "Luk4sy": {
        "Reading": 7.5,
        "Listening": 7.5,
        "Writing": 7,
        "Speaking": 7
    },
    "Lukasy": {
        "Reading": 7,
        "Listening": 7,
        "Writing": 6.5,
        "Speaking": 6.5
    }
}

print(stu_score_dict)

# 通过key获取嵌套字典的value
score_reading = stu_score_dict["Luk4sy"]["Reading"]
print(score_reading)

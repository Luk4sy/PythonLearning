# -----------------------------------------------------------
# Filename: python数据和json数据的相互转化
# Author: Luk4sy
# Date: 2023/7/12
#
# Description: 
# -----------------------------------------------------------
import json

# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name": "吴彦祖", "age": 18}, {"name": "彭于晏", "age": 18}]
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

# 这个字典，将字典转换成JSON
d = {"name": "吴彦祖", "age": 18}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将JSON字符串转换未Python的数据类型{k: v, k:v}
s = '{"name":"周杰伦","addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)

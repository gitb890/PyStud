import copy

# 导入copy模块完成浅拷贝
nums = [1,2,3,4,5]
nums_copy = copy.copy(nums)
nums[2] = 30
print(nums)
print(nums_copy)

# 浅拷贝下对象id是一致的情况
item = [10,['ji','jia'],2,3]
item_copy=copy.copy(item)
item[0] = 100
item[1].append('xxx')
print(item)
print(item_copy)
print(id(item[1]))
print(id(item_copy[1]))
# 深拷贝会遍历并拷贝items里的所有内容
item_deep = copy.deepcopy(item)
print(id(item[1]))
print(id(item_deep[1]))

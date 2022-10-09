from collections import OrderedDict

d1 = {'name':'pipe','age':18}
d2 = {'age':18,'name':'pipe'}
print(d1==d2)
# 为True是因为内容一致而顺序不同的字典被视作相等，因为解释器只对比字典的键和值是否一致

d3 = OrderedDict(name='pipe',age=18)
d4 = OrderedDict(age=18,name='pipe')
print(d3==d4)
# 为False是因为同样的OrderedDict则被视作不相等，因为“键的顺序”也会作为对比条件
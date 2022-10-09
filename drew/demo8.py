from collections import namedtuple


def get_rectangle():
    """返回长和宽"""
    width = 100
    height = 20
    return width,height

# 这里是对函数的解包操作
result = get_rectangle()
print(result,type(result))

# 输出(100, 20) <class 'tuple'>

# 调用生成器调用tuple生成一个tuple函数，获得元组
result1 = tuple((n*100 for n in range(10) if n%2==0))
print(result1)

# 创建具名元组
Rectangle = namedtuple('jiosdfg','width,heigh')
print(Rectangle)

# 初始化具名元组
rect = Rectangle(100,192)
# 指定字段名称来初始化
rect = Rectangle(width=100,heigh=192)
# 可以像普通元组一样通过数字下标索引来访问成员
print(rect[0])
# 具名元组支持通过名称来访问成员
print(rect.width)
# 和普通元组一样是不可变的
rect.width +=1
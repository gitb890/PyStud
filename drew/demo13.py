import sys

list = [1,2,3,4]
# 创建迭代器对象
it = iter(list)
# 输出迭代器的下一个元素
# print(next(it))
# print(next(it))
# print(next(it))
# for循环遍历
# for x in it:
#     print(x,end=" ")
# 使用next()函数
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，
# 在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
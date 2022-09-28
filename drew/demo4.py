from decimal import Decimal

sf = 1_000_900
print(sf)

# 精度计算,需要使用字符串的形式
print(Decimal('0.1') + Decimal('0.2'))

numbers = [23, 453, 23, 53, 53, 23, 53, 23, 43, 51, 24, 215, 64, 23, 65, 34, 10]
# 判断列表中的偶数满足取余=0时输出,下面两种方法结果相同，第二种利用布尔值可以作为整型使用的特性
cont = 0
for i in numbers:
    if i % 2 == 0:
        cont += 1
print(cont)

count = sum(i % 2 == 0 for i in numbers)
print(count)

# 字符串类型,可以对其进行遍历、切片、反转等操作，就像访问一个列表对象
s = 'hello world!'
for c in s[1:3]:
    print(c)

print(s[::-1])
print(''.join(reversed(s)))

# 字符串格式化
username, score = 'hiosd', 1930
# C语言风格----------
print('heeik%s,your score is %d' % (username, score))
# str.format---------
print('heeik{},your score is {:d}'.format(username, score))
# f-string风格----------
print(f'heeik{username},your score is {score:d}')
# 二次加工,将username前增加20个空格
print(' {:>20}'.format(username))
print(f' {username:>20}')

# 拼接字符串的方式
words = ['Numbers(1-10):']
for i in range(10):
    words.append(f'Value: {i + 1}')
print('\n'.join(words))


def extract_value(s):
    items = s.split(':')
    # 因为s不一定包含：所以需要对结果长度进行判断
    if len(items) == 2:
        return items[1]
    else:
        return ''


print(extract_value('huvos:sfjisfv'))
print(extract_value('nisfvs'))


def extract_value_V2(s):
    # 当s包含分隔符:时，元组最后一个成员刚好是value
    # 若是没有分隔符，最后一个成员默认是空字符串’‘
    return s.partition(':')[-1]


print(extract_value_V2('jiosvs:sfuhig'))

# 字符串替换
wo = 'hui周昂问囧从机场,hui回收v.'
table = wo.maketrans(',.','，。')
print(wo.translate(table))
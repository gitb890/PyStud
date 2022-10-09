import dis

"""dis模块反编译字节码"""

def add(x,y):
    return  x+y

print(dis.dis(add))


word = ['hui','hujiaff','jifa','juiaf']*30

def str_cat():
    """字符串拼接"""
    s=''
    for words in word:
        s += words
    return s
print(str_cat())

def str_join():
    """使用列表配合join产生字符串"""
    l = []
    for words in word:
        l.append(words)
    return ''.join(l)
print(str_join())

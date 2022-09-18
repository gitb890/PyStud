
wendu = input('输入带符号当前的温度：')
# 温度转换公式
# F = C*1.8+32
# C = (F-32)/1.8

if wendu[-1] in ['F','f']:
    C = (eval(wendu[0:-1])-32)/1.8
    # [0:-1]切片，获取字符串中最后一个字符
    print("转换后的温度是{:.2f}C".format(C))
elif wendu[-1] in ['C','c']:
    F = (eval(wendu[0:-1])) * 1.8 + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入错误，请检查格式")



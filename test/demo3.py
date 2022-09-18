import os

from numpy import average

test = {'hello':12,12:90,43:89}

for i in test:
    print("test['hello']:",test['hello'])
# print(test)

a = 19
b = 20

while b<1000:
    # print("it`s true")
    print(b,end=' ')
    a,b=b,a+b


ios = os.getcwd()
# print(ios)

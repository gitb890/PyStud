data = ['huf','jiosd','jisof','shdj',12]

*friut,_= data
# username,*friut,score=data
# 等价于 username,friut,score = data[0],data[1:-1],data[-1]


# print(username)
print(*friut)
print(_)
# print(*score)

for username,score in [('hui',100),('huisd',50)]:
    print(username)
    print(score)

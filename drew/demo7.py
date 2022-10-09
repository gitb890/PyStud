def remove_odd_mul_100(numbers):
    """剔除奇数并乘以100"""
    results = []
    for number in numbers:
        if number % 2 == 1:
            continue
        results.append(number * 100)
    return(results)

numbers = []
results = [n*100 for n in numbers if n%2 ==0]


#用一个表达式完成4件事情
#
# 1. 遍历旧列表：for n in numbers
# 2. 对成员进行条件过滤：if n % 2 == 0
# 3. 修改成员： n * 100
# 4. 组装新的结果列表
#
results = [n * 100 for n in numbers if n % 2 == 0]

print("\a")

x = 1
print(f'{x+1=}')

a = ['gyu','gyu',67]
n = [7,7,'ghu']
x = [a,n]
print(x)

print('{jiogr}\n'*40)
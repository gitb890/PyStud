movie = {'name': 'Burning', 'type': 'movie', 'year': 2018}

# 通过 key 来获取某个 value
movie['year']

# 字典是一种可变类型，所以可以给它增加新的key
movie['rating'] = 10
# 2018
# 字典的key 不可重复，对同一个 key 赋值会覆盖旧值
movie['rating'] = 9
movie
# {'name': 'Burning', 'type': 'movie', 'year': 2018, 'rating': 9}

for key in movie:
    print(movie[key])

for key,value in movie.items():
    print(key,value)

try:
    dict['items'].append(value)
except KeyError:
    dict['items']=[value]


cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
print(cars.sort())

# 使用函数对汽车列表调用这个函数
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

print(sorted(cars,reverse=True))

# 反着打印列表
print(cars)
cars.reverse()
print(cars)

# 确定列表的长度
len(cars)
print(len(cars))


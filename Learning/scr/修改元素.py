motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0,'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)
del motorcycles[2]
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

aaa = motorcycles.pop()
print(motorcycles)
print(aaa)

last_owned = motorcycles.pop()
print("The last motorcyle I owned was a " + last_owned.title() + ".")


first_owned = motorcycles.pop(0)
print("The first motorcyle I owned was a " + first_owned.title() + ".")

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)



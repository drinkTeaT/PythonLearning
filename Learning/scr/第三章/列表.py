bicycles = ['trek','cannondale','resdline','specialized']
print(bicycles)
print(bicycles[0])
# 让读取的元素更整洁，可以使用第二章的内容
print(bicycles[0].title())
print(bicycles[1].upper())
print(bicycles[3].lower())
print(bicycles[-1])

message = " My first bicycle was a " + bicycles[0].title() + "."
print(message)

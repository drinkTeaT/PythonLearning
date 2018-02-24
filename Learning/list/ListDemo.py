#coding:gbk
'''
函数部分
'''

'''创建函数'''
def test ():
    print("hello world")
    
'''创建函数'''
''' 有return该函数返回一个值'''
def test1(value):
    '''定义一个变量 sum用来对列表数据求和'''
    sum = 1
    '''对列表数据进行遍历（把里面的值一个个拿出来）'''
    for i in value:
        sum = sum * i
    return sum

value = [1,2,3,2,2,3,1]
print(test1(value))



'''变量    重复赋值'''
abc = 45
abc = 54
fgh = [1,4,"t8iy"]

''' 常量  不能赋值'''
12
"asdfasf"
4.42
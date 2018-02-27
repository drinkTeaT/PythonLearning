'''

基础知识  变量，常量，数据类型，函数返回值
变量是可以被重复赋值的，而且是名字是自定义的
常量不准被赋值
数据类型 常见的有 整数  int,小数 float ，列表 list ，字符串 str，字典 dict，集合 set等等  检测数据类型 用 type(参数)
'''
a = 45
a = 8979.36
b = "var"

c = []

d = {}
d = dict()

e = set()

type(e)

''' 函数返回值'''
#定义一个  无参，没有返回值的函数
def cetaphil():
    for i in c:
        print(i)
        
#调用 函数
cetaphil()

#定义一个 有参，有返回值的函数 
#传递两个数据到该函数，并返回一个包含这两个数据的列表数据类型
def pen(b,aa=1):
    c = [1,2,3]    
    c.append(b)
    c.append(aa)
    return c
#调用函数
pen(1,2)

''' 给定一个列表，里面包含小数，整数。得出他的平均数 用有返回值函数实现'''
data = [1,6,1.34,2,3,4,5.14]
def avg(a):
    d = 0
    for i in a:
        d = d + i
    f = d/len(data)
    return f

print(avg(data))   # a = data

''' 给定一个列表，里面包含小数，整数。在函数内部打印出他的平均数 用无返回值函数实现'''

def soft(a):
    b = 0
    for i in a:
        b = b + i
    h = b/len(a)
    print(h)

data = [1,6,1.34,2,3,4,5.14]
soft(data)

















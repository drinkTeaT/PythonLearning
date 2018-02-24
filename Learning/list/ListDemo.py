#coding:gbk
'''
函数部分  计算两个列表数据之和
'''

'''创建函数'''
def test ():
    print("hello world")
    
list1 = [12,23,8,9]
list2 = [6,2,3]

def test1(a,b):
    sum1 = 0
    for i in a:
        sum1 = sum1 + i
    
    sum2 = 0
    for i in b:
        sum2 = sum2 + i
    
    return sum1+sum2

n = test1(list1, list2)
print(n)

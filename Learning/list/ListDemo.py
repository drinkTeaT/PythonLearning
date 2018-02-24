#coding:gbk
'''
函数部分 缺省赋值 以及缺省函数的作用
'''


'''
def 函数名（参数）:
         代码组 
创建缺省函数'''
def abc(a,b = 3):
    return a+b

n = abc(6,2)
print(n)

n = abc(1,2)
print(n)
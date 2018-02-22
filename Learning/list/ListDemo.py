#coding:gbk
'''
for循环  ;if else;只打印 person 列表中的数字
'''

person = ["male","female","kid",23,1.4,"female","tom","jack",34,998,"汉字",943242423.23232323232]
number  = 12
'''i是一个变量，用来取列表中的值'''
for i in person:
    print(i)

'''等于号是  == '''
if isinstance(number, list) == True:
    print("是真的！")
else:
    print("是假的！")

print("整数 的数据类型",type(person[3])," 小数的数据类型 ",type(person[4]),"字符串数据类型",type(person[0]))

'''打印 person 列表中的数字'''
for i in person:
    if isinstance(i, int) == True or isinstance(i, float) == True : 
        '''如果i是小数 或 整数就显示该值 '''
        print(i)
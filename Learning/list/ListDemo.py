#coding:gbk
'''
列表推导  按条件循环一个列表中所有值  ;如何在列表推导内过滤列表中字符串？
'''

data1 = [1,90,33,74,3.14,99,5.432,102.3]

'''把data1数字中大于50的放入data2列表内'''
data2 = [i for i in data1  if i > 50 ]
print(data2)

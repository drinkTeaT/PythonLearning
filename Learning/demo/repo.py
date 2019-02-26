''' 实现在两个列表中拿出相同位置的值'''
from Learning.scr import method
fruit = dict()
fruit["Apple"] = 5
fruit["Watermelon"] = 2
fruit["Orange"] = 4
fruit["Pear"] = 4

freshfruit = [8,2,12,6,23,123,4,2,43,54,65,7,3,4]
weight = [10,30,15,12,23,123,4,2,43,54,65,7,3,4]

''' 计算今天的毛收入'''
for i in range(freshfruit.__len__()):
    print(i)
    
print(method.newIncome(freshfruit, weight))
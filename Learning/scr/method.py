'''
写函数专用
计算   水果毛收入 传递一个字典和列表作为参数，返回一个毛收入
'''
def income(a,b):
    ''' 苹果价格*斤数 + 西瓜价格*斤数  + 橙子价格*斤数 + 梨子价格*斤数  '''
    price = a["Apple"]*b[0] + a["Watermelon"]*b[1] + a["Orange"]*b[2] + a["Pear"]*b[3]
    return price

'''

计算   水果毛收入 传递列表列表作为参数，返回一个毛收入
'''
def newIncome(a,b):
    f = 0
    for i in range(len(a)) :
        f = f + a[i]*b[i]
    return f
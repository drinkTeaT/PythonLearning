#coding:gbk
'''
��������
'''

'''��������'''
def test ():
    print("hello world")
    
'''��������'''
''' ��return�ú�������һ��ֵ'''
def test1(value):
    '''����һ������ sum�������б��������'''
    sum = 1
    '''���б����ݽ��б������������ֵһ�����ó�����'''
    for i in value:
        sum = sum * i
    return sum

value = [1,2,3,2,2,3,1]
print(test1(value))



'''����    �ظ���ֵ'''
abc = 45
abc = 54
fgh = [1,4,"t8iy"]

''' ����  ���ܸ�ֵ'''
12
"asdfasf"
4.42
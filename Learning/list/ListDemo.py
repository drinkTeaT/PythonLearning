#coding:gbk
'''
forѭ��  ;if else;ֻ��ӡ person �б��е�����
'''

person = ["male","female","kid",23,1.4,"female","tom","jack",34,998,"����",943242423.23232323232]
number  = 12
'''i��һ������������ȡ�б��е�ֵ'''
for i in person:
    print(i)

'''���ں���  == '''
if isinstance(number, list) == True:
    print("����ģ�")
else:
    print("�Ǽٵģ�")

print("���� ����������",type(person[3])," С������������ ",type(person[4]),"�ַ�����������",type(person[0]))

'''��ӡ person �б��е�����'''
for i in person:
    if isinstance(i, int) == True or isinstance(i, float) == True : 
        '''���i��С�� �� ��������ʾ��ֵ '''
        print(i)
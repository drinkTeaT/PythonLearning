#coding:gbk
'''
���⼯�������һ�����б�������femaleǰ�涼���롰������ҫ������β���ڶ�femaleǰ�棿
'''

person = ["male","female","kid",23,1.4,"female"]

position = person.index("female" )
person.insert(position, "������ҫ")
print(person)
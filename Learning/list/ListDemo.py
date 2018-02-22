#coding:gbk
'''
问题集锦：如何一个在列表中所有female前面都插入“王者荣耀”？如何插入第二female前面？
'''

person = ["male","female","kid",23,1.4,"female"]

position = person.index("female" )
person.insert(position, "王者荣耀")
print(person)
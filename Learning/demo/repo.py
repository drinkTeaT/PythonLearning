'''

文件的读和写    for循环里面的readline只打印某一行？

'''
import os
'''打开文件所在目录'''
os.chdir("D:\\")
''' 找到具体 “文件名.后缀 ”'''
data = open("ss.txt","a")

''' 删除原有数据写入新数据'''
print("/\nss",file = data)
''' 增加新数据'''
data.write("胜多负少单方事故")
'''关闭文件'''
data.close()
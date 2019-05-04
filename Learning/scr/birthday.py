# 正确的做法是将 age使用str（）函数变成一个字符串
age = 23
message = "happy"+ str(age) +  "rd Birthday"
print(message)

# 错误的例子
age = 23
message = "happy"+ age + "rd Birthday!"
print(message)
# 这里的age 是一个数值int，不是字符串，因此无法运行

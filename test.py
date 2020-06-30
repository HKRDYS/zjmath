import math


# 这里自定义不可变的常量
class Finally:
    f = 10**-6
    pi = 3.14159


pi = 10
# 调用自己定义的常量
a = Finally.pi*3
# 输出结果发现并没受到新定义的干扰
# print("{:.6f}".format(a))
# 当然这样会比直接定义的慢，但是可以防止误操作，主要是
# 这种做法也可以用于CPP,JAVA有相关防护就不需要惹

b = 10
c = b
b = b+5
print(c)
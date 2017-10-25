# 从内置模块sys导入argv这个列表（参数变量）
from sys import argv
# argv包含传递给脚本的所有参数，第一个参数为脚本本身，即script
script, filename = argv
# 打开filename这个参数
txt = open(filename)
# 打印这句话并使用format实现
print("Here's your file {}".format(filename))
# 打印出txt的read方法
print(txt.read())
# 关闭文件
txt.close()

print("Type the filename again:")
# 获取输入
file_again = input("> ")
# 打开这个输入并赋值给变量
txt_again = open(file_again)
# 使用read方法并打印出来
print(txt_again.read())
# 关闭文件
txt_again.close()
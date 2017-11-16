# 导入gl.py文件
import gl
# 打印全局变量_a
print(gl._a)



# 列表
things = ['a', 'b', 'c', 'd']
print(things)
things[0] = 'x'
print(things)

# 字典
stuff = {'name': 'zed', 'age': 30, 'height': 175}
print(stuff['name'])
stuff['name'] = 'Alan'
print(stuff)
del stuff['name']
print(stuff)

# 一个练习

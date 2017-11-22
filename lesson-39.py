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
# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
print(states['Oregon'])

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
print(cities['CA'])

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
print(cities)

# print out some cities
print('-' * 10)
print('NY state has: ', cities['NY'])
print('OR state has:', cities['OR'])

# print some states
print('-' * 10)
print('Michigan\'s abbreviation is: ', states['Michigan'])
print('Florida\'s abbreviation is: ', states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print('{} is abbreviated {}'.format(state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print('{} has the city {}'.format(abbrev, city))

# now do both at the same time
print('-' * 10)
# dict.item()是返回可遍历的(键，值)元祖数组
for state, abbrev in states.items():
    print('{} state is abbreviated {} and has city {}'.format(state, abbrev, cities[abbrev]))

print('-' * 10)

# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print('Sorry, no Texas.')

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print('The city for the state \'TX\' is: {}'.format(city))

information = {'name': 'zibba', 'sex': 'Male'}
for i, j in information.items():
  print(i, ':', j)


# dictionaries
a_dict = {'server': 'db.diveinpython3.org', 'database': 'mysql'}
print(a_dict)
print(a_dict['server'])
print(a_dict['database'])

# modifying
a_dict['database'] = 'blog'
print(a_dict['database'])

# add new key-value
a_dict['user'] = 'mark'
print(a_dict)

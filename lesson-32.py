hairs = ['brown', 'black', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print('This is count {}'.format(number))

# same as above
for fruit in fruits:
    print('A fruit of type: {}'.format(fruit))

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print('I got {}'.format(i))

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in elements:
    print('Adding {} to the list.'.format(i))
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print('Element was: {}'.format(i))
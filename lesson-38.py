ten_things = 'Apples Oranges Crows Telephone Light Sugar'
print('Wait there\'s not 10 things in that list, let\'s fix that.')
stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']
while len(stuff) != 10:
    next_one = more_stuff.pop()

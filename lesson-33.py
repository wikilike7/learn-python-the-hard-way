def print_number(i, j):
    i = 0
    numbers = []

    while i < 6:
        print('At the top i is {}'.format(i))
        numbers.append(i)
        i = i + j
        print('Numbers now: ', numbers)
        print('At the bottom i is {}'.format(i))

    print('The numbers: ')

    for num in numbers:
        print(num)

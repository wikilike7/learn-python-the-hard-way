# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: {}".format(arg1))

# this one takes no arguments
def print_none():
    print("I got nothing.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# below function is create by myself
def print_name_born(name, born):
    print("My name is {}, and i was born in {}".format(name, born))
print_name_born("Shichao Wang", "1986")

# create a new function
def degrees_celsius_to_fahrenheit():
    print("Please enter degrees celsius in next blank line:")
    degrees_celsius = int(input())
    fahrenheit = degrees_celsius * 1.8 + 32
    print("The degrees celsius is {0} C, and the fahrenheit is {1} F".format(degrees_celsius, fahrenheit))

degrees_celsius_to_fahrenheit()


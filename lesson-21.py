def add(a, b):
    print("Adding {} + {}".format(a, b))
    return a + b

def subtract(a, b):
    print("Subtracting {} - {}".format(a, b))
    return a - b

def multiply(a, b):
    print("Multiplying {} * {}".format(a, b))
    return a * b

def divide(a, b):
    print("Dividing {} / {}".format(a, b))
    return int(a / b)

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))

# A puzzle for the extra credit, type it in anyway.
print("Here os a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand")
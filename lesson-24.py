print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do \n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\t where there is none.
"""

print("----------")
print(poem)
print("----------")

five = 10 - 2 + 3 - 6
print("This should be five: {}".format(five))

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10
result = (secret_formula(start_point))
# beans, jars, crates = secret_formula(start_point)
# print("With a starting point of: {}".format(start_point))
# print("We'd have {} beans, {} jars, and {} crates.".format(beans, jars, crates))

# start_point = start_point / 10

print("We have also do that this way:")
print("We'd have {} beans, {} jars, and {} crates.".format(result))
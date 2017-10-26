from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {0} to {1}".format(from_file, to_file))

# we could do these two on one line too, how?
in_file = open(from_file)
print(type(in_file))
indata = in_file.read()
out_file = open(to_file, 'w')
out_file.write(indata)
print("Alright, all done.")
out_file.close()
in_file.close()
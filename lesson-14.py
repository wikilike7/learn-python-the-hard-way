from sys import argv
script, user_name, age = argv
prompt = '>>>'
print("Hi {}, I'm the {} script.".format(user_name, script))
print("I'd like to ask you a few questions.")

print("How old are you, {} ?".format(user_name))
user_age = input(prompt)

print("Do you like me {}?".format(user_name))
likes = input(prompt)

print("Where do you live {}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have ?")
computer = input(prompt)

print("""
Alright, so you said {} about liking me.
You live in {}. And you age is {}. Not sure where that is.
And you have a {} computer. Nice.
""".format(likes, lives, age, computer))
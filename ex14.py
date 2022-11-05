from sys import argv

script , user_name = argv
prompt = '>'

print("hi %s , I'm the %s script."%(user_name,script))
print("I'd Like to ask you a few questions.")
print("Do you like me %s?"%user_name)
likes = input(prompt)

print("where do you live %s?"%user_name)
lives = input(prompt)

print("what kind of comp do you have?")
computer = input(prompt)

print ("""
alright , so you said %r about liking me.
you live in %r. Not sure where that is .
and you have a %r computer.nice
"""%(likes,lives,computer))
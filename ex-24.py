print ("Let's Practice Everiting .")
print('you\'d need to know\'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation


\n\t\twhere there is none.
"""

print("___________")
print(poem)
print("___________")


five = 10 - 2 + 3 - 6 
print("This should be five:%s"% five)

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans/1000
	creates = jars/100
	return jelly_beans,jars,creates

start_point = 10000
beans,jars,creates = secret_formula(start_point)

print("with a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d creates. " % (beans,jars,creates))

start_point = start_point/10

print("We can also do that this way:")
print("We'd have %d beans , %d jars , and %d creates."% secret_formula(start_point))

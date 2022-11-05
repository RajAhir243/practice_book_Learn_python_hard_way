i = 0
num = []

while i < 6:
	print("At The Top i is %d" % i)
	num.append(i)

	i = i + 1
	print("Number now: ",num)
	print("At the Bottom i is %d" % i)

print("The Numbers: ")

for numbs in num:
	print(numbs)
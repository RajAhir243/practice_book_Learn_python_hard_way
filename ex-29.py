people = int(input("Value of people's: "))
cats = int(input("Value of Cat's: "))
dogs = int(input("Value of Dog's: "))

if people < cats:
	print("Too many cats ! kill them all")
if people > cats:
	print("Still kill all of the cats")
if people < dogs:
	print("The world is happy")
if dogs <people:
	print("the world is sad")

dogs += 9

if people <= dogs:
	print("now are thay equal")
if people >= dogs:
	print("Are the equal yet????")

if people == dogs:
	print("people are dogs")
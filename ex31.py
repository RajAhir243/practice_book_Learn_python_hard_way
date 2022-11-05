print("You Enter a dark room with two doors. Do You Go Through Door #1 or Door #2?")

door = input("> ")

if door == "1":
	print("There's a Giant Bear here eating cheese cake. what do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear")

	bear = input("> ")
	
	if bear == "1":
		print("The bear eats Your face off. good job!")
	elif bear == "2":
		print("The bear eats Your legs off. Good job!")
	else:
		print("Well, Doing %s is probably better. Bear runs away."% bear)

elif door == "2":
	print("You stare into the endless abyss at Cathulhu's retina.")
	print("1. BlueBerries.")
	print("2. Yellow Jacket Clothespins.")
	print("3. Understanding Revolvers Yelling Melodies.")
	
	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print("Your Body survives Powered by a mind of jello . good job")
	else:
		print("The Insanity Rots Your Eyes into A Pool of munk . goof job")
else:
	print("You stumble Around And Fall On a knife and die. good job")
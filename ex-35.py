from sys import exit 

def gold_room():
	print("This room is full of gold. how much do you take??")

	next = input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
	if how_much < 50:
		print("Nice, You're not greedy , you win !!")
		exit(0)
	else:
		dead("You greedy BASTERD!!!!!!!!!!!!!!")
	
def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in ")
	print("How are you going to move the bear????")
	bear_moved=False

	while True:
		next = input("> ")
		
		if next=="take honey":
			dead("the bear looks at you then slaps your face off.")
		elif next=="taunt bear"and not  bear_moved:
			print("the bear has moved from the door.you can go through it now.")
			bear_moved=True
		elif next=="taunt":
			("the bear gets pissed off and chews your leg off.")
		elif next=="open door" and not bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")
def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")
		
	next = input("> ")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well That was tasty!!")
	else:
		cthulhu_room()

def dead(why):
	print(why , "Good Job!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	exit(0)

def start():
	print("You are in a dark room.")
	print("There is a door to your right and left.")
	print("Which one do you take??????????????????????")

	next = input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve to DEATH!")

start()
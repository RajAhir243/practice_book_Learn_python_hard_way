people = int(input("Amount of People in The Area: "))
cars = int(input("Amount of Cars in The Area: "))
buses = int(input("Amount of Buses in The Area: "))

if cars>people:
	print("This Area is Rich")
elif cars<people:
	print("This Area is Cheap")
else:
	print("its an Average Area")

if buses>cars:
	print("That's how local peoples Travel")
elif buses<cars:
	print("Thats How Rich people Travel")
else:
	print("Its an equal match")

if people>buses:
	print("There is no need of bus ")
else:
	print("we would need more buses for Local Traveling")
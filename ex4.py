# create variables
cars = 100
space_in_a_car = 4.0	# floating point value
drivers = 30
passengers = 90
cars_not_driven = cars - drivers	# cars variable minus drivers variable
cars_driven = drivers				# each car has a driver
carpool_capacity = cars_driven * space_in_a_car		# carpool is capable of holding number of cars multiplied by space in the car
average_passengers_per_car = passengers / cars_driven	# determine average number of passengers

print "There are", cars, "cars available."		# print statement with variable cars
print "There are only", drivers, "drivers available."	# print statement with drivers variable
print "There will be", cars_not_driven, "empty cars today."	# print statement with cars_not_driven variable
print "We can transport", carpool_capacity, "people today."	# print statement with carpool_capacity variable
print "We have", passengers, "to carpool today."	# print statment with passengers variable
print "We need to put about", average_passengers_per_car, "in each car."	# print statement with average_passengers_per_car variable

#variables in python

cars = 100
space_in_car =4.0
number=1.7333
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
avg_passenger_per_car = passengers/cars_driven
#variables
#string literals
print("there are", cars, 'cars available')
print(f"let's talk about the number of cars that is {cars}")
print("there are only", drivers, "empty cars todya")
print(f"athere are {passengers} passengers but only {drivers} drivers")
print(f"rounding a number can be done with round() 1.733-> rounded is:{round(number)}")
#.format() syntax

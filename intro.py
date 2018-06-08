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

type_people = 10
x =f"there are {type_people} types of people"
binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"

print(x)
print(y)

#Python’s str.format() method of the string class
#allows you to do variable substitutions and
#value formatting. This lets you concatenate elements together within a string through positional formatting.

hilarious = False
joke_eval = "is that funny? {}"
print(joke_eval.format(hilarious))
print("is that funny {}".format("...maybe"))
print("there are  {} cars in lot".format(14))


w="left side..."
e="right side..."
print(w+e)
#formatter

formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("coke", "pepsi", "sevenup", "rootbeer"))

print(formatter.format(formatter, formatter, formatter,formatter))
print(formatter.format(
"this is another",
"substituion",
"in just strings",
"and stuff"

))
#get methods for data type
#print(help(str.lower))

#integers, floats
num = 3
print(type(num))

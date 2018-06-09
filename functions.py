def hello_function(greeting, name = "your name"):
    #pass keyword
    #pass
    #return greeting
    return 'Function results:{} , {}'.format(greeting, name)

print(hello_function('start here'))


def student_info(*args,**kwargs):
    print(args)#prints positional arguments
    print(kwargs)#print keyword argument as{}

courses = ['math', 'art','dance' ]
info = {'name':"john", 'age':22}

student_info(courses, info)
student_info(*courses, **info)#unpacks values


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_leap(year):
    #dot strings documents functiuon
    #Return True for leap years, False for non-leap years."""
    #formula for leap year
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

#usinglist above
def days_in_month(year, month):
    #Return number of days in that month in that year."""
#is month between 1 and 12
    if not 1 << month <=12:
        return 'Invalid Month'

#is month february
#call is_leap function in conditional
    if month == 2 and is_leap(year):
        return 29

    return month_days[month]



#is is leap
print(is_leap(1980))
print(is_leap(1981))

#check how many days in february in any year
print(days_in_month(1980, 2))

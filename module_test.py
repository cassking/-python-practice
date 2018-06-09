
import sys
import random #from standard lib
import math
import datetime
import calendar
import os


import modules as mm
from modules import find_index , test
courses = ['dance', 'singing', 'art', 'math']

index = mm.find_index(courses, 'math')
#can also just use .find_index()
# index = mm.find_index(courses, 'math')
print(index, test)
#print(sys.path)
random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(os.getcwd())

#tuples and sets
#mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
#imutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(list_1)
print(list_2)
list_1[0]="new history"
print(list_1)
print(list_2)


print(tuple_1)
print(tuple_2)
#tuple_1[0]="new history"#cannot be done
print(tuple_1)
print(tuple_2)
#use tuples for non mutable

#sets no duplicates
exxx_courses={'Art', 'Math','Dance', 'Physics', 'CompSci'}

ess_courses={'History', 'Math','Math', 'Physics', 'CompSci'}
print(ess_courses)
print('Math' in ess_courses)

print(ess_courses.intersection(exxx_courses))
print(ess_courses.difference(exxx_courses))

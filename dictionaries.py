
#dictionaries

student = {
1: 'Male',
'name': 'John',
'age': 25,
'courses': ['dance', 'singing']
}
print(student[1])


student['phone'] = '222-3333'
#get method
print(student.get('name'))
print(student.get('car'))#returns NONE instead of error
print(student.get('car', 'not found'))
print(student.get('phone'))
student['name'] = 'Jane'
print(student)

student.update({1: 'female','name':"Sally", 'age': 12})
print(student)

#delete
del student[1]
print(student)
print(student.pop('age'))

print(len(student))
print(student.values())
print(student.keys())

#items() method
for key, value in student.items():
    print(key,value)

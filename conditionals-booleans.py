
language = 'java'
if  True:
    print('this is true')
if language == 'python':
    print('this is true for pyth')


#OBJECT IDENTITY checks to see if same object in
# memory
if language == 'python':
    print('...language is python')
elif language == 'java':
    print('...language is java not python')
elif language == 'javascript':
    print('language is js not python')
else:
    print('no match')



user = 'admin'
logged_in = True

if user != 'admin' and logged_in:
    print('admin page')
else:
    print('not allowed')


a = [1,2,3]
b = [1,2,3]
print(a is b)
#same as
print(id(a) == id(b))

print(id(a))#diff objects
print(id(b))
#in python all these eval to false
# all else is true
condition = False
condition = None
condition = 0 #numbers eval to true
condition = () #or '', or {}, []

if condition:
    print('eval to true')
else:
    print('eval to false')

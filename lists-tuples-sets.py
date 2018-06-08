courses =['history', 'math', 'science', 'stuff']
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])#get range first index inclusive second index is not
print(courses[1:])#assumes from index to end of array
nums =[1,5,2,7,4]
courses_3 =['historyxxx', 'mathxxx', 'sciencexxx', 'stuffxxx']

#modifying lists
courses_2= ['spanish', 'english']
courses.append("art")#one value
courses.insert(0, "dance")
courses.insert(0, courses_2)
print("extend")
courses.extend(courses_2)#multiple values to add
print("append")
courses.append(courses_2)#extend vs apend
#courses.remove('stuff')

courses_3.reverse()
courses_3.sort(reverse=True)
nums.sort(reverse=True)
print(courses_3)
print(nums)

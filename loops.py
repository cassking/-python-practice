nums = [1,2,3,4,5,6,7,8]

#basics
for num in nums:
    if num == 8:
        print('found')
        break
    if num == 2:
        print('continue')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num,letter)


#range
for i in range(10):
    print('index - 1', i)

for i in range(2, 11):
    print('index', i)


x = 0
#while True:
while  x < 10:
    if x == 5:
        break #can use break to stop infinite loop
    print(x)
    x += 1 #increment otherwise stuck in infinite loop

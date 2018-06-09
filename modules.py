#importing modules

print('imported module_test ... ')

test = 'test string'

def find_index(to_search, target):
    #find the index of a value in a sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i
    #otherwise return -1
    return -1

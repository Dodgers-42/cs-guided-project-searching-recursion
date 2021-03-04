# Linear Search
def linear_search(arr, target):
    #look at every item, and check if its the one we are looking for
    for item in arr:
        if item == target:
            # We have found our item
            return True

    return False

# Recursive version of linear search

def linear_search_recursive(arr, target):
    if arr[0] == target:
        return True
    else:
        found = linear_search_recursive(arr[1:], target)
    if found:
        return found
    return False

our_array = [1, 2, 3, 4]

#IS AN ITEM IN OUR ARRAY? RETURN TRUE OR FALSE
print(linear_search_recursive(our_array, 3))


#print(f'Does number 14 exist in our array?')
#print(linear_search(our_array, 14))

#print(f'Does number 7 exist in our array?')
#print(linear_search(our_array, 7))
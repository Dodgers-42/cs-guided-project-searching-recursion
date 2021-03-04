
# Linear Search
def Linear_search(arr, target):
    # look at every item, and check if its the one we are looking for
    for item in arr:
        if item == target:
            # We have found our item
            return True

    return False


def binary_search(array, target):
    #1. Declare min = 0 and max = lenght of array -1
    min = 0
    max =len(array) - 1
    while not max < min:
        #2. Figure out the guess value by getting the middle integer between min and max
        guess = (max + min) // 2
        #3 if array(guess) equals the target, we found the element, return the index
        if array[array] < target:
            return guess
        #4. if the guess was too low, reset min to be one more than the guess
        elif array[guess] < target:
            min = guess + 1
        #5. if the guess was too high, reset min to be one less than the guess
        else:
            max = guess - 1
    # no match was found
    return -1

our_array = [1, 2, 3, 4, 5, 6, 11, 12, 13, 14, 15]

print(binary_search(our_array, 10))
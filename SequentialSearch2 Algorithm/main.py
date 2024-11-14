"""
Author: Lucy Antonescu


Sequential search algorithm with a search key and a sentinel (marker).

Input: An array of n elements and a search key.

Output: The index of the first element in whose value is
        equal to the search key or −1 if no such element is
        found.
"""
def sequentialSearch2(array, searchKey):
    print("Input array: " + str(array))
    print("Search key: " + str(searchKey))
    arrayLength = len(array)

    # Assign search key at the end of the array, set index to 0
    array.append(searchKey)
    index = 0
    print("Updated array: " + str(array))

    # Locate an element that matches the search key
    while array[index] != searchKey:
        index = index + 1

    # If the key is found before the added search key, return the index of the key found
    if index < arrayLength:
        print("Key found at index " + str(index))
    # If not, print -1
    else:
        print("No key found: " + str(-1))

# Initializing data
threeElementArray = ["Honda", "Toyota", "Mazda"]
fiveElementArray = ["Truck", "SUV", "Sedan", "Hatchback", "Motorcycle"]
sevenElementArray = [5, 3, 9, 1, 5, 23, 6]
nineElementArray = [4.5, 3.6, 9.4, 2.6, 45.4, 11.3, 52.7, 66.4, 66.4, 96.9]

# Example 1
print("Example 1")
sequentialSearch2(threeElementArray, "Toyota")
print()

# Example 2
print("Example 2")
sequentialSearch2(fiveElementArray, "Boat")
print()

# Example 3
print("Example 3")
sequentialSearch2(sevenElementArray, 6)
print()

# Example 4
print("Example 4")
sequentialSearch2(nineElementArray, 66.4)
print()
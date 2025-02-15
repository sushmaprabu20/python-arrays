# Creating an array using the array module
import array

arr = array.array('i', [1, 2, 3, 4, 5])

# Accessing elements
print("First element:", arr[0])

# Appending an element
arr.append(6)
print("After append:", arr)

# Removing an element
arr.remove(3)
print("After remove:", arr)

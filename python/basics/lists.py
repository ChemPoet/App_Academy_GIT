# Lists

#   Ordered series of values. Duplicate values are allowed.
#   Can contain strings, numbers, or other lists.
#   Lists are declared in square brackets [].

fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])
#   Lists are zero-indexed  ∴ fruits[0] refers to "apple"
print(fruits[1])
print(fruits[-1])
#   Can use "negative-indexing" to call values from the end of the list.
print()

fruits[1] = "blueberry"
#   List values are mutable, a.k.a. they can be edited. "banana" -> "blueberry"
print(fruits[0])
print(fruits[1])
print()

fruits.append("kiwi")
#   Fxn {.append()} adds values to the end of the list.
print(fruits)
fruits.insert(1, "orange")
#   Fxn {.insert(index, )} adds a value to the list at the specified index position, shifting the other values' indexes.
print(fruits)

fruits.remove("cherry")
#   Fxn {.remove()} will remove the FIRST INSTANCE of THE value in a list.
print(fruits)

fruits.sort()
#   Fxn {.sort()} automatically arranges list values in ASCENDING order. (or alphabetical)
print(fruits)

fruits.sort(reverse=True)
#   Fxn {.sort(reverse=True)} arranges list values in DESCENDING order.
print(fruits)

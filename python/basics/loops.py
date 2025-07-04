# Loops

fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(fruit)

#   Creates new variable "fruit" that itterates through the LIST "fruits"
#   Loop executes for each individual value in the list.
print()

numbers = (1, 2, 3, 5, 7)

for number in numbers:
    print(number)

#   Loops can be used with different data types. e.g.,
#   Strings:    executes loop for each value in the STRING (i.e. each CHARACTER)
#   Lists:      executes loop for each value in the LIST
print()

count = 1

while count <= 5:
    print(count)
    count += 1  #   Incrementally increases "count" by 1 after each loop.
#   Executes code repeated until certain condition is met.
#   e.g., until count >= 5
print()

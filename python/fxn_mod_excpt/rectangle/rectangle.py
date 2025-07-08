#   Request user input about the dimensions (L & W) of a rectangle.

length = float(input("\n\tEnter the length of the rectangle: "))
width = float(input("\n\tEnter the width of the rectangle: "))

import calculate

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"\n\tThe area of the rectangle is: {area}")
print(f"\n\tThe perimeter of the rectangle is: {perimeter}\n")
# Loops

fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    if fruit == "cherry":
        break       #   Exits loop when condition is met.
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        continue    #   Ignores (skips) the value when condition is met and continue 
                    #   the loop. i.e., it will ignore "cherry" and continue printing.
    print(fruit)

print()

for fruit in fruits:
    if fruit == "cherry":
        pass    #   Ignores (skips) the CONDITIONAL when VALUE is reached and 
                #   continues the loop. i.e., it WILL print "cherry".
    print(fruit)

print()


count = 0

while count <= 5:
    print(count)
    count += 1
    if count == 3:
        break   #   Exits the loop AS SOON AS count = 3. 
                #   ∴ count = 3 IS NOT printed
print()

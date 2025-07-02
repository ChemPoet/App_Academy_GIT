#Control Statements

#   Controls the flow of execution based on certain conditions.
#   e.g., IF, ELIF, ELSE

num1 = int(input("Enter your first number..."))
num2 = int(input("Enter your second number..."))


if num1 > num2:
    print(num1, " is greater than ", num2)
elif num1 < num2:
    print(num1, " is smaller than ", num2)
else:
    print("Both your numbers are equal.")
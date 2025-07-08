#Functions

#   Fxns are defined using 'def'
#   Fxns called using its name followed by '()'
#   If the fxn uses parameters, they must be specified INSIDE the '()'

def greet(name):                    #   Fxn 'greet' uses the argument 'name'.       !! NB !! REMEMBER the ":" !!
    print(f"\nHello, {name}.\n")    #   When fxn 'greet is called, ..... code will excecute using the value of 'name'.
    

greet('Alice')


#   Fxns can return a value to use elsewhere in the code

def add(a, b):                      #   Fxn name: add; Parameters: a, b.
    return a + b                    #   Fxn purpose: return the value for the operation (a + b)

result = add(2, 5)                  #   Result = Variable == value returned by fxn 'add' for parameters (2, 5)
print(result)
print()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)     #   Fxn 'factorial' relies on RECURSION - a fxn calling itself within the fxn.
    
factor = int(input("Enter a whole number between 2 and 9.\n\t"))
print("\tThe factorial of " + str(factor) + " is " + str(factorial(factor)) + ".")

    
def greet(name, greeting="Hello"):       #   Fxns can contain DEFAULT values for parameters.
    print(f"\n{greeting}, {name}.\n")    

greet('Bob')                      #   ∴ Do not NEED to pass a value for "greeting" when calling fxn greet.
greet('Bob', "Good morning")      #   However, you can specify a new/unique value for "greeting" when calling the fxn.


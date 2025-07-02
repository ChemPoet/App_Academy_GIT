#Advanced Concepts – Strings

message = 'Hello World!'

print("Index Fxns applied to '" + message + "':")
print("[0]:     " + message[0])           #   Indexing calls the value(s) stored in a specific position (index) within a string/array.
print("[1]:     " + message[1])           #   Indexes start from position 0, 1, 2, 3,...
print()

print("[-1]:    " + message[-1])          #   Indexes can be called from the back of a string/array using -1, -2, -3,...
print("[-2]:    " + message[-2])
print()


message1 = "This is Bob's world."

print(message1)             #   FXN {len()} determines the length of the string/array (i.e., number of index values).
print("Length of string = " + str(len(message1)) + " indexes.")     #   FXN {str()} changes the integer output of {len} into a string.
print()                     #   INCL. spaces, symbols, numbers, etc.


message2 = ' Hello World! '

print("The original message reads: '" + message2 + "'.")     #   FXN {.strip()} removes leading and trailing empty spaces from a string.
print("{.strip()} removes the space from the front and back of a string, so the message now reads: '" + message2.strip() + "'.")
print()                     #   FXN {.strip()} removes leading and trailing empty spaces from a string.
print("We can write the message in all lowercase using {.lower()}, e.g., : '" + message2.lower() + "'.")
print("Or we could rewrite it in all uppercase using {.upper()}, e.g., : '" + message2.upper() + "'.")
print()

message3 = "To be, or not to be?"
print('The {.split()} fxn will split the string "' + message3 + '" into a list.')
print(message3.split(','))  #   Splits the string into list using the specified deliminator (,).
print()
print("We could always just {.replace()} the subject...?")
print(message3.replace("be","EAT"))
print()
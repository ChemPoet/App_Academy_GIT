# Exception Handling

#   Exceptions  = disruption of a programme's normal runtime functions.

#   Try Block       -> Code that may raise exceptions
#   Except Block    -> Code that will execute when exceptions occur
#   Finally Block   -> Code that executes AFTER the 'try-except' blocks, REGARDLESS of whether or not there were exceptions
#   Else Block      -> Code that executes ONLY if NO exceptions were raised in the TRY block.

'''try:
    print(x)
except NameError:             #   Catch-specific exceptions
    print("Variable x is not defined.")     #   If the specified error occurs, this message will print.
except:
    print("An exception occured.")          #   If any other type of error occured, this message will print instead.'''
    
'''try:
    print(x)
except:
    print("Something went wrong.")
finally:
    print("The 'try-except' is finished.")'''

try:
    print(x)
except:
    print("Variable x is not defined.")
else:
    print("Everything went wrong.")         #   Would only have printed ELSE block if x had been a defined variable—which it is not.
    


x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero.")        #   'raise Exception' causes an ERROR MESSAGE to be DISPLAYED instead of printed!
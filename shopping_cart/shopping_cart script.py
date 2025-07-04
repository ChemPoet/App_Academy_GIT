#   SHOPPING CART

#   1) User input of data – food item, price
#   2) Loop User input until user wants to Check Out
#   3) Output all items in User input
#   4) Calculate total for all items in User input



#   VARIABLES, LISTS, DICTIONARIES
food_list = []
price_list = []
shopping_cart = {}



#   DEFINITIONS
#   Continue Shopping?
def next_item_prompt():
    while True:
        next_item = input("\nWould you like to add an item to you cart? [Y | N] \n").lower()
        if next_item == "y":
            return True
        elif next_item == "n":
            return False
        else:
            print("\nInvalid response. Please enter either [y] for Yes, or [n] for no.\n")

#   Adding items
def shopping():
    add_item = str(input("\nWhat food item would you like to add to the list today?\n"))
    print()

    food_list.append(add_item)
    'print(food_list)'

    item_price = float(input("\nHow much does the itme cost?\n[R ___.__]\n"))
    print()

    price_list.append(item_price)
    'print(price_list)'
    print()

    shopping_cart[add_item] = item_price

    'print(shopping_cart)'

#   Checking out



#   INTERFACE
print('Good day! Welcome to your Shopping Cart.\n Would you like to add an item to you cart?\n')

next_item_prompt()

shopping()



'''if bool is 
    next_item is True and check_out is False
    print("\nLet's get started!\n")
    shopping()
    
else:
    next_item is False and check_out is True
    print("\nWe look forward to seeing you again soon!\n")'''


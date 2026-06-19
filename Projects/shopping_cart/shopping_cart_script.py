
#   SHOPPING CART

#   1) User input of data – food item, price
#   2) Loop User input until user wants to Check Out
#   3) Output all items in User input
#   4) Calculate total for all items in User input



#   VARIABLES, LISTS, DICTIONARIES
food_list = []
price_list = []
shopping_cart = {}
next_item = ""



#   DEFINITIONS
#   Continue Shopping? Y|N
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
    if next_item == "y":
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
        
        next_item_prompt()
        
    elif next_item == "n":
        print("\nWould you like to proceed to Check Out?\n")



#   Check out
def check_out_output():
    total_cost = 0.00
    if len(shopping_cart) > 0 and next_item == "n":
        print("\nProcessing the items in your Shopping cart...\n")
        for key, value in shopping_cart():
            print(f'\t{key}\t{value}')
        for price in price_list:
            total_cost += total_cost + price
        print("\tTOTAL DUE:\tR" + total_cost)
    elif next_item == "y":
        print('shopping from checkout_output')
        shopping()
    else:
        print("\nWe look forward to seeing you again soon!\n")
            
        
        
    
    


#   INTERFACE
print('\tGood day! Welcome to your Shopping Cart.\n')

next_item_prompt()

shopping()

check_out_output()



'''if bool is 
    next_item is True and check_out is False
    print("\nLet's get started!\n")
    shopping()
    
else:
    next_item is False and check_out is True
    print("\nWe look forward to seeing you again soon!\n")'''


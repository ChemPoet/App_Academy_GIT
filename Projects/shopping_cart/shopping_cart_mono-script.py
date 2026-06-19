
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
print('\tGood day! Welcome to your Shopping Cart.\n')

def next_item_prompt():
    
    
    next_item = input("\n\tWould you like to add an item to you cart? [Y | N] \n").lower()
    if next_item == "y":
        total_cost = 0.00
        add_item = str(input("\n\tWhat food item would you like to add to the list today?\n"))
        print()

        food_list.append(add_item)
        'print(food_list)'

        item_price = float(input("\n\tHow much does the itme cost?\n[R ___.__]\n"))
        total_cost += item_price
        print()

        price_list.append(item_price)
        'print(price_list)'
        print()

        shopping_cart[add_item] = item_price
        'print(shopping_cart)'
        
        
    elif next_item == "n":
        if len(shopping_cart) > 0 and next_item == "n":
            print("\nProcessing the items in your Shopping cart...\n")
            for key, value in shopping_cart.items():
                print(f'\t{[key]}\t{[value]}')
            print("\tTOTAL DUE:\tR " + str(total_cost) + '.')
        else:
            print("\n\tWe look forward to seeing you again soon!\n")            
    
    else:
        print("\n\tInvalid response. Please enter either [y] for Yes, or [n] for no.\n")
    
next_item_prompt()



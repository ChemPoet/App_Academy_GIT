#   Shopping Cart

#   1) User input of data – food item, price
#   2) Loop User input until user wants to Check Out
#   3) Output all items in User input
#   4) Calculate total for all items in User input

food_list = []
price_list = []
shopping_cart = {}
next_item = True
check_out = False

add_item = str(input("""What food item would you like to add to the list today?
                     
    """))
print()

food_list.append(add_item)
    
print(food_list)

item_price = float(input("""How much does the itme cost?
    R ___.__                     
      """))
print()

price_list.append(item_price)
    
print(price_list)
print()

shopping_cart[add_item] = item_price

print(shopping_cart)

# Create shopping cart programme that will continuously ask the user for a food product and its price.
# Have an exit clause if the user wishes to stop adding more items to their cart.
# At the end, show all of the food items and the total cost to the user.


#   Declaire variables
foods = []      #   list: in order to add multiple values
prices = []     #   list: in order to add multiple values
total = 0       #   single value that can be repeatedly updated

print("\n\n\tWELCOME TO PYTHON FOODS!\n")

#   continuously == LOOPS!!
while True:
    food_item = (input("\tEnter a food to buy or press q to quit.\n\t\t"))
    #   if statement to TEST user input
    if food_item.lower() == 'q':
        break
    else:
        item_price = float(input(f"\tEnter the price of the {food_item}:\n\t\tR "))
        foods.append(food_item)
        prices.append(item_price)
        
print("\n\t-------- YOUR CART --------\n")

for food in foods:
    print(f"\t{food}")
    '''print(f"\t{food}", end= " ")'''      #   Fxn (end= " ") forces the list to print out end-over-end with a "space" in between each value.
for price in prices:
    total += price      #   total = total + price

print("\n\t---------------------------\n")
print(f"\tYour total is:\t\tR {total} \n")
print("\tTHANK YOU FOR SHOPPING WITH US!!\n")
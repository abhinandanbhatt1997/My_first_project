#requested_toppings = 'mushroom'
#if requested_toppings!= 'Anchovies': 
#	print("Hold the Anchovies!")

requested_toppings = ['pepperoni', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers' : 
		print("Sorry, we are out of green peppers right now.")
	else :
		print(f"Adding {requested_topping}.")
print("Finished making your pizza")

requested_toppings = ['chicken sausage']
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"\nAdding {requested_topping}.")
	print("\nFinished making your pizza.")

else :
	print("\nAre you sure you want your pizza without toppings ?")

#Using Multiple Lists

available_toppings = ['mushrooms','olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"\nAdding {requested_topping}.")
	else:
		print(f"\nSorry {requested_topping} is currently unavailable.")
print("\nFinished making your pizza.")

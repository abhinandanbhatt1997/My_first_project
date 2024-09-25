pizza = []
pizza.append('Margerita')
pizza.append('Veg Delight')
pizza.append('Cream Mushroom')
pizza.append('4 Cheese')

#print(pizza)

pizza.insert(0,'pan')

print(pizza)
for name in pizza:
	print(f"We have {name.title()} pizza currently available.\n")

print(f"I loovveeee pizzzaaaaaaa")

#Store info about the piza being ordered

pizza = { 'crust': 'thin-crust',
			'toppings': ['mushroom', 'extra - cheese'],
			}
#Summarize the Order
print(f"Your ordered a {pizza['crust']} crust pizza.")
for topping in pizza['toppings']:
	print("\t"+ topping)
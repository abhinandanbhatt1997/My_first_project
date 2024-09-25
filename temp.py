numbers = list(range(1,41))
print("The list of numbers is :\n",numbers)
for values in range(1,41):
	print(values)

print("This is the end of the program")

numbers = list(range(1,41))
print("The list of squares is :\n",numbers)
for values in range(1,41):
	print(values**2)

print("This is the end of the program")

#My_Pizza_your_pizza

my_pizza = ['margerita', 'onion', '4 white cheese', 'neopalitan', 'chicken delight']
print(f"\n",my_pizza)
friend_pizza = my_pizza
print(f"This is my Friend's pizza", friend_pizza)

my_pizza.append('Chicken bbq')
print(f"\nMy favourite pizzas are : \n", my_pizza)

friend_pizza.append('Mushroom bbq')
print(f"\nHowever my friend's favourite pizza's are: ", friend_pizza)

age = 19
if age >18:
	print("\nYou are old enough to vote")
	print("Have you registered to vote yet ?")

age = 56

if age<18:
	print("Age : ", age, "You are not of legal age to drink")
else:
	print("Age : ", age, "years old. Wow!", "Here's your drink. Cheers!")


dict = {'a':1, 'b':2, 'c': 3}
print(dict.keys())
print(dict.values())
print(dict.get('c'))
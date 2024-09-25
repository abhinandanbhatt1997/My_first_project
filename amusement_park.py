#Admission for anyone under age 4 is free.
#Admission for anyone between the ages of 4 and 18 is $25.
#Admission for anyone age 18 or older is $40.

age = -1

if age<4:
	print("The amusement park is free for your age group!")

elif age <=18:
	print("The amusement park fee for your age group is $25!")
else :
	print("The amusement park fee for your age group is $40")


age = 66

if age<4:
	price = 0
elif age<18:
	price = 25
elif age<65:
	price = 40
elif age >= 65:
	price = 20

print(f"Your ticket price is ${price}.")


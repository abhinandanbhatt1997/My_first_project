#Ordinal number

numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
print(numbers)

for number in numbers :
	if number == 1:
		print(f"\nThis is the {number}st number.")
	elif number == 2 :
		print(f"\nThis is the {number}nd number.")
	elif number == 3 :
		print(f"\nThis is the {number}rd number")
	elif number>3 and number<10: 
		print(f"\nThis is the {number}th number")
else :
	print(f"\nThe number {number} is not on the list.")

print("End of the program.")

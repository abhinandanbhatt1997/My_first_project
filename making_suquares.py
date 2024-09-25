number_list = []
for value in range(1,21):
	number_list.append(value)

print(number_list)

squares = []
for value in range(1,21):
	squares.append(value**2)

print(f"The list of squares from 1 to 20 is :", squares)

#Count_till_20

numbers = []
for value in range(1,21):
	numbers.append(value)
print(f"The number sequence is ", numbers)

numbers1 = []
for value in range(1,1000000):
	numbers1.append(value)
print("\nThe number sequence is quite large :\n", numbers1)

#Summing_digits_uptill_a million

numbers1 = []
for value in range(1,1000000):
	numbers1.append(value)
sum_1 = sum(range(1,1000000))
print(f"The sum is : \n", sum_1)

#Generate_odd_numbers

odd_numbers= list(range(1,30,2))
print(odd_numbers)
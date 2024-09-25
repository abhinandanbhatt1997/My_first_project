odd_number = [list(range(1,30,2))]
print(odd_number)

multiple_of_30 = [list(range(3,30,3))]
print(f"\nThe first ten multiple of 3 are : ", multiple_of_30)

first_ten_cubes = list(range(1,11))
for value in list(range(1,11)):
	first_ten_cubes.append(value**3)
	print(first_ten_cubes)

print(f"These are the first 10 cubes.")
for value in rangenge(1,10):
	print(value)

numbers = list(range(1,6))
print(numbers)

#even_numbers.py

even_numbers = list(range(2,22,2))
print(f"\n These are the even numbers {even_numbers}")

#squares.py

squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

# cubes.py

cubes = []
for values in range(10,20):
	cube = values**3
	cubes.append(cube)
print(cubes)

squares = []
for values in range(1,10):
	squares.append(values**2)
print(squares)

#Statistics

digits = [1,2,3,4,5,6,7,8,9,0]
print(digits)
min_digit = min(digits)
print(f"The minumum digit is {min_digit}\n")
max_digit = max(digits)
print(f"The max digit is {max_digit}\n")
sum_digit = sum(digits)
print(f" The sum of all the given digits is {sum_digit}\n")

#squares

squares = [value**2 for value in range(1,12)]
print(squares)
#SortingaListPermanantly

cars = ['Volkswagon','Ferrari', 'Toyota','BMW', 'Lamborghini', 'Audi', 'Porsche','Mustang','Shelby']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['Volkswagon','Ferrari', 'Toyota','BMW', 'Lamborghini', 'Audi', 'Porsche','Mustang','Shelby']

print(f"Here is the Original list of cars : ")
print(cars)
print(f"\nHere is the Sorted list of cars : ")
print(sorted(cars))

print(f"Here is the original, sorted and reverse sorted list of cars, respectively : ")
print(cars)
print(sorted(cars))
reverse_sorted = cars.sort(reverse=True)
print(reverse_sorted)


# finding the length of a list

cars = ['Volkswagon','Ferrari', 'Toyota','BMW', 'Lamborghini', 'Audi', 'Porsche','Mustang','Shelby']
len(cars)
print(f"The number of cars present in the list is {len(cars)}.")


cars = ['audi','bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())

print(bicycles[-1].title())

message = f"My first bicycle was a {bicycles[-2].title()}"

print(message)

#Modifying_elements_in_a_list

motorcycle = ['ducati', 'honda', 'triumph', 'KTM']

print(motorcycle[0])
motorcycle[0] = 'TVS'

print(motorcycle)

motorcycle.append('Benelli')
print(motorcycle)

#Appending_lists_from_scratch

motorcycle = []
motorcycle.append('Benelli')
motorcycle.append('triumph')
motorcycle.append('KTM')
motorcycle.append('Ducati')

print(motorcycle)

motorcycle=['honda', 'suzuki', 'yamaha']
print(motorcycle[0])

motorcycle.insert(0,'ducati')
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

del motorcycle[0]
print(motorcycle)

del motorcycle[1]
print(motorcycle)

#POP_Method_to_remove_an_element

motorcycle = ['honda','suzuki','yamaha']
print(motorcycle)

popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)

popped_motorcycle = motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)

#Howtorememberlastownedvehicle

motorcycle = ['honda','KTM','Benelli', 'suzuki', 'yamaha', 'R-E']
print(motorcycle)

last_owned_brand = motorcycle.pop()
print(f"My last owned brand is", last_owned_brand)
print(f" The motorcycles I have : ", motorcycle)
print(f" The next bike to sell is : ", motorcycle[4])

print(f"The last owned brand is  {last_owned_brand.title()}")
print(f"I have {motorcycle} bikes left")

motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycle)
motorcycle.remove('ducati')
print(motorcycle)

motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
print(f"\n{too_expensive.title()} is too expensive for me")

Guests = ['Eric', 'Paul', 'John', 'David', 'Joseph']
print(Guests)
absent_guest= Guests.pop()
print(f"Our guest of honor {absent_guest} could not make it.")

print(f"The last man standing in the guest list is {Guests[0]}.")

Guests = ['Eric', 'Paul', 'John', 'David', 'Joseph']
Guests.insert(0,'Moses')
print(Guests)

print(f"Hello {Guests[0]}!. Welcome to my Python practise")
print(f"Hello {Guests[1]}!. Welcome to my Python practise")
print(f"Hello {Guests[2]}!. Welcome to my Python practise")
print(f"Hello {Guests[3]}!. Welcome to my Python practise")
print(f"Hello {Guests[4]}!. Welcome to my Python practise")


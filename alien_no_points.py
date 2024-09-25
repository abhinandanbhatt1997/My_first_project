#Using get to access values

alien_0 = {'color':'green', 'speed': 'slow'}
#print(alien_0['points'])
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)

#A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color' : 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
alien_3 = {'color': 'blue', 'points': 20}
alien_4 = {'color':'purple', 'points': 25}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

#Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5 , 'speed' :'slow'}
	aliens.append(new_alien)

#Show the first 5 aliens.
for alien in aliens[:30]:
	print(alien)
print("This is it.")

# Grocery: I want to set up a counter and keep details of the items in each row.
#There are 5 rows of 5 different items.


#Make the first 10 items in row 1 'Apple'

items = [] #empty list for storing item name

for item_number in range(10):
	new_item = {'name':'apple','price': 40, 'color': 'green'}
	items.append(new_item)

#show the first 10 items

for item in items[:5]:
	print(item)
print("End of an era")

#Show how many items have been created.
print(f"Total number of created items : {len(item)}")


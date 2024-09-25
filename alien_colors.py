#alien_color = ['green', 'yellow', 'red']
#for value in alien_color:
#	print(value)

alien_color = 'v'
if 'green' or 'red' in alien_color:
	print(f"The alien color is: ", alien_color)
	print("And you just earned 5 points.")

else:
	print("The color is not green and no points for you")

alien_color = 'Green'

if 'green' in alien_color:
	print(f"The alien color is: ", alien_color)
	print("And you jus earned 5 points.")

else:
	print("The color is not green and you just earned 10 points.")



alien_color = ('orange')
if 'green' in alien_color:
	print(f"\n\n\n\nThe alien color is ",alien_color)
	print("You just earned 5 points")
elif 'red' in alien_color:
	print(f"\n\n\n\nThe alien color is ", alien_color)
	print("You just earned 10 points")
else :
	print(f"\n\n\n\nThe alien color is" ,alien_color)
	print("You just earned 15 points")


alien_0 = {'color': 'green', 'points' : 5}
print(f"\n The alien color is", alien_0['color'])
print(f"\n The points you earned for this alien are :", alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
#print(alien_0)

#Starting with an empty dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = '25'
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}.")

#Modifying values in a dictionary.
alien_0 = {'x_position': 0,'y_position': 25, 'speed': 'fast'}
print(f"Original position : {alien_0['x_position']}")

#Move the alien to the right.
#Determine how far to move the alien based on the current speed.

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3
#The new position is the old position plus the increment.

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position : {alien_0['x_position']}")

#Removing key-value pair

alien_0 ={'color': 'green', 'points': 55}
print(alien_0)
del alien_0['points']
print(alien_0)


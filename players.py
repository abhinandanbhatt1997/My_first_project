players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[1:4])
print(players[:2])
print(players[2:])
print(players[-3:])

print("Here are the names of first three players on the team:\n ")
for player in players[:3]:
	print(player.title())


users = ['Menon']

for user in users:
	if len(users) == 0 :
		print("\nWe need to find some users.")
	elif user=='admin':
		print("\nHello Administrator!\nWould you like to see daily status report?")
	else:
		print(f"Hello {user.title()}.\nWould you like to restore your previous settings?")

print("\nThis is the end of the program.")
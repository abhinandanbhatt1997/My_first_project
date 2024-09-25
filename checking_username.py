current_users = ['Jhon', 'David', 'Paul', 'Matthews', 'Moses']
new_users = ['Marry', 'King James', 'Paul', 'Andrew', 'David']

print(current_users)
#current_user_upper = current_users.upper()

for new_user in new_users:
	if new_user in current_users: 
		print(f"\nUsername {new_user} already used.")
	else :
		print(f"\nUsername {new_user} not already taken.")
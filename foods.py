my_food = ['pizza','falafel','carrot']
friends_food = my_food[:]

print("My friend foods are: ")
print(my_food)

print("\nMy friend's favourite food are: ")
print(friends_food)

my_food.append('Cannoli')
friends_food.append('Ice-Cream')

print("\nMy favourite foods are : ")
print(my_food)

print("\n My friend's favourite food are : ")
print(friends_food)

#ThisDoesn'tWork
friends_food = my_food

my_food.append('Cannoli')
friends_food.append('Ice-Cream')

print(f"My favourite foods are : ")
print(my_food)

print("\nMy friend's favourite food is : ")
print(friends_food)
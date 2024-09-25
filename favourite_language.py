requested_toppings = ['mushroom', 'onions', 'pineapple']
'mushroom' in requested_toppings

favourite_language = ' python '
favourite_language.rstrip()
favourite_language.lstrip()
favourite_language.strip()

message = "\tOne of python's greatest strengths is its supportive coder community."
print(message)

favourite_languages = {'jen': 'french', 
'arthur':'spanish',
'sarah':'c',
'edward': 'ruby',
'phil': 'python',
}
print(favourite_languages)

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite_language is {language}.")

favourite_languages = {'jen': 'french', 
'arthur':'spanish',
'sarah':'c',
'edward': 'ruby',
'phil': 'python',
}

for name, language in favourite_languages.items():
	print(f"{name.title()}'s favourite language is {language.title()}.")


#HexCode
hexcode_digit = {0:0, 1:1,2:2, 3:3, 4:4,5:5, 6:6, 7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
for hexcode, decimal_equivalent in hexcode_digit.items():
	print(f"The hexcode {hexcode} is eqvivalent to decimal {decimal_equivalent}.")

favourite_languages = {'jen': 'french', 
'arthur':'spanish',
'sarah':'c',
'edward': 'ruby',
'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
	print(name.title())
	if name in friends:
		language = favourite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favourite_languages.keys():
	print("Erin, please take our poll!")

print("\nThe following languages have been mentioned: ")
for language in favourite_languages.values():
	print(language.title())

favourite_languages = {'jen': 'python', 
'arthur':'c',
'sarah':'c',
'edward': 'ruby',
'phil': 'python',
}

print(f"The following languages have been mentioned:")
for language in set(favourite_languages.values()):
	print(language.title())

#Creating list inside a dictionary

favourite_languages = {
						'jen': ['python', 'ruby'],
						'sarah': ['c'],
						'edward' : ['ruby', 'go'],
						'phil': ['python', 'haskell'],
						}
for name, languages in favourite_languages.items():
	print(f"\n{name.title()}'s favourite languages are :")
	for language in languages:
		print(f"\t{language.title()}")

#How many languages does everyone like
for name,language in favourite_languages.items():
	if len(language)>=2:
		print(f"\t{name.title()} has more than 1 favourite languages.")
	else:
		print(f"\t{name.title()} has just 1 favourite language")
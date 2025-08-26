# Part 1: Hello, birthday month - variable and if-statements 

# Write a program that asks for your name and the month you were born in.

# Then, your program should print
# A greeting to you, using your name
# A message with the number of letters in your name
# A 'Happy birthday month!' message if you were born in the current month
# Easier - compare the user's input to "January" or "August" or whatever the current month is
# Harder - use Python to figure out the current month and use that in the comparison. Check out the datetime library.

users_name = input('Hello!! Please enter your name: ')
birthday_month = input('Enter the month you were born in: ')

print(f'Hello {users_name}')

letters_in_name = len(users_name)

print(f'You have {letters_in_name} letters in your name')

# Nice upgrade - allow month in any case
if birthday_month.lower() == 'august':
    print('Happy birthday month!')
# optional else to print a different message 
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3','4', '5', '6', '7', '8', '9']
symbols = ['!','#','$','%','&','*']
print('Welcome to pYpassword generator')
nr_letters = int(input('Enter the number of letters you want in your Password\n'))
nr_numbers = int(input('Enter the number of numbers you want in your Password\n'))
nr_symbols = int(input('Enter the number of symbols you want in your Password\n'))

list_random_letters = random.sample(letters,nr_letters)
list_random_numbers = random.sample(numbers,nr_numbers)
list_random_symbols = random.sample(symbols,nr_symbols)
list_of_items_in_passwod = list_random_letters+list_random_symbols+list_random_numbers
print(list_of_items_in_passwod)
Password = ''
for item in list_of_items_in_passwod:
    Password += random.choice(list_of_items_in_passwod)
print(Password)

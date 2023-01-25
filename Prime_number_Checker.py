a = int(input('Enter number to check for prime'))

def Check_for_prime_number(number):
    is_prime = True
    for i in range (2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f'{number} is a prime number' )
    else:
        print(f'{number} is not a prime number')


Check_for_prime_number(a)
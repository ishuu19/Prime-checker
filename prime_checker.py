# Prime number checker

def prime_checker(number):
    if number <= 1:
        print('Not Prime')
    is_prime = True
    for i in range(2, number):
        if number%i == 0:
             is_prime = False
    if is_prime:
        print(f'{number} is a Prime Number!')
    else:
        print(f'{number} is NOT a Prime Number!')


number = int(input('Check the number: '))
   
prime_checker(number)
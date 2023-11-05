
# Prime Number Checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number - 1):
        if number % i == 0:
            is_prime = False
            
            if is_prime:
                print("Its a Prime number")
            else:
                print("Its not a Prime number")
        
n = int(input("Check this number: "))
prime_checker(number = n)

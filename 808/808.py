'''reversible prime squares'''

import math
import time
import sympy.ntheory as nt

def generate_next_prime(prime):
    '''generate prime numbers: this used to be much shorter, comprised of just the following two lines - 
    nextprime = nt.nextprime(prime)
    return nextprime
    but i realized that not all the primes are being used anyways, so we'll filter out those unused ones
    '''
    if len(str(prime)) % 2 != 0:
        if str(prime)[:2] > '32' or ((str(prime))[::-1])[:2] > '32': # if you look at nums comprised solely of 9s
            # with an odd num of digits (the max num of that length), the square root is always under 3.16228 e X, 
            # where X is some positive int, so let's filter out all the numbers greater than that
            length = len(str(prime))
            while len(str(prime)) < length:
                nextprime = nt.nextprime(prime)
    elif len(str(prime)) % 2 == 0:
        if str(prime)[:2] > '10' or ((str(prime))[::-1])[:2] > '10': 
            length = len(str(prime))
            while len(str(prime)) < length:
                nextprime = nt.nextprime(prime)
    nextprime = nt.nextprime(prime)
    return nextprime

assert generate_next_prime(2) == 3
assert generate_next_prime(3) == 5

def not_palindromic(n):
    '''check if a number is palindromic'''
    return str(n) != str(n)[::-1]

assert not_palindromic(1234)
assert not_palindromic(169)
assert not_palindromic(111) == False

def gen_reverse(n):
    '''generate the reverse of a number'''
    return int(str(n)[::-1])

assert gen_reverse(123) == 321
assert gen_reverse(169) == 961

def check_root_prime(n):
    '''check if a number is a prime square'''
    root = math.sqrt(n)
    if str(root)[-1] == '0':
        root = int(root)
    if nt.isprime(root):
        return True
    return False

assert check_root_prime(25) == True
assert check_root_prime(52) == False
assert check_root_prime(961) == True

def main():
    '''put it all together'''
    st = time.time()
    reversible_prime_squares = set()
    primenum = 1
    while len(reversible_prime_squares) < 50:
        primenum = generate_next_prime(primenum)
        #print(primenum**2)
        #print("Checking prime square: {}".format(primenum**2))
        if not_palindromic(primenum**2):
            rev = gen_reverse(primenum**2)
            #print("Checking reverse: {}".format(rev))
            if check_root_prime(rev):
                reversible_prime_squares.add(primenum**2)
                reversible_prime_squares.add(rev) # i left this out the first time, this saves us a LOT of time
                print("Found reversible prime square! {} and its reverse are valid numbers. Adding to set...".format(primenum**2))
            #else:
                #print("Reverse is not a prime square...")
        #else:
            #print("Palindromic number, skipping...")
    et = time.time()
    print(reversible_prime_squares)
    print('The sum of the first 50 prime reversible prime squares is: ', sum(reversible_prime_squares))
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

if __name__ == "__main__":
    main()


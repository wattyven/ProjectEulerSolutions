'''reversible prime squares'''

import math
import time
import sympy.ntheory as nt

def generate_next_prime(prime):
    '''generate prime numbers'''
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
                print("Found reversible prime square! {} is a valid number. Adding to set...".format(primenum**2))
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


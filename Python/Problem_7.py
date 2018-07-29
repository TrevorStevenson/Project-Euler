#!/usr/bin/env python3

#print the 10001st prime number

import math

def main():
    primes = 0
    a = 2
    while primes < 10001:
        if is_prime(a):
            primes = primes + 1
            print(a)
        a = a + 1
    print(a-1)
    
def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
            
    high = math.ceil(math.sqrt(n))
    for i in range(2, high + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    main()

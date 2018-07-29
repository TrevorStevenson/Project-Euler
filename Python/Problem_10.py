#!/usr/bin/env python3

#find the sum of primes below 2 million

import math

def main():
    sum = 0
    for i in range(2, 2000000):
        if is_prime(i):
            sum += i
    print(sum)

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

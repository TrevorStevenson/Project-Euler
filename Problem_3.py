#!/usr/bin/env python3

#prints the largest prime factor of 600851475143

import math

def main():
    num = 600851475143
    high = math.ceil(math.sqrt(num))
    for i in range(high, 2, -1):
        if num % i == 0 and isPrime(i):
            print(i)
            return
            
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


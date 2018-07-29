#!/usr/bin/env python3

#determine the lowest number divisible by 1 through 20

import math

factors = dict()

def main():
    lmulti = 1
    for i in range(2,21):
        prime_factors(i)
    print(factors)
    for k, v in factors.items():
        lmulti *= int(k) ** v
    print(lmulti)

def prime_factors(n):
    if n == 1:
        return
    if is_prime(n):
        if str(n) not in factors:
            factors[str(n)] = 1
        return
                
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            num = 0
            while n % i == 0:
                num = num + 1
                n = n // i
            if str(i) in factors:
                factors[str(i)] = max(factors[str(i)], num)
            else:
                factors[str(i)] = num        

def is_prime(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True
            
    high = math.ceil(math.sqrt(n)) + 1
    for i in range(2, high):
        if n % i == 0:
            return False
    return True

    
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

#find the first triangular number to have over 500 divisors

import math

def main():
    n = 1
    while num_divisors(n * (n+1) // 2) < 500:
        n += 1
    print(n * (n+1) // 2)

def num_divisors(n):
    d = 0
    for i in range(1, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            d += 2
    return d

if __name__ == "__main__":
    main()

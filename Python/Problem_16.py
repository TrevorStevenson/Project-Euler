#!/usr/bin/env python3

#find the sum of the digits of 2^1000

def main():
    power = 1
    n = 2
    while power < 1000:
        n = n ** 2
        power *= 2
    while power > 1000:
        n = n // 2
        power -= 1
    sum = 0
    for i in str(n):
        sum += int(i)
    print(sum)

if __name__ == "__main__":
    main()

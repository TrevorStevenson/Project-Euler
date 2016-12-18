#!/usr/bin/env python3

#prints the difference between the square of the sum of the first 100 natural numbers and the sum of the squares of the same numbers

def main():
    diff(100)

def diff(n):
    sum = n * (n + 1) // 2
    square = sum * sum
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i * i
    print(square - sum)

if __name__ == "__main__":
    main()

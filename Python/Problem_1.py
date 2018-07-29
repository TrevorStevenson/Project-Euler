#!/usr/bin/env python3

#prints the sum of the multiple of 3 or 5 less than 1,000

def main():
    sum = 0
    for i in range(1,1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)


if __name__ == "__main__":
    main()

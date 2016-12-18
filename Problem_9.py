#!/usr/bin/env python3

#find the unique  pythagorean triple such that a + b + c = 1000

def main():
    for a in range(1, 999):
        for b in range (1, 999):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(a * b * c)
                return


if __name__ == "__main__":
    main()

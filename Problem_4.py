#!/usr/bin/env python3

#prints the largest palindrome that is a product of two 3 digit numbers

def main():
    palindromes = []
    for i in range(100, 1000):
        for n in range(100, 1000):
            if is_palindrome(i  * n):
                palindromes.append(i * n)
    print(max(palindromes))

def is_palindrome(n):
    num_string = str(n)
    digits = len(num_string)
    stack = []
    for i in range(0, digits // 2):
        stack.append(n % 10)
        n = n // 10

    if digits % 2 != 0:
        n = n // 10
        
    for i in range(0, digits // 2):
        if stack.pop() != n % 10:
            return False
        n = n // 10

    return True  

if __name__ == "__main__":
    main()

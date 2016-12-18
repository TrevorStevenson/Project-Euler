#!/usr/bin/env python3

#prints the sum of the even Fibonacci numbers under 4,000,000

def main():
    sum = 0
    fib = 2
    prev = 1
    
    while fib <= 4000000:
        if fib % 2 == 0:
            sum += fib
        temp = fib
        fib += prev
        prev = temp
        
    print(sum)

if __name__ == "__main__":
    main()
    

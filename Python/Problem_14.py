#!/usr/bin/env python3

#find the largest collatz sequence starting under 1 million

def main():
    max = 0
    ans = 0
    for i in range(1, 1000000):
        l = collatz_length(i)
        if l > max:
            max = l
            ans = i
    print(ans)

def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0: n = n // 2
        else: n = 3 * n + 1
        length += 1
    return length

if __name__ == "__main__":
  main()

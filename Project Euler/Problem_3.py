'''
Created on Aug 3, 2016

@author: trevorstevenson
'''

# Store number to find prime factorization.
number = 600851475143

# Create list to store factors.
factors = [number]

# Iterate through factors, determining if each number is prime. If it is, leave it. If not, remove it and replace it with 2 of its factors. 
# These new factors will then be checked if they are prime, and the cycle repeats. Splitting will stop when all numbers are prime.
def split_factors(numbers):
    for i in numbers:
        if is_prime(i) > 1:
            numbers.remove(i)
            numbers.append(is_prime(i))
            numbers.append(i // is_prime(i))
        
# Determine if given number is prime. If it is, return True. If not, return its smallest factor. 
def is_prime(number):
    for i in range(2, number // 2, 1):       
        if number % i == 0:
            return i
        
    return True
  
# Split the factors 
split_factors(factors)

# Print the largest prime factor
print(max(factors))
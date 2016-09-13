'''
Created on Aug 3, 2016

@author: trevorstevenson
'''
# Create list to store even fibonacci numbers
even_fib_numbers = []

# Generator function to yield all fibonacci numbers
def generate_fibonacci_sequence(max_value):
    # Begin at 0 with 0 and 1. a and b store previous 2 values to generate next number.
    num = 0
    a = 0
    b = 1
    # Cap the sequence at the given max value
    while num < max_value:
        # Yield next number in the sequence. Calculate next number and shift a and b 1 number to the right in the sequence. The sequence "0, 1, a, b, num" becomes "0, 1, 1, a, b"
        yield num
        num = a + b
        a = b
        b = num
        
# Iterate over fibonacci numbers. If they are even, add them to list.
for i in generate_fibonacci_sequence(4000000):
    if i % 2 == 0:
        even_fib_numbers.append(i)

# Print the sum.
print(sum(even_fib_numbers))
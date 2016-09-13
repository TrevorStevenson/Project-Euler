'''
Created on Aug 4, 2016

@author: trevorstevenson
'''
# Determine if number is palindrome
def is_palindrome(number):
    # Convert to string. Raise error if not
    try:
        number = str(number)
    except:
        raise ValueError("Must be a string or an int.")
    # Determine how many pairs of numbers must be checked
    pairs = len(number) // 2
    x = 0
    y = -1
    
    # Check if pairs of numbers are the same. If not return False.
    while x < pairs:
        if number[x] != number[y]:
            return False
        x += 1
        y -= 1
    
    return True   

# Create empty lists to hold 3 digit numbers and palindromes made from product of 3 digit numbers.
three_digit_numbers = []
palindromes = []

# Fill list of 3 digit numbers
for x in range(100, 1000, 1):
    three_digit_numbers.append(x)

# Iterate through list twice to produce every product between 3 digit numbers. Determine if each is a plaindrome. If so, add it to palindromes list.    
for x in three_digit_numbers:
    for y in three_digit_numbers:
        num = x * y
        if is_palindrome(num) == True:
            palindromes.append(num)
            
# Print the largest determined palindrome.           
print(max(palindromes))
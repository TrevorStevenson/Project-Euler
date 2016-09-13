'''
Created on Aug 11, 2016

@author: trevorstevenson
'''

factorization = dict()

def main():
    num = input("Find the lowest number that is evenly from 1 to...")
    try:
        num = int(num)
    except:
        print("You must enter a valid number")
        
    lowest_multiple(num)
   
    
def lowest_multiple(n):  
    for t in range(2, n + 1):
        prime = [t]
        split_factors(prime)
        
        for x in prime:
            try:
                prime_count = factorization["{}".format(x)]
            except:
                prime_count = 0
            if prime.count(x) >= prime_count:
                factorization["{}".format(x)] = prime.count(x)
                
    final_answer = 1
    
    for k, v in factorization.items():
        try:
            k = int(k)
        except:
            raise ValueError("Key is not of type int.")
        
        try:
            v = int(v)
        except:
            raise ValueError("Value is not of type int.")
        
        final_answer *= k ** v
    
    print(final_answer)
  
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
    if number == 0:
        return False
    elif number == 1:
        return False
    elif number == 4:
        return 2
    
    for i in range(2, number // 2, 1):       
        if number % i == 0:
            return i
        
    return True

    
if __name__ == "__main__":
    main()
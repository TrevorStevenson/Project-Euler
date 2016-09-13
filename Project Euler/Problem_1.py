'''
Created on Aug 3, 2016

@author: trevorstevenson
'''

# Create list to store multiples
multiples = []

def main(): 
    # Get input from the user.
    print("This program will find the sum of the multiples of any two factors below a certain number.")   
    input_one = input("Please enter the first factor: ")
    input_two = input("Please enter the second factor: ")
    input_three = input("Please enter the max value: ")
    
    # Ensure that input is an int.
    try:
        input_one = int(input_one)
        input_two = int(input_two)
        input_three = int(input_three)
        
    except:
        raise ValueError("You did not enter a valid number.")
    
    # Raise an error for negative numbers.
    if input_one <= 0 or input_two <= 0 or input_three <= 0:
        raise ValueError("The numbers must be above 0.")
    
    # Print the answer to the console.
    print(get_multiples(input_one, input_two, input_three))
    

def get_multiples(factor_one, factor_two, max_value):
    # Iterate over all multiples of factor one under the max value. Add them to the multiples list.
    for i in range(0, max_value, factor_one):
        multiples.append(i)
     
    # Iterate over all multiples of factor two under the max value. Add them to the multiples list if they are not also a multiple of factor one. This prevents double counting numbers.    
    for n in range(0, max_value, factor_two):
        if n % factor_one != 0:
            multiples.append(n)
    
    # Print out the sum of the numbers in the list.
    return sum(multiples)
   
if __name__ == "__main__":
    main()
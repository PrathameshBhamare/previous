# Python Program to find the factors of a number

# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           #for example the number is given 320 you can change this number from 320 to other number to find the factors of that number

num = 320

print_factors(num)
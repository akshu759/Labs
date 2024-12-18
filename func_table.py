#WAP to get a table of a number using function

def print_table(num):
    print(f"Multiplication Table of{num}:")
    for i in range(1,11):
        print(f"{num} * {i}={num*i}")
        
#Input from the user 
number = int(input("Enter a number to print its multiplication table:"))

#Function call
print_table(number)        
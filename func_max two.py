#WAP to find maximum among two number

def find_max (num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
    
#input from the user
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))   

#function call and display result
max_number= find_max(num1,num2)
print(f"The maximum number between {num1} and {num2} is {max_number}.")
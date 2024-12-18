# WAP to reverse the elements in the list
def reversed_list(input_list):
    return input_list[::-1]

user_input= input("Enter the number of elements in the list separated by spaces:")
user_list = user_input.split()


    
print("\nOriginal list:", user_list)
    
#reversing the list
reversed_list= reversed_list(user_list)
print ("Reversed list:", reversed_list)
#WAP to check whether person can vote or not using function

def can_vote(age):
    if age>= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."
    
#input from the user
age= int(input("Enter your age:"))

#function call and display the result
print(can_vote(age))   
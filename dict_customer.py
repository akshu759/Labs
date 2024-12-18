#A dictionary representing customer IDs and their correspondingcustomer names 
customer ={
    1: " Naitik Patil",
    2: "prasad patel",
    3: "pallavi bhosle",
    4: "nick chavan",
    5: "nikhil koli"
}
#accessing the customer name using the customer ID
print("The name of customer ID 1 is:", customer[1])

#adding a new customer with their ID and name 
customer[6]="Sahil padwal"

#Printing the updated dictionary
print(customer)
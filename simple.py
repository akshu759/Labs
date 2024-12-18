#WAP to calculate simple interest

def calculate_simple_interest(principal,rate_of_interest,time):
    #formula for simple interest: SI(P*R*T)/100
    simple_interest=(principal*rate_of_interest*time)/100
    return simple_interest

Principal=float(input("Enter the Principal amount:"))
rate_of_interest=float(input("Enter the rate of interest:"))
time=float(input("Enter the time period in years:"))

si=calculate_simple_interest(Principal,rate_of_interest,time)

print(f"The Simple Interest is :{si}")


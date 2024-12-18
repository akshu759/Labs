basic_salary=float(input("Enter your basic salary:"))

DA =(10/100)*basic_salary #10% of basic salary
HRA=(12/100)*basic_salary #12% of basic salary

if basic_salary> 50000:
    Total_salary= basic_salary +DA + HRA
    print(f"Your total salary is:{Total_salary} ")
else:
    print("Salary is less than or equal to 50000, no total salary calculation.")
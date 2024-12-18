#A dictionary representing students and their grades 
student_grades ={
    "sanika": "A",
    "srushti": " C",
    "kanchan":"A+",
    "Shubham":"B",
    "raj": "B-"
}

#accessing the grade of a specific student
print("Kanchan's grade is :",student_grades["kanchan"])

#adding a new student with their grade
student_grades["Ganesh"]= "C+"

#printing the updated dictionary
print(student_grades)
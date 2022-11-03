#Kane Kinder
#DEANSLIST_M02
#This app will be used to test a students gpa against the requirements needed to 
#be on the dean's list or Honor Roll.
#fname, lname= first and last name variables for student
#GPA = students gpa, as a float

lname=input("Please enter your last name: (enter ZZZ to quit) ")
if lname=="ZZZ":
    quit
else:
    fname=input("Please enter your first name: ")
    GPA=float(input("Please enter your GPA: "))
    if GPA>=3.5:
        print("Congratulations, you have made the Dean's List!")
    elif GPA>=3.25 and GPA < 3.5:
        print("Congratulations, you have made the Honor Roll!")
student_GPA=4.5
student_score=55

if student_GPA>=3.5:
     if 50<=student_score<=65:
         print("Partial scholarship")
     elif student_score>65:
         print("full scholarship")
     else:
         print("no scholarship")
else:
    print("no scholarship")
    score = int(input("your score?"))


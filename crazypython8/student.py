class student:
    school_name = "digital school"
    #student_name = "student"

    def __init__(self, name, age , course):
        self.name = name
        self.age = age
        self.course= course




student_1 = student("alce", 15, "python")
print(student_1.course)


#student_1 = student()
#print(student_1.school_name)
#print(student_1.student_name)
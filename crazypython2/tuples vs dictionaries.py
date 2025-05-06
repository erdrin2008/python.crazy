grades={
    ("john","math"):5,
    ("alice","biology"):4,
    ("bob","physics"):3.5,
    ("eve","music"):5,
    ("john","english"):4
}
#john grades in math
print(grades[("john","math")])
#add a grade to bob in math
grades[("bob","math")]=3
print(grades[("bob","math")])

#how to get all the students name
keys=list(grades.keys())
print(keys)
student, subject=keys[0]
print(student)
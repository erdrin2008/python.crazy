names=["alama","blerta","dhurata","shpati"]
for name in names:
    print(name)

#shembulli 2
    sentence_shembulli="hello, world"
    for char in sentence_shembulli:
        if char.isalpha(): #kthen true or false if char is a letter
            print(char)

#shembulli 3 me range function
for numri in range(1,6): #range(x,y) x- ku fillopm y- ku mbaron mirp nuk e perfshin y
    print(numri)
#find max ne nje list
numrat=[33,45,45,55,23,12,94,100,101,1,5]
max=numrat[0]
for num in numrat:
    if num>max:
        max=num
print("the max value of the list is",max)

#break keyword
from crazypython3.challange import score

numrat=[1,2,3,4,5,6]
target=3
for numer in numrat:
    print(numer)
    if numer==target:
        print("target found!!!!!(ˉ﹃ˉ)")
        break

#continue
scores=[65.42.57,78,35,62,50.92]
total=0
count=0
for score in scores:
    if score<50:
        continue
        total=total+score
        count+=1
mesatarja=total/count #mesatarja per vlerat e scori mbi 50
print("mesetarja e kerkuar",mesatarja)
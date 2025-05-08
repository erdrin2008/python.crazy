from os import PathLike

my_set={1,2,3,4,5,6,6,3,6,3,5,3,5,3,},
print(my_set)

my_set_1= {1, 3, 5, 6, 6, 3, 6, 3, 6}
print(my_set_1)

A={1,2,3}
B={3,4,5}

#find the union
union=A.union(B) # union = A | B
print(union)

#intersection
cut=A.intersection(B) # cut= A & B
print(cut)

#diferenca
difference=A.difference(B) #diferenca A-B
print(difference)

#diferenca symmetric
d_symmetric=A.symmetric_difference(B) #d_symmetric=A ^ B
print(d_symmetric)

#add element
A.add(6)
print(A)

#remove element
A.remove(6)

#discard - remove an element without error if it does not exist 🍖
A.discard(100)

#removes all the elements
A.clear()

#find the number  of element of a set
print(len(A))

List=[3,4,5,6]

C=set(list)
print(C)
A=(1,2,3,4,5)
number=100
#operatory in and  not in
print(number in A) # true or false if the number is from the A
print(number not in A)


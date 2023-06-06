# list can be changed and modified......
# insert order allowed can access duplicate element growable ,contains hetrogeneous element and mutable 
# we put element in square brackets[]  repetation operator * is allowed
# we can put list in list..
#we can add two list means it adds 2nd list in last of the first list
marks=[23,34,56,67,323,(2,3),33]
print(marks,(type(marks)))
print(marks[:])
print(marks[1:-1])

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
marks.append(90)   #method here 90 will be inserted in last of the list
print(marks)
marks.remove(323) #method 
print(marks)  
print("length of the list is: ",len(marks))
print(marks[len(marks)-3])
if 7 in marks:
    print("yes")
else:
    print("no")
if 67 in marks:
    print("yes")
else:
    print("no")

lst=[i for i in range(10)]
print(lst)

# lst=[i*2 for i in range(10)]
# print(lst)

# lst=[i*i for i in range(10) ]
# print(lst)

# lst=[i*i for i in range(10) if(i%2==0)]
# print(lst)
# x=[10,23,30,"csk"]
# x1=x*2  # allowed star* operator
# print(x1)

# a=[1,2,3,4,'name',"praveen",[234,45,"raman"]]  # list inn list is allowed
# print(a)

# a=[1,3,2,34,4]
# b=[1,43,54,767]
# print(a+b)
# print(a*3)
# print(a==b)
# print(a[2],'\n')  #indexing
# for i in a:
#     print(i)

# colours=['red','blue','green','black']
# print(colours)
# color= sorted(colours) # to sort a list make another variable
# print("sorted elements of colours are: ",color)
# a=[1,3,1,89,2,145,121,23,0]
# print(a)
# aa= sorted(a) # to sort a list make another variable
# print("sorted elements are: ",aa)
# print("length of colors:  ",len(colours))
# print("length of a: ",len(a))
# print("sum of the list elements: ",sum(a))

matrix_1=[[4,5,6,],[5,6,7],[7,9,0]]
matrix_2=[[41,15,16,],[25,26,27],[37,39,30]]
matrix_result=[[0,0,0],[0,0,0],[0,0,0]]
# for i in matrix_1:
#     print(i)
# for i in matrix_2:
#     print(i)

for rows in range(len(matrix_1)):
    for columns in range(len(matrix_2)):
        matrix_result[rows][columns]=matrix_1[rows][columns]+ matrix_2[rows][columns]  

print("addition of matrix is: ")
for i in matrix_result:
    print(i)
# mat=[[1,2],[3,4],[5,6]]
# mm=[[0,0,0],[0,0,0]]

# print("matrix is: ")
# for i in mat:
#    print(i)

# for rows in range(len(mat)):
#     for columns in range(len(mm)) :
#      mm[columns][rows]=mat[rows][columns]

# print("transpose of matrix is: ")
# for i in mm:
#    print(i)
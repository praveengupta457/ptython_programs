# a=input("enter you name :")
# print("you name is ",(a))
# X=input("enter first number: ")
# Y=input("enter first number: ")
# print(X+Y)
# sum=int(X)+int(Y) #we need to define the type of x and y to print sum otherwise it will ytake them as a string and output will be 2334
# print(sum)
# print(int(X)+int(Y))

# ............  read dynamic data from the keyboard these were only available in python 2 not in python 3.............

#  raw_input
# x=raw_input("enter some number") # raw input treated as string only wether we give any value

# y=input("enter some number") #input data is not considered as string we are not required typecasting we provide any value it takes


# x=input("enter any number: ") # python 3 input function acts as python 2 raw input (here we need to typecasting)

# x=input("enter some number:")  #by default type is str type 
# print(type(x))

# x=input("enetr 1st number:") 
# y=input("enetr 2nd number:") 
# # p=int(x) # now x xhanged to int
# # q=int(y) # now y xhanged to int
# print("sum of numbers is: ",int(x)+int(y))

# print("the sum is",int(input("enter 1st number"))+int(input("enter 2nd number")))

# employee data example............

# eno=int(input("enter employee number: "))
# ename=(input("enter employee name: "))
# esaler=float(input("enter employee salery: "))
# eadd=(input("enter employee address: "))
# em=bool(input("employee married or not[True/false]: "))

# print("employee number: ", eno)
# print("employee name: ",ename)
# print("employee salery: ",esaler)
# print("employee address:  ",eadd)
# print("employee marraige: ",em)

# how to read multiple values the keyboard in single line integer

# a,b=[int(x)for x in input("enter 2 values: ").split()]
# print("the sum is: ",a+b,"the producct is: ",a*b)

# # # read 2 float value from the keyboard which are seperated with (,) separation and print sum

# x,y=[float(b) for b in input("enter 2 float values: ").split(',')]  #split('any seperator') method for seperator
# print("the sum is: ",x+y)

# # how to read multiple values the keyboard in single line string

# a,b=[str(x) for x in input("enter 2 strings: ").split()]
# print(a,b)

# eval() function......to  solve any expression from keyboard.........
# p=eval("10+20+30+40")
# print(p)

# ex=input("enter any expression: ")
# result=eval(ex)
# print(result)

# #  inside eval function automatically it will be treated as same data type we input in it
# x=input("enter a list") #and you put an list as[10,20,30] this will considerd as a string 
# print(type(x))
# x=eval(input("enter data: ")) #this will considerd as a list now, what data we enter internally that will be considerd
# print(type(x))

# # reading multiple value of diff. data types ussing eval method

# p,q,r=[eval(x)for x in input("enter 3 number").split()]
# print(type(p),type(q),type(r))

#  output statement   ...print() function............................
# without any argument....print()
# 
# print("hello\ndurga\tgood morning")
print("hello"+"good morning") # we  can use any operator  using + operator both argument should be str
print("hello","good morning")
#  string operator
print("hello\t"*3)  # using * ooperator one argument should be int and other string

#  sep attribute  used to seperate bw data
a,b,c=10,20,30
print(a,b,c) # output is 10 20 30
print(a,b,c,sep=',')   # output is 10,20,30

print("hello")
print("students")
print("good")
print("morning")
# end= is used after print statement in line 
print("hello",end=' ')  # using end= attribute 'space'  output==>> hello students good morning
print("students",end=' ')
print("good",end=' ')
print("morning")

# print(10,20,30,sep=':') output of both in 2 line 
# print(50,60,70)
print(10,20,30,sep=':',end=' ') # output of both in 1 line 
print(50,60,70)
print("...list tuple and set inn single line...")
l=[10,30,20,40]
t=(100,200,300,400)
s={101,102,103,104}
print(l,end='...')
print(t,end='...')
print(s)


#  print(formatted string)
# %i===> int
# %d ==>>int
# %s==>> string
#  %f==>> float

x,y,z=10,20.4,"radhey"
l=[10,30,20,40]
print("avalue is:%i"%a)
print("avalue is:%f"%b)
print("avalue is:%s"%c)
print("the value of a %i, b %f ,c %s and l %s is "%(a,b,c,l))

# print with replacement method    {}=>> this is replacement method and after comment we use .formate() in{} we use index and in formate() we use names
name="praveen"
salary=200000
gf="none"
print("hello {0} your salary is {1} and you have {2} girlfriend".format(name,salary,gf))
print("hello {} your salary is {} and you have {} girlfriend".format(name,salary,gf))   # here order is important
print("hello {x} your salary is {y} and you have {z} girlfriend".format(z=gf,x=name,y=salary)) # here order is not important


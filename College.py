# # m=int(input("enter a numbers: "))
# # print(m)
# # print(type(m))
# # t=float(m)
# # print(type(t))

# # 
# # import random
# # print(random.randrange(1,30))

# # print("my name is praveen  (i have used double quotation)!!")
# # print('my name is praveen  (i have used single quote)')

# # print('''my name is praveen
# # i am from up from ballia dist.
# # my school was in belthra road
# # i am in pune now and persuing mca 
# # and my college name dypimr''')

# a=int(input("enetr 1st number"))
# b=int(input("enetr 2nd number"))
# # if a>b:
# #     print("a was: ",a,"b was: ",b,"a is grater than b")
# # elif a<b:
# #     print("a was: ",a,"b was: ",b,"b is greater than a")
# # else:
# #     print("both numbers are same")

# print("a is grater than b" if a>b  else "a is less than b" if a<b else "both are equal")    
# # print("both are equal" if x==y else "x is smaller than y "if x< y else "x is greater  than y")
# print("please enter your marks in the formst of (math,english,hindi,sst,science)")
# math,english,hindi,sst,science=[int (x) for x in (input("input 5 subjects marks: ")).split()]
# percentage=(math+english+hindi+sst+science)/5
# print("percentage of your exam in 5 subjects:  ",percentage)
# print("merit" if percentage >=80 and percentage <=100 else "distinctions" if percentage>=70 and percentage <=80 else "lower marks")

# year = int(input("enter a year: "))
# print("leap year" if year %4==0 else "not A LEAP YEAR" if year %400==0  else "not a leap year")

# x=input("enter a number: ")
# y= input("enter second number: ")
# print("entred numbers are: ",x,y)
# x,y=y,x
# print("swapped numbers are: ",x,y)

# import math
# x=int(input("enter a number for square root: "))
# print(math.sqrt(x))
# a=int(input("enter side a: "))
# b=int(input("enter side b: "))

# print("are ao ftriangle is: ",(a*b)/2)
# a=int(input("enter radius: "))
# print(("area of circle:" ,3.14*a**2),(" circumference is: ",2*3.14*a))
# year=int(input("entr a year: "))
# if( year %4==0 and year %100==0 or year400%==0):
#     print("leap year")
# else:
#     print("not a leap year")

# print(int(input("entr number 1: "))+int(input("enter number 2: ")))
# n1=int(input("entr number 1: "))
# n2=int(input("entr number 2: "))
# print("the numbers are{0} and {1}".format(n1 ,n2))
# print("the numbers are{1} and {0}".format(n1 , n2))
# print("addition {0} subtraction {1} multiplication {2} dividion {3}".format(n1+n2,n1-n2,n1*n2,n1/n2) )

# a=10
# b=20
# add=a+b
# print(f"number are a {a} and number 2 b={b} and addition add={add}" )

# i=2
# while i<=10:  # initialise condition print 
#     print(i,end=',')
#     i+=2
# print("the even numbers are: ")  

number=10
sum=0
for i in range(1,number+1):
    sum=sum+i
    print(sum)
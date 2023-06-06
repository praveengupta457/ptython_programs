# # #conditional statement
# # #   <,>,<=,>=,!=

# a=int(input("enter your age: "))
# print("your age is: ",a)
# # print(a>=18)
# # print(a<=18)
# # print(a==18)
# # print(a!=18)
# if(a>=18):
#         print("you can vote")
#         print("you can drive")
# else:
#         print("you cant vote")
#         print("you cant drive")
#         print("you cant do anything")  #here if the indentation is same as of line 14,15 then it will goes inside else 
# print("thank you!!!")#here the indentation is not same as of line 14,15 then it willn't go inside else now it is independent and will execute always 

# #elif.............

# a= int(input("enter a number: "))
# if(a>0):
#     print("the number is positive")
# elif(a==0):
#     print("the number is zero")
# elif(a==-999):
#     print("this is a special number")
# else:
#     print("the number is negative")

# print("thank you!!")

# #   nested if...........

# a=int(input("enter a number: "))
# if(a<0):
#     print("The number is negative")
# elif(a>0):
#     print("the number is +ve")
#     if(a>10 and a<20):
#         print("The number lies between 11-20")
#     elif(a<10 and a>0):
#         print("the number is lied b/w 0 to 10")
#     else:
#         print("the number is grester than 20")
# else:
#     print("the number is _0")        
name=input("input your name: ")
if name=="praveen":
    print("hello praveen how are you")
print("you are not a right person")
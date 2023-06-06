
#  int represent all long bol short is included in python,float,complex, string,bool,bytes,list,
#  tuple,dictionary,range,none,frozenset,set,bytearray,

a="gayyr" #here is x is name of variable so it is identifier
b=1233
c='d'
d=complex(2,7)     # to make a number complex we need to define as complex first
print("type of a is",type(a),(a))
print("id of a is: ",id(a))
print("type of b is",type(b),(b))
print("id of b is: ",id(b))
print("type of c is",type(c),(c))
print("id of c is: ",id(c))
print("type of d is",type(d),(d))
print("id of d is: ",id(d))

# binary number

a=0b101110   #the method to give binary to python we need to give 0b or 0B before a binary no. 

b=-0B110010
print(a)
print(b,type(b))
print(type(a))

#octal [0 to 7 followed by (0o zero and o)to make octsl]
octal=0o77772
print(octal,type(octal))

# heaxdecimal (base 16) allowed (0 to 9 and a to f) a to f in any case upper or lower  followed by 0x

hexa=0x4737adf
print(hexa,type(hexa))
#we get output in decimal form

#converting from one type to  another type

#float to int==int()
#int to float==float()
#int to strint==str()
#complex no. can't be converted to int and float but can be in  bool()
#  all fundamental data types are immutable

# range of data types.........

# int 0 to 256  at the time python interpreter starts:....integer objects will be created at the begining (0 to 256)
# bool always (0,1)
# string always 
# flot and complex cant be reusable they will creat their object seperate
#bytes must be in the range 0 to 256....(1) and it is immutable
# byte and bytearray  are same but bytearray are mutable in python only byte is not present but there is bytes

f=int(132.345)
print(type(f))

by=[10,20,30,40] 
b=bytes(by)  # nnow list has been changed to bytes and its range should be  0 to 256 ie==10,20,30,40 if values are greater than 256 and smaller than 0 it will show an error
print(type(b)) 

# bb=[-1,34,344]
# bt=byte(bb)     after running this program will sho an error because of range of bytes
# print(type(bt))
x=[10,30,4,5,3,33,89]
b=bytearray(x)
print(type(b))

b[0]=123  # 10 will be replaced by 123 coz bytearray is mutable
for i in b: print(i)
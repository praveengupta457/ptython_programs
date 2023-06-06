#operators  ==>>
#1.arithmetic operator    +,-,*,/, // (floor division), % **(exponent operator)
# 2.relational operator   
# 3.logical operator
# 4.bitwise operator
# 5.assignment operator
# 6.special operator

# a=10
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)   # it always gives float value
# print(a//b)  # gives integer value and float value both
# print(a%b)   # reamainder 
# print(a**b)   # it means 10*10==100
# print("")
# a=10.5
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)   # it always gives float va,ue
# print(a//b)  # gives integer value and float nearest (integer value both
# print(a%b)   # reamainder 
# print(a**b)   # it means 10*10==100

# st='abc'+3 this will give error but not in java:>> st='abc'+3  /TypeError: can only concatenate str (not "int") to str
# print(st)
# st='abc\t'*3  # star* operator is allowed in python wih string but should be only int and string value
# print(st)

# #   RELATIONAL OPERATOR....(>,<,<=,>=,==)

# x=10
# y=20
# print("x>y",x>y)
# print("x>=y",x>=y)
# print("x<y",x<y)
# print("x<=y",x<=y)
# print("x==y",x==y)
# print(" ")

# x=10
# y=20
# print("x>y",x>y)
# print("x>=y",x>=y)
# print("x<y",x<y)
# print("x<=y",x<=y)
# print("x==y",x==y)

# print(" ")

# x="Praveen"
# y="praveen" # unicode value of p > P so it will compare all alphabet in the string 
# print("x>y",x>y)
# print("x>=y",x>=y)
# print("x<y",x<y)
# print("x<=y",x<=y)
# print("x==y",x==y)

# bitwise operator (&,|,^,~,<<,>>) applicable only for int and boolean

# 4 & 5 valid and 10.5& 2.5 invalid TypeError: unsupported operand type(s) for &: 'float' and 'float'
#  & if both are 1 then only 1 otherwise 0
#  |  atleast 1 should be 1 for 1 ootherwise 0
# ^(x-or) if both arguments are diffrent 1,0 then 1 otherwise 0
#  ~( bitwise complement operator) 1 will beome 0 and 0 become 1
#  << ( bitwise left shift operator)
#  >> ( bitwise right shift operator)

# x=10 & 2
# print("and: ",x) # ans 2 

# x=10 | 2
# print("or: ",x)  # ans 10

# x=10 ^ 2
# print("x-or: ",x)  #ans 8

# increment and decrement are not available in python ++x is treated as +(+x)
# y=(10<12)? True:False in pyhton tertiary operator are not available like this it is available as a english statement
# print(y)

#  in pyhton tertiary operator are available

# y=True if 10<20 else False
# print(y)
# y=True if 10>20 else False
# print(y)
# print("spaces")
# a=1000 if 20>30 else 2000 if 20>30 else "galat"
# print(a)

# z=int(input("enter first 'z' number: "))
# w=int(input("enter second 'w' number: "))
# e=int(input("enter third 'e' number: "))

# p="z is greater of all" if (z>w and z>e) else "w is greater of all" if w>z and w>e else " e is greater of all" if e>z and e>w else "please enter unequal nummber"
# print(p)   # this will give max of all
# q="z is minumum of all" if (z<w and z<e) else "w is minumum of all" if (w<z and w<e) else "e is minumum of all" if (e<z and e<w) else "please enter unequal nummber"
# print(q)  # this will give min of all

# z=int(input("enter first 'z' number: "))
# w=int(input("enter second 'w' number: "))
# e=int(input("enter third 'e' number: "))

# q="z is minumum of all" if (z<w and z<e) else "w is minumum of all" if (w<z and w<e) else "e is minumum of all" if (e<z and e<w) else "please enter unequal nummber"
# print(q)


# x=int(input("enter 1st number: "))
# y=int(input("enter 2nd number: "))
# print("both are equal" if x==y else "x is smaller than y "if x< y else "x is greater  than y")

#  1. special operator 
#   1a. identity operator
#   1b. membership operator

# a=10
# b=10
# print(a is b)      # true
# print(a is not b)  # false

# #  taking this eg as a string

# x="praveen"
# y="praveen"
# print(id(x))
# print(id(y))
# print(x is y) # 'is' operator compzres address of object
# print(x is not y)

# #  takin this eg as a list

# lst=[10,20,30]
# lstt=[10,20,30]
# print(lst is lstt) # false because list is immutable and create diffrent adrs Location 
# print(id(lst))   #2190378943104 adrs
# print(id(lstt))  #2190378891968 adrs
# print(lst == lstt) # ans== true because '==' operator will compares element and 'is' operator compzres address of object

#  'in' and 'in not'
ls=[10,20,30, "rohan","buddy"]
print(10 in ls) 
print(40 not in ls)  
print("rohan" in ls)
print("")
s="hello brother"
print(""in s)
print("Hello" in s)  # case senstive
print("hello" in s)

#  unary> binary> ternary operator priority
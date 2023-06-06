# # tuples are unchangable/immutable we cant't append the tuple and can't change the element and fillled inside () braces and seperated by commas(,)
# tup=(1,2,3,4,5,"RAM", "happy",[7,9]) # we use a list like element in tuple here [7,9] is an element 
# print(type(tup),tup)
# print(tup)
# print("length of tuple is: ",len(tup))
# print(tup[5])

# #...........................................................................................................................
# tt=(1)
# print(tt,type(tt))  #here it will show the type int but not tuple to make it tuple we need to pyt (,) after single element
# #now here on putting , after 1 it will tell tupe tuple
# tt=(1,)
# print(tt,type(tt))
# #...........................................................................................................................

# if "happy" in tup:
#     print("yes *happy* it is present")
#     tata=tup[5:7]
#     print(tata)

# #methods of tuple

# country=("BHATRAT", "NEPAL" ,"SRI LANKA", "OMAN", "UAE")
# cc=country*2
# print(country)
# print("using star operator: ",cc)
# lst=list(country)  # made a temprory list and now in list we can add and remove the elements so--
# lst.append("RUSSIA")  #adding "russia" in list
# print(lst) 
# lst.remove("OMAN")  #rempving "oman" from list
# print(lst)
# country=tuple(lst) #again convrting list into tuple
# print(country) #printimng tuple type of country

# tuple1= (1,2,6,4,6,5,6,7,8,6)
# tp=tuple1.count(6)  #count method count the no. of occurence of elements in tuple
# print("count of tuple is: ",tp)
# tp=tuple1.index(7)
# print("index of element is: ",tp)
# tp=len(tuple1)
# print("length of tuple is: ",tp)

a=(1,2,3,4)
# b=(5,6,7,8)
# print(a+b)
# print(a*3)
# print(a==b)
# print(len(a)==len(b))
# for i in a:
#     print(i)

# # conversion
# c=(a,b)
# print(c)
# name="rajan"
# print(name,type(name))
# # changing string to tuple
# st_to_tup=tuple(name)
# print(st_to_tup)

# sub=("python", " OT"," AIT"," SPM","ADBMS")
# print(sub)
# for i in sub:
#     print(i)
# print(sub[1:4:3])    
# print(sub[::3])    
# x=sub.count("AIT")
# print(x)  # count is an inbuild  function of tuple

# reverse paking
# student="grade","baburao",8
# x,y,z =student
# print(x)
# print(y)
# print(z)

# reverse=student[::-1]
# print(reverse)
x=[1,2,3]
y=[4,5,6]
zipped=zip(x,y)  # zip method combines the index values in tuple
print(list(zipped))
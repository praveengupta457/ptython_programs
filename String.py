#  we can put any value in string either integer,float,string,hypecasting
# a string is sequence of characters 
#there is no char  character in python

Name="praveen gupta"
name='''ergheuighig
fgfggfg fjhg vffg ggg '''   #3''' me ye 3 """ me diffrent line ek  string bn jati h
print(Name)
print(name)
print(Name[2])  #indexing
print("using for loop\n")
for character in name:
    print(character)

#....... STRING SLICING method **s[begin:end]

names="ravan,meghnath"
print(names[0:13])
#negative slicing
print((names[0:-10]))   #counts reverse including 0 but not 10
print(len(names[0:-10])) #count number of words
print(len(names))
print(names[-5:-1])
print(names,"contains ",len(names)," words")
nm="harry"
print(nm[-4:-2])

#........cases uppr and lower.............................

a="ram ji !!!!"
b="LAKSHMAN ji"
c="ravan"
print(a)
print(a.upper())
print(a.rstrip("!"))
print(b.lower())
print(c)
print(c.center(20))
print(c.replace("ravan","sita"))
print(len(a.capitalize()))

an="ram"   #here the values of every refrence variable is same so they should point to ame memory location
an1="ram"
an2="ram"
an3="ram"
# now here we havw made another rv as an3 with the value "lala" will chnge the address  of both an3 
an3="lala"
print(id(an))     # memory location of an 2045360436448
print(id(an1))    # memory location of an1 2045360436448
print(id(an2))    # memory location of an2 2045360436448
print(id(an3))    # memory location of an3 2045360436448   all are same..... after become    2094389289216
print(id(an3))     # memory location of an3   2094389289216


#     .....**********ESCAPE CHARACTER*********...........
    #  \n to break line \t for a tab we use \r go to first position of that line, \b, \f page down go to next page,\',\",\\,\v

s="abcd\nefgh"
print(s)    

s="abcd\tefgh"
print(s)  

st= '"RAM"is a very good boy'
st1= "'RAM'is a very good boy"
st2= "\"RAM\" is a very good boy"
st3='''"RAM" is a good 'indian' boy'''
st4=""""RAM" is a good 'indian' boy"""
print(st)
print(st1)
print(st2)
print(st3)
print(st4)

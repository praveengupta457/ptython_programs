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
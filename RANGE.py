# range immutable and is datatype and function it is not applicable for float

r=range(10) #it ends end-1 ie. upto 0 to 9
print(r,type(r))
for i in r:
    print(i)
r1=range(10,20)  # 10 to 19
for x in r1: print(x)

r2=range(10,50,5) # 10 to 49 by incrementing 5 each
for y in r2: print(y)
#.....................................
# x3=range(10.3)
# for xx in x3: print(xx)  # this will showw error because 10.3 is a float which is not valid
#.....................................

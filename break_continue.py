
for i in range(1,11):
    print("5X",i,"=",5*i)
    i=i+1
    if(i==8):
        break
print("out of loop and i becomes 8")  
print(" ")
print(" ")


for i in range(1,11):
    print("5X",i,"=",5*i)
    i=i+1
    if(i==8):
        continue
print("loop continues")   
print(" ")
print(" ")

for i in range(1,11):
    print("5X",i,"=",5*i)
    i=i+1
    if(i==8):
     pass
print("loop passed")  

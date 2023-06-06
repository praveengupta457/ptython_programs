
# ISME ERROR HAI
import time
samay=time.strftime('%H:%M:%S')
print(samay)
if(int(samay< 12,00,00)):
    print("good morning")
elif(int(samay > 12,00,00 and samay<16,00,00)):
    print("good afternoon")
    if(int(samay>16,00,00 and samay<20,00,00)):
       print("good evening")
else:
    print("good night")


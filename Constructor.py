# #  constructor  (__init__)
# class Employee:
#     # no_of_leaves=8
#     def __init__(self,aname,asalary,aroll):
#       self.name=aname
#       self.salary=asalary
#       self.roll=aroll
#     def display(self):
#         print("the name is: ",self.name,"salary is: ",self.salary,"and role is: ",self.roll)

# tt=Employee("praveen",50000,"developer") 
# tt.display()
# print(tt.roll)

class Area:
    def __init__(self,a,b):
        self.length=a
        self.breadth=b
        print("i m in constructor")   
    def area(self):
            self.aa=self.length*self.breadth
            print("area of rrectangle is: ",self.aa)
p=Area(4,5)
p.area()
           
# class Area:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("i m in constructor")
#     def area(self):
#         self.aa=self.a*self.b
#         print("area of rrectangle is: ",self.aa)
# length=int(input("enter length of rectangle: "))    
# breadth=int(input("enter breadth of rectangle: "))            
# p=Area(length,breadth)
# p.area()
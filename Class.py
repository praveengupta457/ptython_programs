# class Student:
#     pass

# p=Student()
# n=Student()
# p.name='praveen'
# p.standerd="MCA"
# n.name='naveen'
# n.standerd="MCA"
# n.subjects="hindi","english"
# # print(p.name,p.standerd)
# # print(n.name,n.standerd,n.subjects)

# class Employee:
#     no_of_leaves=8  # iska object se koi mtlb nhi h 
#     pass


# him=Employee()  # object
# her=Employee()      # object
# him.name='male'   #instance variable
# him.salery=12334    #instance variable
# him.role='developer'
# her.name='female'
# her.salery=12345
# her.role='rester'
# print(him.name,him.salery,him.role,him.no_of_leaves)
# print(her.name,her.salery,her.role,her.no_of_leaves)

# Employee.no_of_leaves=12   # here only class can help in updating the values 
# print("no of leaves is increased: ",her.name,her.salery,her.role,her.no_of_leaves)


# class Employee:
#     no_of_leaves=8  # iska object se koi mtlb nhi h 
#     def printdetails(self):
#         return f"Name is {self.name} salery is{self.salery} and role is {self.role}"

# him=Employee()  # object
# her=Employee()      # object
# him.name='mendal'   #instance variable
# him.salery=12334    #instance variable
# him.role='developer'
# her.name='ladki'
# her.salery=12345
# her.role='tester'
# print(him.name,him.salery,him.role,him.no_of_leaves)
# print(her.name,her.salery,her.role,her.no_of_leaves)

# Employee.no_of_leaves=12   # here only class can help in updating the values 
# print("no of leaves is increased: ",her.name,her.salery,her.role,her.no_of_leaves)
# print(him.printdetails())
# print(her.printdetails())


class rectangle():
    
    def calc(self,a,b):
        self.area=a*b
        print("area of rectangle is: ",self.area)
rec=rectangle()
rec.calc(4,4)


# 1.>>class... 2.>>object 3.>>refrence variable
# 1. class== a blueprint of templete,model,design... and class is a specification and design to create multiple object
#    class repersent the data members , proprty and behaviour of object.

# 2. object==a physical existenece of a class..or an instance of class is called object
# one to many (from one class we can create many objects)

# 3.refrēnce variable> used to refer object we can perform operation on the objecets and (object can have n number of ref. var)
#  using reference variable we can access the property and method of an object 
# e.g...a model of tv say sony 12 model >> has n number of copies and are some action can be performed on it using remote 
# (where tv model is [class] , n number copies is[object] and [remote] is reference variable) 

# static variable .. variable that not varries from object to object called static variable
# instance variable .. variable that varries from object to object called instance variable

#  class studdent...
#  every student has diffrence name ,roll, age etc etc but the school name is static so student data are instance variable and school is static variable 
# various places to declare static variable 1> within the class directly and outside of any method and constructor

# class student:
#     def  check_pass_fail(self):
#         if self.marks>=40:
#             print("passed in subject")
#         #  return True
#         else:
#             print("failed in subject")
#         #    return False
# student1=student()
# student1.name="praveen"
# student1.marks=88

# student2=student()
# student2.name="naveen"
# student2.marks=39
# pass_fail = student1.check_pass_fail()
# pass_fail1 = student2.check_pass_fail()
# print(student1.name,"is: ",pass_fail)
# print(student2.name,"is: ",pass_fail1)

# class add{
#     int a,b;
#     add(int a,int b){
#         this.a=a;
#         this.b=b;
#     }
#     void summ(){
#     int sum=a+b;
#      System.out.println("the sum of two number is: "+ sum);
#     }

# }
# public class ab{
# public static void main(String[] args) {
#   add  ss=new add(4,6);
#     ss.summ();
# }
# }

# class add:
#     sum=0
#     def __init__(self,a,b):
#         self.sum=a+b
#     def ss(self):
#         print("sum is: ",self.sum)
# ob=add(2,3)
# ob.ss()



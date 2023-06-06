# diff bw set and list is >>in set duplicate is not allowed and insertion order is not followed
#in set  hetrogeneous element is allowed
# slicing not allowed ,we can append and remove eleemnt
# set is represent in{} brackets


# a={10,20,30,40,"ramesh"}
# print(a,type(a)) # in output order is not important
# #a[0]   this show error oz set does't follow inserting/indexing order
# print(a)
# a1={10,20,30,40,10,20,30} # here output is like a coz duplicate element is not allowed
# print(a1,type(a1))
# a.add("ashish")
# print(a)
# a.remove("ramesh")
# print(a)
# s=set()
# for i in range(10):
#  print(s)
#  s.add(i)

# a=set('nihira')
# b=set('school')

# print(a)
# print(b)
# # print(a-b)
# print(a+b)
# # print(a*b)
# print(a|b)
set={i for i in range(10)}
print(set)

months={'jan','feb','march','april'}
print(months)
months.add('may')
print(months)

# months.update(['june','july'])
# print(months)
months.discard('january')#when element not present in the set,using discard method to delete that element will not show error 
print(months)
months.remove('january') #when element not present in the set,using remove method to delete that element will show error
print(months)
# dictionary holds (key>>and their corresponding values) duplicate key is not allowed but duplicate value is allowed values and keu ccan be hetrogeneous
#dictionary is also represented in {} as set, dict is mutable

d={100:'om',101:'aum',103:'any',104:'one'} #key value pair
print(d,type(d))
d[90]="ongc" #we can append element like this
print(d,type(d))
d[100]='haha' # here om will be replaced with haha
print(d,type(d))
dd=set()
d1={} # this is by default a dictionary  not set to make it set we need to declare it as d1=set()
print(type(d1))
print(type(dd))
dict={1:'ram',2:'shyam',3:'lakhan'}
print(dict)
print(1 in dict)
print(all(dict))
# print(dir(dict))
di=dict.fromkeys(dict,'kuch bhi')
print(di)
print(dict.get(2))  # grt method
dict.update({2:'gagat'})   # update funcrtiion 
print(dict)
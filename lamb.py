
import functools

no=[2,5,4,6,12,3,24,56,0,10]
max_no=functools.reduce(lambda a,b : a if a> b else b,no)
print(max_no)



"""fruits=['apple','orange','peaches']
final_list=list(map(lambda fruits : fruits.upper(),fruits))
print(final_list)"""
                
                
                
"""list1=[5,6,7,8,9,34,12,56,34]
final_list=list(map(lambda x:x*2,list1))
print(final_list)"""

"""def oddnumber(x):
    if x%2 !=0:
        return x
number=[2,3,4,5,6,7,8,9,10]

calc_odd=list(filter(oddnumber,number))
print(calc_odd)"""

#oddnumber=list(filter(lambda number : number%2!=0,number))

#print(oddnumber)



"""age=[13,20,45,60,12,5,9,10]

adults = list(filter(lambda age : age>18,age))

print(adults)"""




"""max = lambda a,b: a if(a>b) else b

print(max(5,10))"""


"""is_even_list = [lambda items=x : items * 10 for x in range(1,5)]


for item in is_even_list:
    print(item())"""






"""b=lambda a : a+10
c=lambda a,b,c : a*b*c

print(b(10))
print(c(10,10,10))


def calc(n):
    return lambda a:a*n


result=calc(4)
result2=calc(6)
print(result(10)) 
print(result2(10))"""
    

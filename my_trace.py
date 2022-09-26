import pdb

def add(a,b):
    result=a+b
    return result

pdb.set_trace()

x=input("Enter first number :")
y=input("Enter second number :")
sum=add(x,y)
print(sum)
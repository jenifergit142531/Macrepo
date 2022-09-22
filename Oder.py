
def recursivefn(n):
    if(n>0):
        result=n+recursivefn(n-1)
        print(result)
    else:
        result=0
    return result    

print("Recursive function implemented :")
recursivefn(4) 


"""def empty():
    pass"""
    
 



"""def fahrenheit(celcius):
  return 95 * celcius +32.


print(fahrenheit(30))
print(fahrenheit(20))
print(fahrenheit(10))"""




"""def movies(mname):
    for x in mname:
        print(x)
        
mname=["pushpa","kgf","x-men"]
movies(mname) """       




"""def place(hometown="Chennai"):
    print("I am from "+hometown)

place("Gurgaon")
place("pune")
place()
place("cochin")"""



"""def products(**items):
    
    print("Items in the order : " +items["item1"])
    
products(item1="Milk",item2="Egg",item3="Bread")  """



"""def products(*items):
    
    for x in items:
     print("The items in the order is "+x)
     products("Milk","Butter","Bread","Eggs","Jam","Fruits","Ham")    

     """
     
"""def products(item1,item2,item3):
    
    print("Items in the order : " +item1)
    
products(item1="Milk",item2="Egg",item3="Bread")  """
     
    
    









"""def order(orderid,items):
    print("order received")
    print("order id :",orderid)
    print("Items :",items)
    
    
order(101,5)"""
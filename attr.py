class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        
        #create object for the class
s=Student("Mira",101,24) 

# built in attributes
print(s.__dict__)
print(s.__doc__)
print(s.__module__)

    #built in functions    
        #print the attribute value 
print(getattr(s, 'name'))
        
        #reset the value
setattr(s, "age", 21)
        
        #check if the attribute is contained
print(hasattr(s,'sid'))
        
        #delete the attribute
delattr(s,'id')
        
print(s.id)
        
    
    